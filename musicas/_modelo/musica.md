# mXX: [Título da música]

| Campo | Valor |
|---|---|
| Status | roteiro / música pronta / gerando clipes (X de Y) / montada / publicada |
| Personagens | Chef Bolinha, … |
| Cenário | … |
| Duração da música | (preencher depois do Suno) |
| Clipes novos | Y (Z dias, 2 por dia) |

---

## 1. História

**Em uma frase:** …

| Ato | O que acontece |
|---|---|
| 1. Situação | … |
| 2. Problema | … (engraçado, nunca assustador) |
| 3. Tentativas | … |
| 4. Solução e festa | … |

**Participação da criança:** … (onde a criança responde, conta, imita ou bate palmas)

## 2. Ficha de variação

Compare com as 2 músicas anteriores. Se 3 ou mais linhas coincidirem, mude.

| Eixo | Esta música | m(XX-1) | m(XX-2) |
|---|---|---|---|
| Problema | | | |
| Cenário | | | |
| Luz / hora | | | |
| Ritmo e estilo | | | |
| BPM | | | |
| Participação | | | |
| Quem resolve | | | |

## 3. Música (Suno)

**Style:**

```
…
```

**Lyrics:**

```
[Intro]
…

[Verse 1]
…

[Chorus]
…
```

## 4. Mapa de clipes

Os tempos são estimados até a música ficar pronta. Depois, o `mapa.yaml` passa a ter os tempos reais.

| Trecho da música | Tempo | Clipe |
|---|---|---|
| Intro + Verso 1 | 0:00–0:20 | **c01** (novo) |
| Refrão 1 | … | **c03** (novo) |
| Refrão 2 | … | c03 (reaproveitado) |

### Plano de dias

| Dia | Clipes | Feito |
|---|---|---|
| 1 | c01, c02 | [ ] |
| 2 | c03, c04 | [ ] |

## 5. Prompts

### Bloco fixo

Cole este bloco **no começo de todo prompt de vídeo** desta música (Parte A e Parte B).

```
…
```

### c01: [nome]

**1º quadro (imagem, anexar: …):**

```
…
```

**Parte A (0–10s):**

```
Start exactly from the attached image. …
```

**Parte B (10–20s):**

```
Start exactly from the attached image and continue the same scene. …
```

## 6. Montagem

1. Clipes em `clipes/cXX.mp4`, música em `musica.wav`.
2. `python scripts/montar_musica.py musicas/mXX-<slug>`
3. Assistir `montagem/final.mp4` inteiro e ler `montagem/relatorio.md`.

## 7. Publicação

- **Título:** `[Título] [emoji] | Chef Bolinha | Música Infantil`
- **Descrição:**

  ```
  …
  ```

- **Tags:** música infantil, musica para crianças, desenho infantil, música para bebê, …
- **Thumbnail:** quadro de …

### Checklist

- [ ] "Sim, é conteúdo para crianças"
- [ ] Conteúdo alterado/sintético (IA) marcado
- [ ] Letra e melodia originais
- [ ] "Verificações" sem aviso de direitos autorais
- [ ] Vídeo inteiro assistido: nada deformado, nenhuma tela cinza
- [ ] Gemini/Veo e Suno pago (uso comercial)
- [ ] Título, descrição com letra e thumbnail
- [ ] Restrições conferidas 24h depois

## 8. Métricas

| Quando | Views | Tempo médio assistido | % assistida | Inscritos ganhos |
|---|---|---|---|---|
| 24h | | | | |
| 7 dias | | | | |

**Aprendizados:** …
