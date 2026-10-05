#!/usr/bin/env python3
"""Montagem de uma música completa do Chef Bolinha (vídeo horizontal 16:9).

Uso:
    python scripts/montar_musica.py musicas/m01-chapeu-voador

Lê <musica>/mapa.yaml, corta cada trecho do clipe indicado, junta tudo em 1920x1080 a 24 fps
e coloca a música do Suno por cima (áudio do Veo descartado, -14 LUFS).
Clipe que ainda não existe vira tela cinza, para dar para acompanhar a música se completando.
Tudo o que é gerado vai para <musica>/montagem/.

Formato do mapa.yaml (tempos em segundos da música; cada trecho começa onde o anterior acaba):

    musica: musica.wav
    trechos:
      - {ate: 20.4, clipe: c01, nome: "Intro + Verso 1"}
      - {ate: 30.1, clipe: c02}
      - {ate: 37.5, clipe: c02, desde: 10}      # desde: segundo do clipe onde o trecho começa
      - {ate: 57.0, clipe: c03, espelhar: true}  # espelhar: inverte na horizontal
      - {ate: fim, clipe: c09}                   # fim: até o final da música
"""
import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

W, H, FPS = 1920, 1080, 24
COR_FALTA = "0x5A6470"  # cinza-azulado: clipe ainda não gerado


def run(cmd, capturar=False):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        sys.stderr.write(r.stderr[-3000:])
        raise RuntimeError(f"falhou: {' '.join(map(str, cmd[:6]))} ...")
    return r.stderr if capturar else r.stdout


def duracao(arq):
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                      str(arq)]).strip())


def tamanho(arq):
    out = run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height",
               "-of", "csv=p=0", str(arq)])
    return tuple(map(int, out.strip().split(",")))


def mmss(t):
    return f"{int(t // 60)}:{t % 60:05.2f}"


def achar_clipe(pasta, nome):
    p = pasta / "clipes" / nome
    if p.suffix:
        return p if p.exists() else None
    return next((p.with_suffix(e) for e in (".mp4", ".mov", ".webm") if p.with_suffix(e).exists()), None)


def filtro(larg, alt, espelhar, frames):
    """Leva o clipe a 1920x1080; outra proporção fica inteira no centro sobre fundo desfocado."""
    if abs(larg / alt - W / H) < 0.02:
        f = f"scale={W}:{H}:flags=lanczos,setsar=1"
    else:
        f = (f"split=2[f][g];[f]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=40:2[fundo];"
             f"[g]scale={W}:{H}:force_original_aspect_ratio=decrease:flags=lanczos[frente];"
             f"[fundo][frente]overlay=(W-w)/2:(H-h)/2,setsar=1")
    if espelhar:
        f += ",hflip"
    # quadros a mais para o caso de o clipe acabar antes do trecho (último quadro congelado)
    return f + f",fps={FPS},tpad=stop={frames}:stop_mode=clone"


def preparar_audio(musica, dur, trab):
    """Música inteira, completada com silêncio ou cortada na duração do vídeo; loudnorm -14 LUFS (2 passadas)."""
    bruto = trab / "audio_bruto.wav"
    run(["ffmpeg", "-y", "-v", "error", "-i", str(musica), "-af",
         f"aresample=48000,apad,atrim=0:{dur:.4f},afade=t=out:st={dur - 0.05:.4f}:d=0.05",
         "-ac", "2", "-c:a", "pcm_s24le", str(bruto)])
    medida = run(["ffmpeg", "-hide_banner", "-i", str(bruto), "-af",
                  "loudnorm=I=-14:TP=-1.0:LRA=11:print_format=json", "-f", "null", "-"], capturar=True)
    j = json.loads(medida[medida.rfind("{"):medida.rfind("}") + 1])
    final = trab / "audio_final.wav"
    run(["ffmpeg", "-y", "-v", "error", "-i", str(bruto), "-af",
         f"loudnorm=I=-14:TP=-1.0:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:"
         f"measured_LRA={j['input_lra']}:measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true,"
         f"aresample=48000", "-c:a", "pcm_s24le", str(final)])
    conf = run(["ffmpeg", "-hide_banner", "-i", str(final), "-af", "loudnorm=print_format=json", "-f", "null", "-"],
               capturar=True)
    return final, float(json.loads(conf[conf.rfind("{"):conf.rfind("}") + 1])["input_i"])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pasta", help="pasta da música, ex.: musicas/m01-chapeu-voador")
    args = ap.parse_args()

    import yaml
    t0 = time.time()
    pasta = Path(args.pasta).resolve()
    mapa = yaml.safe_load((pasta / "mapa.yaml").read_text(encoding="utf-8"))
    musica = pasta / mapa.get("musica", "musica.wav")
    if not musica.exists():
        sys.exit(f"Música não encontrada: {musica}")
    dur_musica = duracao(musica)
    out = pasta / "montagem"
    trab = out / "_trabalho"
    trab.mkdir(parents=True, exist_ok=True)

    # cada trecho vira um segmento com número exato de quadros, contado a partir do início da música
    # (assim os arredondamentos não se acumulam e o vídeo não sai de sincronia)
    linhas, segs, avisos = [], [], []
    de = 0.0
    for k, t in enumerate(mapa["trechos"], 1):
        ate = dur_musica if str(t["ate"]).lower() == "fim" else float(t["ate"])
        q_ini, q_fim = round(de * FPS), round(ate * FPS)
        frames = q_fim - q_ini
        if frames <= 0:
            sys.exit(f"Trecho {k}: 'ate' ({ate}) precisa ser maior que o fim do trecho anterior ({de}).")
        desde = float(t.get("desde", 0))
        nome_clipe = str(t["clipe"])
        clipe = achar_clipe(pasta, nome_clipe)
        seg = trab / f"seg_{k:02d}.mp4"
        precisa = frames / FPS
        if clipe is None:
            situacao = "**falta** (tela cinza)"
            run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", f"color=c={COR_FALTA}:s={W}x{H}:r={FPS}",
                 "-frames:v", str(frames), "-c:v", "libx264", "-preset", "medium", "-crf", "18",
                 "-pix_fmt", "yuv420p", str(seg)])
        else:
            larg, alt = tamanho(clipe)
            sobra = duracao(clipe) - desde
            situacao = "ok"
            if sobra < precisa - 0.05:
                situacao = f"clipe curto: {precisa - max(sobra, 0):.1f}s com o último quadro congelado"
                avisos.append(f"Trecho {k} ({nome_clipe}): {situacao}")
            run(["ffmpeg", "-y", "-v", "error", "-ss", f"{desde:.3f}", "-i", str(clipe), "-an",
                 "-vf", filtro(larg, alt, t.get("espelhar", False), frames),
                 "-frames:v", str(frames), "-c:v", "libx264", "-preset", "medium", "-crf", "16",
                 "-pix_fmt", "yuv420p", str(seg)])
        segs.append(seg)
        linhas.append(f"| {k} | {t.get('nome', '')} | {mmss(de)}–{mmss(ate)} | {precisa:.2f}s | {nome_clipe}"
                      f"{f' (desde {desde:g}s)' if desde else ''}{' espelhado' if t.get('espelhar') else ''} | "
                      f"{situacao} |")
        print(f"[{k}/{len(mapa['trechos'])}] {mmss(de)} a {mmss(ate)} {nome_clipe}: {situacao}", flush=True)
        de = ate

    dur_video = round(de * FPS) / FPS
    if abs(dur_video - dur_musica) > 0.5:
        avisos.append(f"O mapa acaba em {mmss(dur_video)}, mas a música tem {mmss(dur_musica)}.")

    lista = trab / "lista.txt"
    lista.write_text("".join(f"file '{s.name}'\n" for s in segs), encoding="utf-8")
    video = trab / "video.mp4"
    run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lista), "-c", "copy", str(video)])

    audio, lufs = preparar_audio(musica, dur_video, trab)
    final = out / "final.mp4"
    run(["ffmpeg", "-y", "-v", "error", "-i", str(video), "-i", str(audio), "-map", "0:v", "-map", "1:a",
         "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", str(final)])

    faltam = sorted({str(t["clipe"]) for t in mapa["trechos"] if achar_clipe(pasta, str(t["clipe"])) is None})
    rel = [f"# Montagem: {pasta.name}", "",
           f"Gerado por `scripts/montar_musica.py` em {time.strftime('%Y-%m-%d %H:%M')} "
           f"({time.time() - t0:.0f}s).", "",
           f"- Música: `{musica.name}` ({mmss(dur_musica)})",
           f"- Vídeo: {W}x{H}, {FPS} fps, {mmss(dur_video)}; áudio do Veo descartado",
           f"- Loudness final: **{lufs:.1f} LUFS** (alvo -14, pico real -1 dBTP)",
           f"- Clipes que faltam: {', '.join(faltam) if faltam else 'nenhum'}", "",
           "| # | Trecho | Tempo | Duração | Clipe | Situação |", "|---|---|---|---|---|---|", *linhas, ""]
    if avisos:
        rel += ["## Avisos", "", *[f"- {a}" for a in avisos], ""]
    (out / "relatorio.md").write_text("\n".join(rel), encoding="utf-8")
    print(f"Pronto: {final}\nFaltam: {', '.join(faltam) if faltam else 'nenhum'}")
    for a in avisos:
        print(f"Aviso: {a}")


if __name__ == "__main__":
    main()
