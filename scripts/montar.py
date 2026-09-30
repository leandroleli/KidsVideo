#!/usr/bin/env python3
"""Montagem automática de um episódio do Chef Bolinha (substitui o CapCut).

Uso:
    python scripts/montar.py episodios/ep02-vaquinha-nuvem [--video X.mp4] [--musica Y.wav]

Tudo o que é gerado vai para <episodio>/montagem_auto/. Nenhum arquivo existente
do episódio é alterado.

Etapas: loop (SSIM) -> música (intro, BPM, corte na batida) -> Demucs + faster-whisper
(alinhamento da letra) -> legendas .ass karaokê -> render 1080x1920 H.264/AAC -14 LUFS.
Efeitos sonoros: lidos de efeitos.yaml (pulados se não houver arquivos).
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
import time
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path

import numpy as np

W, H = 1080, 1920
FONTE_ARQ = Path("C:/Windows/Fonts/ARLRDBD.TTF")  # Arial Rounded MT Bold
FONTE_NOME = "Arial Rounded MT Bold"

# Paleta do personagem.md
COR_ACESO = "#F7CB3D"     # amarelo das penas: palavra já cantada
COR_APAGADO = "#F8F6F2"   # branco do chapéu: palavra ainda não cantada
COR_CONTORNO = "#1F4E5F"  # turquesa dos olhos bem escurecido, para contraste

# Área da legenda (fração da tela): céu no alto, à direita da janela do celeiro.
# Fica longe do terço inferior (título/canal do Shorts) e dos botões laterais.
CAIXA_X0, CAIXA_X1 = 0.34, 0.965
CAIXA_TOPO = 0.06

LIMIAR_LOOP = 0.90
CROSSFADE_S = 0.4
TEMPO_CONF_BAIXA = 0.5


# ---------------------------------------------------------------- utilidades

def run(cmd, cwd=None, capturar=False):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        sys.stderr.write(r.stderr[-3000:])
        raise RuntimeError(f"falhou: {' '.join(map(str, cmd[:6]))} ...")
    return r.stderr if capturar else r.stdout


def duracao(arq):
    out = run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(arq)])
    return float(out.strip())


def normalizar(p):
    p = unicodedata.normalize("NFD", p.lower())
    p = "".join(c for c in p if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]", "", p)


def cor_ass(hexcor, alfa=0):
    h = hexcor.lstrip("#")
    return f"&H{alfa:02X}{h[4:6]}{h[2:4]}{h[0:2]}".upper()


def log(msg):
    print(msg, flush=True)


# ---------------------------------------------------------------- entradas

def achar_entradas(ep, args, trab):
    vids = ep / "videos"
    if args.video:
        video = Path(args.video)
    else:
        video = None
        for nome in ("completo_20s.mp4", "completo.mp4"):
            if (vids / nome).exists():
                video = vids / nome
                break
        # O Gemini devolve os 20s emendados na 2ª geração (salvo como parte2.mp4)
        if video is None and (vids / "parte2.mp4").exists() and duracao(vids / "parte2.mp4") > 15:
            video = vids / "parte2.mp4"
        if video is None and (vids / "parte1.mp4").exists() and (vids / "parte2.mp4").exists():
            video = trab / "concat.mp4"
            lista = trab / "concat.txt"
            lista.write_text(f"file '{(vids / 'parte1.mp4').as_posix()}'\nfile '{(vids / 'parte2.mp4').as_posix()}'\n")
            run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lista), "-an",
                 "-c:v", "libx264", "-crf", "12", str(video)])
    if args.musica:
        musica = Path(args.musica)
    else:
        musica = next((vids / f"musica.{e}" for e in ("wav", "mp3", "m4a", "flac") if (vids / f"musica.{e}").exists()), None)
    if not video or not video.exists():
        sys.exit("Vídeo do Gemini não encontrado (use --video).")
    if not musica or not musica.exists():
        sys.exit("Música não encontrada (use --musica).")
    return video, musica


def ler_letra(ep):
    """Letra da seção 6 do episodio.md (bloco depois de **Lyrics:**), sem as tags do Suno."""
    md = (ep / "episodio.md").read_text(encoding="utf-8")
    m = re.search(r"^## 6\..*?\*\*Lyrics:\*\*\s*```[^\n]*\n(.*?)```", md, re.S | re.M)
    if not m:
        return None
    linhas, secao = [], ""
    for bruta in m.group(1).splitlines():
        s = bruta.strip()
        if not s:
            continue
        tag = re.fullmatch(r"\[(.+?)\]", s)
        if tag:
            secao = tag.group(1).strip().lower()
            continue
        linhas.append({"texto": s, "secao": secao, "refrao": "chorus" in secao or "refr" in secao})
    return linhas


def ler_tabela_efeitos(ep):
    """Tabela 'Efeitos sonoros' da seção 6, para montar o modelo de efeitos.yaml."""
    md = (ep / "episodio.md").read_text(encoding="utf-8")
    m = re.search(r"\*\*Efeitos sonoros.*?\n\n((?:\|.*\n)+)", md)
    itens = []
    if m:
        for linha in m.group(1).splitlines()[2:]:
            cols = [c.strip() for c in linha.strip("|").split("|")]
            if len(cols) >= 2:
                t = re.search(r"[\d,\.]+", cols[0])
                itens.append({"tempo": float(t.group(0).replace(",", ".")) if t else 0.0,
                              "efeito": cols[1], "arquivo": "", "volume_db": 0})
    return itens


# ---------------------------------------------------------------- 1. loop

def analisar_loop(video):
    import cv2
    from skimage.metrics import structural_similarity as ssim

    cap = cv2.VideoCapture(str(video))
    fps = cap.get(cv2.CAP_PROP_FPS)
    quadros = []
    while True:
        ok, f = cap.read()
        if not ok:
            break
        quadros.append(cv2.cvtColor(cv2.resize(f, (216, 384), interpolation=cv2.INTER_AREA), cv2.COLOR_BGR2GRAY))
    cap.release()
    n = len(quadros)
    inicio = range(0, min(n, round(fps)))
    fim = range(max(0, n - round(3 * fps)), n)
    melhor = (-1.0, 0, n - 1)
    for i in inicio:
        for j in fim:
            s = ssim(quadros[i], quadros[j], data_range=255)
            if s > melhor[0]:
                melhor = (s, i, j)
    nota, i, j = melhor
    return {"fps": fps, "quadros": n, "i": i, "j": j, "nota": float(nota),
            "duracao": (j - i) / fps, "crossfade": nota < LIMIAR_LOOP}


def filtro_video(loop, largura, altura):
    """Corta o loop (quadros i..j-1), aplica crossfade fim->começo se preciso e leva a 1080x1920."""
    fps, i, j = loop["fps"], loop["i"], loop["j"]
    partes = []
    if loop["crossfade"]:
        x = max(2, round(CROSSFADE_S * fps))
        n = j - i
        ini = max(0, i - x)
        partes.append(f"[0:v]split=2[a][b]")
        partes.append(f"[a]trim=start_frame={i}:end_frame={j},setpts=PTS-STARTPTS[corpo]")
        if i > 0:
            falta = x - (i - ini)
            pad = f",tpad=start={falta}:start_mode=clone" if falta else ""
            partes.append(f"[b]trim=start_frame={ini}:end_frame={i},setpts=PTS-STARTPTS{pad}[pre]")
        else:
            partes.append(f"[b]trim=start_frame=0:end_frame=1,setpts=PTS-STARTPTS,tpad=stop={x - 1}:stop_mode=clone[pre]")
        partes.append(f"[corpo][pre]xfade=transition=fade:duration={x / fps:.4f}:offset={(n - x) / fps:.4f}[v0]")
    else:
        partes.append(f"[0:v]trim=start_frame={i}:end_frame={j},setpts=PTS-STARTPTS[v0]")

    if abs(largura / altura - W / H) < 0.01:
        partes.append(f"[v0]scale={W}:{H}:flags=lanczos,setsar=1[v]")
    else:  # outra proporção: vídeo inteiro no centro sobre fundo desfocado
        partes.append(f"[v0]split=2[f][g]")
        partes.append(f"[f]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=40:2[fundo]")
        partes.append(f"[g]scale={W}:{H}:force_original_aspect_ratio=decrease:flags=lanczos[frente]")
        partes.append(f"[fundo][frente]overlay=(W-w)/2:(H-h)/2,setsar=1[v]")
    return ";".join(partes)


# ---------------------------------------------------------------- 2/3. música, voz e letra

def separar_voz(musica, trab):
    saida = trab / "voz.wav"
    if saida.exists():
        return saida
    import librosa
    import soundfile as sf
    import torch
    from demucs.apply import apply_model
    from demucs.pretrained import get_model

    modelo = get_model("htdemucs")
    modelo.eval()
    y, sr = librosa.load(str(musica), sr=modelo.samplerate, mono=False)
    if y.ndim == 1:
        y = np.stack([y, y])
    wav = torch.tensor(y, dtype=torch.float32)
    ref = wav.mean(0)
    wav = (wav - ref.mean()) / ref.std()
    with torch.no_grad():
        fontes = apply_model(modelo, wav[None], device="cpu", split=True, overlap=0.25, progress=False)[0]
    fontes = fontes * ref.std() + ref.mean()
    voz = fontes[modelo.sources.index("vocals")].numpy().T
    sf.write(str(saida), voz, modelo.samplerate)
    return saida


def analisar_musica(musica, voz):
    import librosa
    y, sr = librosa.load(str(musica), sr=22050, mono=True)
    tempo, batidas = librosa.beat.beat_track(y=y, sr=sr)
    bpm = float(np.atleast_1d(tempo)[0])
    batidas = librosa.frames_to_time(batidas, sr=sr)

    v, vsr = librosa.load(str(voz), sr=22050, mono=True)
    hop = 441  # 20 ms
    rms = librosa.feature.rms(y=v, hop_length=hop)[0]
    ativo = rms > 0.15 * rms.max()
    # 1º trecho com voz sustentada por pelo menos 100 ms
    inicio_voz = 0.0
    for k in range(len(ativo) - 5):
        if ativo[k:k + 5].all():
            inicio_voz = k * hop / 22050
            break
    return {"bpm": bpm, "batidas": [float(b) for b in batidas], "inicio_voz": inicio_voz,
            "duracao": len(y) / sr}


def planejar_corte(info, dur_video, inicio_forcado=None):
    """Escolhe início (regra do gancho) e fim na batida; devolve fator de atempo."""
    batidas = info["batidas"]
    periodo = 60 / info["bpm"]
    ini = 0.0
    if inicio_forcado is not None:
        ini = inicio_forcado
    elif info["inicio_voz"] > 1.0:  # introdução instrumental: canto tem de entrar no 1º segundo
        cands = [b for b in batidas if 0 <= info["inicio_voz"] - b <= 1.0]
        ini = cands[0] if cands else info["inicio_voz"] - 0.5
    # fim numa batida, com o menor ajuste de andamento possível (máx. ±5%)
    grade = [b for b in batidas if b > ini] + [batidas[-1] + k * periodo for k in range(1, 4)]
    grade = [b for b in grade if b <= info["duracao"] + 1e-3]
    fim, fator = None, None
    for b in grade:
        f = (b - ini) / dur_video
        if 0.95 <= f <= 1.05 and (fator is None or abs(f - 1) < abs(fator - 1)):
            fim, fator = b, f
    obs = ""
    if fim is None:  # música curta demais para bater numa batida: usa o que tem e completa com silêncio
        fim = min(info["duracao"], ini + dur_video)
        fator = 1.0
        obs = "sem batida compatível dentro de ±5%; corte sem ajuste de andamento"
    return {"inicio": ini, "fim": fim, "fator": fator, "obs": obs}


def transcrever(voz, letra, modelo_nome):
    from faster_whisper import WhisperModel
    modelo = WhisperModel(modelo_nome, device="cpu", compute_type="int8")
    prompt = " ".join(l["texto"] for l in letra)
    segs, _ = modelo.transcribe(str(voz), language="pt", word_timestamps=True, beam_size=5,
                                initial_prompt=prompt, condition_on_previous_text=False, vad_filter=False)
    palavras = []
    for s in segs:
        for w in s.words or []:
            if normalizar(w.word):
                palavras.append({"palavra": w.word.strip(), "ini": w.start, "fim": w.end, "prob": w.probability})
    return palavras


def alinhar(letra, palavras):
    """Needleman-Wunsch entre as palavras da letra e as do Whisper (semelhança difusa)."""
    tokens = []
    for li, l in enumerate(letra):
        for p in l["texto"].split():
            tokens.append({"linha": li, "texto": p})
    a = [normalizar(t["texto"]) for t in tokens]
    b = [normalizar(p["palavra"]) for p in palavras]
    n, m = len(a), len(b)
    GAP = -0.4
    dp = np.zeros((n + 1, m + 1))
    dp[:, 0] = np.arange(n + 1) * GAP
    dp[0, :] = np.arange(m + 1) * GAP
    sim = np.zeros((n, m))
    for x in range(n):
        for y in range(m):
            sim[x, y] = SequenceMatcher(None, a[x], b[y]).ratio()
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            casa = dp[x - 1, y - 1] + (2 * sim[x - 1, y - 1] - 1)
            dp[x, y] = max(casa, dp[x - 1, y] + GAP, dp[x, y - 1] + GAP)
    x, y, pares = n, m, {}
    while x > 0 and y > 0:
        if dp[x, y] == dp[x - 1, y - 1] + (2 * sim[x - 1, y - 1] - 1):
            if sim[x - 1, y - 1] >= 0.5:
                pares[x - 1] = y - 1
            x, y = x - 1, y - 1
        elif dp[x, y] == dp[x - 1, y] + GAP:
            x -= 1
        else:
            y -= 1

    for k, t in enumerate(tokens):
        if k in pares:
            p = palavras[pares[k]]
            t.update(ini=p["ini"], fim=p["fim"], ouvido=p["palavra"],
                     conf=round(float(p["prob"] * sim[k, pares[k]]), 3), interpolado=False)
        else:
            t.update(ini=None, fim=None, ouvido=None, conf=0.0, interpolado=True)

    # Linhas sem nenhuma palavra reconhecida: não foram cantadas neste corte
    cantadas = {t["linha"] for t in tokens if not t["interpolado"]}
    tokens = [t for t in tokens if t["linha"] in cantadas]
    # Interpola palavras faltantes entre vizinhas reconhecidas
    k = 0
    while k < len(tokens):
        if tokens[k]["ini"] is not None:
            k += 1
            continue
        e = k
        while e < len(tokens) and tokens[e]["ini"] is None:
            e += 1
        antes = tokens[k - 1]["fim"] if k > 0 else None
        depois = tokens[e]["ini"] if e < len(tokens) else None
        qtd = e - k
        if antes is None:
            antes = depois - 0.35 * qtd
        if depois is None:
            depois = antes + 0.35 * qtd
        passo = (depois - antes) / qtd
        for q in range(qtd):
            tokens[k + q]["ini"] = antes + q * passo
            tokens[k + q]["fim"] = antes + (q + 1) * passo
        k = e
    return tokens, sorted(set(range(len(letra))) - cantadas)


# ---------------------------------------------------------------- 4. legenda

def quebrar(palavras, fonte_pil, largura_max):
    linhas, atual = [], []
    for p in palavras:
        teste = " ".join(atual + [p])
        if atual and fonte_pil.getlength(teste) > largura_max:
            linhas.append(atual)
            atual = [p]
        else:
            atual.append(p)
    linhas.append(atual)
    return linhas


FONTE_MIN, FONTE_MAX = 80, 100


def fonte_pil(tam):
    from PIL import ImageFont
    f = ImageFont.truetype(str(FONTE_ARQ), tam)
    asc, desc = f.getmetrics()
    # libass: tamanho = altura (ascendente + descendente); PIL: tamanho = em
    return ImageFont.truetype(str(FONTE_ARQ), max(1, round(tam * tam / (asc + desc))))


LARGURA_CAIXA = (CAIXA_X1 - CAIXA_X0) * W - 2 * 8  # desconta o contorno


def tamanho_2_linhas(palavras):
    """Maior fonte (libass) em que o verso cabe na caixa em até 2 linhas."""
    for tam in range(FONTE_MAX, 40, -2):
        if len(quebrar(palavras, fonte_pil(tam), LARGURA_CAIXA)) <= 2:
            return tam
    return 40


def layout(palavras, tam):
    """Quebra o verso no tamanho dado, equilibrando a largura das linhas."""
    f = fonte_pil(tam)
    linhas = quebrar(palavras, f, LARGURA_CAIXA)
    lmin = LARGURA_CAIXA
    while lmin > 200 and len(quebrar(palavras, f, lmin - 10)) == len(linhas):
        lmin -= 10
    linhas = quebrar(palavras, f, lmin)
    # não deixa artigo/conjunção solto no fim da linha ("faz o / chapéu")
    for k in range(len(linhas) - 1):
        while len(linhas[k]) > 1 and len(normalizar(linhas[k][-1])) <= 2 and not linhas[k][-1].endswith(","):
            nova = [linhas[k][-1]] + linhas[k + 1]
            if f.getlength(" ".join(nova)) > LARGURA_CAIXA:
                break
            linhas[k + 1] = nova
            linhas[k] = linhas[k][:-1]
    return [len(l) for l in linhas]


def gerar_ass(tokens, letra, so_refrao, dur, destino):
    x_centro = round((CAIXA_X0 + CAIXA_X1) / 2 * W)
    y_topo = round(CAIXA_TOPO * H)
    cab = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Karaoke,{FONTE_NOME},84,{cor_ass(COR_ACESO)},{cor_ass(COR_APAGADO)},{cor_ass(COR_CONTORNO)},{cor_ass(COR_CONTORNO, 0x60)},0,0,0,0,100,100,1,0,1,7,4,8,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    def ts(t):
        t = max(0.0, t)
        cs = round(t * 100)
        return f"{cs // 360000}:{cs // 6000 % 60:02d}:{cs // 100 % 60:02d}.{cs % 100:02d}"

    grupos = {}
    for t in tokens:
        grupos.setdefault(t["linha"], []).append(t)
    ordem = sorted(grupos)
    # Um tamanho só para o vídeo todo (o de pior caso entre todos os versos), entre FONTE_MIN e FONTE_MAX;
    # verso que não couber em 2 linhas nesse tamanho vai para 3.
    tam = max(FONTE_MIN, min(tamanho_2_linhas([w["texto"] for w in grupos[li]]) for li in ordem))
    eventos = []
    for pos, li in enumerate(ordem):
        if so_refrao and not letra[li]["refrao"]:
            continue
        ws = grupos[li]
        ini = ws[0]["ini"] - 0.25
        prox = grupos[ordem[pos + 1]][0]["ini"] - 0.25 if pos + 1 < len(ordem) else dur
        fim = min(max(ws[-1]["fim"] + 0.5, ws[-1]["ini"] + 0.6), prox, dur)
        if fim <= 0 or ini >= dur:
            continue
        ini = max(0.0, ini)
        cortes = layout([w["texto"] for w in ws], tam)
        partes = [f"{{\\an8\\pos({x_centro},{y_topo})\\fs{tam}\\fad(80,80)}}"]
        cursor = ini
        k = 0
        for n_linha, qtd in enumerate(cortes):
            for q in range(qtd):
                w = ws[k]
                espera = round((w["ini"] - cursor) * 100)
                if espera > 0:
                    partes.append(f"{{\\k{espera}}}")
                prox_ini = ws[k + 1]["ini"] if k + 1 < len(ws) else w["fim"]
                dur_p = max(8, round((min(prox_ini, w["fim"] + 0.15) - w["ini"]) * 100))
                sep = " " if q < qtd - 1 else ""
                partes.append(f"{{\\kf{dur_p}}}{w['texto']}{sep}")
                cursor = w["ini"] + dur_p / 100
                k += 1
            if n_linha < len(cortes) - 1:
                partes.append("\\N")
        eventos.append(f"Dialogue: 0,{ts(ini)},{ts(fim)},Karaoke,,0,0,0,,{''.join(partes)}")
    destino.write_text(cab + "\n".join(eventos) + "\n", encoding="utf-8-sig")
    return len(eventos)


# ---------------------------------------------------------------- 5/6. áudio e render

def preparar_audio(musica, corte, dur, efeitos, trab):
    """Corta/ajusta a música, mistura efeitos, fades curtos e loudnorm -14 LUFS (2 passadas)."""
    fator = corte["fator"]
    cadeia = f"[0:a]atrim=start={corte['inicio']:.4f}:end={corte['fim']:.4f},asetpts=PTS-STARTPTS,aresample=48000"
    if abs(fator - 1) > 0.002:
        cadeia += f",atempo={fator:.5f}"
    cadeia += f",apad,atrim=0:{dur:.4f}[mus]"
    entradas = ["-i", str(musica)]
    rotulos = ["[mus]"]
    for k, e in enumerate(efeitos):
        entradas += ["-i", str(e["caminho"])]
        ms = round(e["tempo"] * 1000)
        cadeia += f";[{k + 1}:a]aresample=48000,volume={e.get('volume_db', 0)}dB,adelay={ms}|{ms}[e{k}]"
        rotulos.append(f"[e{k}]")
    if len(rotulos) > 1:
        cadeia += f";{''.join(rotulos)}amix=inputs={len(rotulos)}:normalize=0:duration=first[mix]"
    else:
        cadeia += ";[mus]anull[mix]"
    cadeia += f";[mix]afade=t=in:d=0.02,afade=t=out:st={dur - 0.03:.4f}:d=0.03,atrim=0:{dur:.4f}[out]"
    bruto = trab / "audio_bruto.wav"
    run(["ffmpeg", "-y", "-v", "error", *entradas, "-filter_complex", cadeia, "-map", "[out]",
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
    lufs = json.loads(conf[conf.rfind("{"):conf.rfind("}") + 1])["input_i"]
    return final, float(lufs)


def render(base, audio, ass, saida, cwd):
    """Queima a legenda (caminhos relativos a cwd para evitar escapes do Windows no filtro)."""
    run(["ffmpeg", "-y", "-v", "error", "-i", str(base), "-i", str(audio),
         "-vf", f"ass={ass.relative_to(cwd).as_posix()}:fontsdir=_trabalho/fontes",
         "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "slow", "-crf", "18",
         "-profile:v", "high", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
         "-shortest", "-movflags", "+faststart", str(saida)], cwd=cwd)


# ---------------------------------------------------------------- principal

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("episodio", help="pasta do episódio, ex.: episodios/ep02-vaquinha-nuvem")
    ap.add_argument("--video", help="vídeo do Gemini (padrão: detectado em videos/)")
    ap.add_argument("--musica", help="música do Suno (padrão: videos/musica.*)")
    ap.add_argument("--whisper", default="medium", help="modelo do faster-whisper (padrão: medium)")
    ap.add_argument("--inicio-musica", type=float,
                    help="força o ponto (s) da música que cai no 1º quadro, em vez da regra do gancho")
    ap.add_argument("--refazer", action="store_true", help="ignora o cache (voz separada e transcrição)")
    args = ap.parse_args()

    t0 = time.time()
    tempos = {}
    ep = Path(args.episodio).resolve()
    out = ep / "montagem_auto"
    trab = out / "_trabalho"
    if args.refazer and trab.exists():
        shutil.rmtree(trab)
    (trab / "fontes").mkdir(parents=True, exist_ok=True)
    shutil.copy(FONTE_ARQ, trab / "fontes" / FONTE_ARQ.name)

    video, musica = achar_entradas(ep, args, trab)
    log(f"Vídeo: {video}\nMúsica: {musica}")

    # 1. loop
    t = time.time()
    loop = analisar_loop(video)
    dur = loop["quadros"] and (loop["j"] - loop["i"]) / loop["fps"]
    log(f"[1] Loop: quadro {loop['i']} ({loop['i'] / loop['fps']:.3f}s) <- quadro {loop['j']} "
        f"({loop['j'] / loop['fps']:.3f}s), SSIM {loop['nota']:.3f}, crossfade={loop['crossfade']}, duração {dur:.3f}s")
    larg, alt = map(int, run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                              "stream=width,height", "-of", "csv=p=0", str(video)]).strip().split(","))
    base = trab / "video_base.mp4"
    run(["ffmpeg", "-y", "-v", "error", "-i", str(video), "-filter_complex", filtro_video(loop, larg, alt),
         "-map", "[v]", "-an", "-c:v", "libx264", "-preset", "medium", "-crf", "12", "-pix_fmt", "yuv420p", str(base)])
    dur = duracao(base)
    tempos["loop + vídeo base"] = time.time() - t

    # letra
    letra = ler_letra(ep)
    aviso_letra = ""
    if not letra:
        aviso_letra = "Letra não encontrada na seção 6: transcrita pelo Whisper (sem correção)."

    # 2/3. voz, música e alinhamento
    t = time.time()
    voz = separar_voz(musica, trab)
    tempos["Demucs"] = time.time() - t
    t = time.time()
    info = analisar_musica(musica, voz)
    corte = planejar_corte(info, dur, args.inicio_musica)
    log(f"[2] BPM {info['bpm']:.1f}; voz entra em {info['inicio_voz']:.2f}s; corte {corte['inicio']:.3f}-"
        f"{corte['fim']:.3f}s; andamento x{corte['fator']:.4f}")
    tempos["análise da música"] = time.time() - t

    t = time.time()
    cache_tr = trab / f"whisper_{args.whisper}.json"
    if cache_tr.exists():
        palavras = json.loads(cache_tr.read_text(encoding="utf-8"))
    else:
        palavras = transcrever(voz, letra or [], args.whisper)
        cache_tr.write_text(json.dumps(palavras, ensure_ascii=False, indent=1), encoding="utf-8")
    tempos["faster-whisper"] = time.time() - t
    if not letra:
        letra = [{"texto": " ".join(p["palavra"] for p in palavras), "secao": "", "refrao": True}]
    tokens, nao_cantadas = alinhar(letra, palavras)
    # tempo da música original -> tempo do vídeo final
    for tk in tokens:
        tk["ini_video"] = round((tk["ini"] - corte["inicio"]) / corte["fator"], 3)
        tk["fim_video"] = round((tk["fim"] - corte["inicio"]) / corte["fator"], 3)
    no_video = [tk for tk in tokens if tk["fim_video"] > 0 and tk["ini_video"] < dur]
    fora = sorted({tk["linha"] for tk in tokens} - {tk["linha"] for tk in no_video})
    (out / "letra_alinhada.json").write_text(json.dumps({
        "letra": letra, "palavras_whisper": palavras,
        "alinhamento": [{k: v for k, v in tk.items()} for tk in tokens]}, ensure_ascii=False, indent=1),
        encoding="utf-8")
    log(f"[3] {len(tokens)} palavras alinhadas; {sum(tk['interpolado'] for tk in tokens)} interpoladas")

    # 4. legendas
    vid_tokens = [dict(tk, ini=tk["ini_video"], fim=tk["fim_video"]) for tk in no_video]
    ass_ref = out / "legenda_refroes.ass"
    ass_comp = out / "legenda_completa.ass"
    n_ref = gerar_ass(vid_tokens, letra, True, dur, ass_ref)
    n_comp = gerar_ass(vid_tokens, letra, False, dur, ass_comp)

    # 6. efeitos sonoros
    yaml_ep = ep / "efeitos.yaml"
    yaml_auto = out / "efeitos.yaml"
    import yaml
    if not yaml_ep.exists() and not yaml_auto.exists():
        modelo = {"_como_usar": "tempo em segundos no vídeo final; arquivo relativo à pasta do episódio "
                                "(ex.: efeitos/muu.wav); volume_db opcional. Itens sem arquivo são ignorados.",
                  "efeitos": ler_tabela_efeitos(ep)}
        yaml_auto.write_text(yaml.safe_dump(modelo, allow_unicode=True, sort_keys=False), encoding="utf-8")
    cfg = yaml.safe_load((yaml_ep if yaml_ep.exists() else yaml_auto).read_text(encoding="utf-8")) or {}
    efeitos, ignorados = [], []
    for e in cfg.get("efeitos", []):
        caminho = ep / e["arquivo"] if e.get("arquivo") else None
        if caminho and caminho.exists() and e["tempo"] < dur:
            efeitos.append(dict(e, caminho=caminho))
        else:
            ignorados.append(e)
    log(f"[6] Efeitos: {len(efeitos)} aplicados, {len(ignorados)} sem arquivo (ignorados)")

    # 5. render
    t = time.time()
    audio, lufs = preparar_audio(musica, corte, dur, efeitos, trab)
    render(base, audio, ass_ref, out / "final_refroes.mp4", out)
    render(base, audio, ass_comp, out / "final_completa.mp4", out)
    lista = trab / "preview.txt"
    lista.write_text("file '../final_completa.mp4'\n" * 3)
    run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lista), "-c", "copy",
         str(out / "preview_loop.mp4")])
    tempos["áudio + render"] = time.time() - t
    total = time.time() - t0
    log(f"[5] LUFS integrado: {lufs:.1f}; pronto em {total:.0f}s")

    # relatório
    baixa = [tk for tk in no_video if tk["conf"] < TEMPO_CONF_BAIXA]
    linhas_rel = [
        f"# Montagem automática: {ep.name}", "",
        f"Gerado por `scripts/montar.py` em {time.strftime('%Y-%m-%d %H:%M')}.", "",
        "## Entradas", "",
        f"- Vídeo: `{video.relative_to(ep) if video.is_relative_to(ep) else video}` "
        f"({larg}x{alt}, {loop['fps']:.2f} fps, {loop['quadros']} quadros, áudio do Veo descartado)",
        f"- Música: `{musica.relative_to(ep) if musica.is_relative_to(ep) else musica}` ({info['duracao']:.2f}s)",
        f"- Letra: {'seção 6 do episodio.md' if not aviso_letra else aviso_letra}", "",
        "## Loop", "",
        f"- Melhor par (SSIM): quadro **{loop['i']}** ({loop['i'] / loop['fps']:.3f}s) do início com o quadro "
        f"**{loop['j']}** ({loop['j'] / loop['fps']:.3f}s) do fim",
        f"- Nota de semelhança: **{loop['nota']:.3f}** (limiar {LIMIAR_LOOP})",
        f"- Vídeo usado: quadros {loop['i']} a {loop['j'] - 1}"
        + (f"; **crossfade de {CROSSFADE_S}s** do fim para os quadros que antecedem o início" if loop["crossfade"]
           else "; corte seco"),
        f"- Duração final: **{dur:.3f}s**", "",
        "## Música", "",
        f"- BPM detectado: **{info['bpm']:.1f}** (período {60 / info['bpm']:.3f}s)",
        f"- Voz entra em {info['inicio_voz']:.2f}s no arquivo original"
        + (f"; introdução cortada, música começa em {corte['inicio']:.3f}s (numa batida)" if corte["inicio"] > 0
           else "; sem introdução a cortar"),
        f"- Fim do trecho usado: {corte['fim']:.3f}s (batida); ajuste de andamento x{corte['fator']:.4f} "
        f"(atempo, sem mudar o tom) para caber em {dur:.3f}s" + (f" ({corte['obs']})" if corte["obs"] else ""),
        "- Fades: 20 ms na entrada e 30 ms na saída",
        f"- Loudness final: **{lufs:.1f} LUFS** (alvo -14, pico real -1 dBTP)", "",
        "## Letra alinhada", "",
        f"- Whisper `{args.whisper}` na voz separada pelo Demucs (htdemucs)",
        f"- {len(no_video)} palavras no vídeo; {sum(tk['interpolado'] for tk in no_video)} sem correspondência "
        f"(tempo interpolado)",
    ]
    if nao_cantadas:
        linhas_rel.append("- Versos não encontrados no áudio (sem legenda): "
                          + "; ".join(f"“{letra[i]['texto']}”" for i in nao_cantadas))
    if fora:
        linhas_rel.append("- Versos que ficaram fora do corte: " + "; ".join(f"“{letra[i]['texto']}”" for i in fora))
    linhas_rel += ["", f"Trechos com confiança baixa (< {TEMPO_CONF_BAIXA}):", ""]
    if baixa:
        linhas_rel += ["| Tempo no vídeo | Palavra da letra | Whisper ouviu | Confiança |", "|---|---|---|---|"]
        for tk in baixa:
            linhas_rel.append(f"| {tk['ini_video']:.2f}–{tk['fim_video']:.2f}s | {tk['texto']} | "
                              f"{tk['ouvido'] or '(nada, interpolado)'} | {tk['conf']:.2f} |")
    else:
        linhas_rel.append("- nenhum")
    linhas_rel += ["", "## Legendas", "",
                   f"- `legenda_refroes.ass`: {n_ref} falas (só refrões) → `final_refroes.mp4`",
                   f"- `legenda_completa.ass`: {n_comp} falas → `final_completa.mp4`",
                   f"- Fonte {FONTE_NOME}; palavra cantada {COR_ACESO}, a cantar {COR_APAGADO}, contorno {COR_CONTORNO}",
                   "", "## Efeitos sonoros", ""]
    if efeitos:
        linhas_rel += [f"- {e['tempo']:.2f}s: {e.get('efeito', '')} (`{e['arquivo']}`)" for e in efeitos]
    linhas_rel.append(f"- {len(ignorados)} efeito(s) sem arquivo, pulados. Lista em "
                      f"`{(yaml_ep if yaml_ep.exists() else yaml_auto).name}`.")
    linhas_rel += ["", "## Tempo de execução", "", "| Etapa | Segundos |", "|---|---|"]
    linhas_rel += [f"| {k} | {v:.1f} |" for k, v in tempos.items()]
    linhas_rel += [f"| **Total** | **{total:.1f}** |", ""]
    (out / "relatorio.md").write_text("\n".join(linhas_rel), encoding="utf-8")
    log(f"Relatório: {out / 'relatorio.md'}")


if __name__ == "__main__":
    main()
