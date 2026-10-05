---
name: chef-bolinha-musicas
description: Cria músicas infantis completas de 2 a 4 minutos para o canal Chef Bolinha (vídeo horizontal 16:9), com o Chef Bolinha, a Vaquinha Nuvem e o Sementinha. Gera a historinha, a letra original, o prompt do Suno, o mapa de clipes de 20s (com refrões reaproveitados), o plano de 2 clipes por dia, os prompts de imagem e de vídeo e o mapa.yaml com os tempos reais da música. Use quando o usuário pedir uma música nova ("cria a m02"), ideias de músicas, mapear uma música do Suno ("mapeia a m01"), ajustar prompts de um clipe ou montar o vídeo.
---

# Chef Bolinha: compositor e roteirista de músicas

## 1. Missão

Criar músicas infantis **originais** de **2 a 4 minutos** que contam uma historinha com o Chef Bolinha e os amigos dele, para crianças de **1 a 4 anos**. O vídeo final é **horizontal 16:9** e é montado com clipes de 20s gerados no Gemini (Veo), **2 por dia**, cortados sobre a música do Suno.

Referência de formato: músicas-história do tipo "Vaca Lola" (https://www.youtube.com/watch?v=9mnn6WMilik). Use **só o formato** como inspiração, nunca personagens, nomes, letras ou melodias.

O fluxo completo está em `instrucao.md`. O modelo de arquivo fica em `musicas/_modelo/musica.md`.

## 2. Fontes de verdade dos personagens

- `personagem.md`: Chef Bolinha (aparência, prompt âncora, voz, bordão, o que nunca mudar).
- `personagem/amigos/vaquinha-nuvem.md` e `personagem/amigos/sementinha-morango.md`.
- Referências para anexar nas imagens: `personagem/bolinha_referencia.png` e `personagem/amigos/<slug>_referencia.png`. As `_ficha.png` são só para consulta: os círculos de detalhe podem aparecer no quadro gerado.

Leia os três antes de escrever. Não invente características que contradigam as bíblias. Um amigo novo só entra se o usuário pedir. Nesse caso, crie a bíblia dele em `personagem/amigos/<slug>.md` no mesmo formato, com nome que não coincida com personagem, marca ou produto conhecido.

## 3. Modos de uso

### A. Ideias de músicas

Proponha 3 a 5 ideias, cada uma com título, problema engraçado, cenário, quem resolve, ritmo e participação da criança. Varie conforme a seção 7.

### B. Criar música ("cria a m02")

1. Leia as fichas de variação das 2 últimas músicas em `musicas/` (**só** para não repetir).
2. Copie `musicas/_modelo/` para `musicas/mXX-<slug>/` e preencha todas as seções (seção 6 desta skill).
3. Crie as pastas `clipes/` e `imagens/` com `.gitkeep`.
4. Mostre ao usuário um resumo (história, refrão, número de clipes, dias) e espere a aprovação antes de commitar.

### C. Mapear a música ("mapeia a m01")

Depois que o usuário salvar `musicas/mXX-<slug>/musica.wav` (ou `.mp3`):

1. Separe a voz (Demucs `htdemucs`) e transcreva com faster-whisper (`medium`, `language="pt"`, `word_timestamps=True`, `initial_prompt` = a letra), para achar o início de cada verso e de cada seção.
2. Confira se a letra cantada bate com a seção 3. Se o Suno mudou alguma coisa, mostre a diferença e pergunte antes de seguir.
3. Divida a música em trechos que respeitem as seções. Cada trecho tem **no máximo 20s** e cada corte cai **no início de um verso**. Se uma seção passar de 20s, divida entre dois clipes ou reaproveite a 2ª metade de outro clipe (`desde`).
4. Escreva `musicas/mXX-<slug>/mapa.yaml` no formato descrito em `scripts/montar_musica.py` e atualize a tabela da seção 4 e o plano de dias do `musica.md` com os tempos reais.
5. Se a música real pedir mais clipes do que o planejado, proponha onde reaproveitar antes de criar clipes novos.

### D. Ajustar um clipe

Quando um clipe sair errado (personagem deformado, ação trocada), reescreva só o prompt daquele clipe, aplicando as regras da seção 5, e explique o que mudou.

### E. Montar

Rode `python scripts/montar_musica.py musicas/mXX-<slug>`, leia `montagem/relatorio.md` e diga o que falta e o que tem aviso.

## 4. Música e letra

**Estrutura** (ajuste à história, mantendo a ordem):

`[Intro]` curta (até 2 compassos) → `[Verse 1]` situação → `[Pre-Chorus]` o problema → `[Chorus]` → `[Verse 2]` tentativa → `[Pre-Chorus]` → `[Chorus]` → `[Bridge]` participação → `[Verse 3]` virada → `[Verse 4]` solução → `[Final Chorus]` (letra mudada: problema resolvido) → `[Outro]` curto.

**Regras:**
- 2 a 4 minutos. Mire em ~3 min (100 a 120 BPM, 4 versos por estrofe).
- Refrão de 4 versos, fácil de cantar, repetido pelo menos 2 vezes com a mesma letra. Ele é reaproveitado no vídeo, então descreve uma **ação que se repete** (correr, procurar, dançar), e não um acontecimento único.
- Frases curtas, palavras de criança de 1 a 4 anos, rima simples, onomatopeias ("vuuu", "boing", "Muu", "plim").
- **Ponte de participação:** pergunta e resposta com coro infantil entre parênteses (o Suno canta como backing vocal), contagem, "cadê?" ou imitação de som.
- O nome dos personagens aparece na letra; a criança precisa aprender quem é quem.
- Bordão "Pi-piu, que delícia!" com moderação (no máximo 1 vez por música, e não em todas).
- **Style do Suno** em inglês, com: gênero infantil + instrumentos + BPM + tonalidade maior + `cute high-pitched young child voice, sweet and clear, Brazilian Portuguese, no vibrato` + `short intro`. Usar a Persona "Chef Bolinha".

**Originalidade:** letra e melodia 100% originais. Nada parecido com: Pintinho Amarelinho (nunca use essa expressão), Seu Lobato, Cinco Patinhos, Galinha Pintadinha, Borboletinha, Baby Shark, Parabéns pra Você, Sapo Não Lava o Pé, Sapo Cururu, Atirei o Pau no Gato, A Dona Aranha, Brilha Brilha Estrelinha, Ciranda Cirandinha, Eguinha Pocotó, A Vaca Lola, Boi da Cara Preta. Nada de nomes de personagens, canais ou marcas existentes.

**Segurança e tom:** o problema é leve e engraçado. Nada de medo, perigo real, choro longo, punição, fogo, facas, quedas perigosas ou personagem em risco. Ninguém come o Sementinha.

## 5. Clipes e prompts

**Mapa de clipes:**
- Cada clipe tem **20s** = Parte A (0–10s) + Parte B (10–20s, continuação a partir do último quadro da A).
- **Reaproveite:** refrões repetidos usam o mesmo clipe ou metades de clipes (`desde`); um clipe pode ser espelhado (`espelhar`) quando a direção não importa. Meta: uma música de 3 min com **7 a 9 clipes novos**.
- Pré-refrões curtos e o outro reaproveitam metades de clipes vizinhos sempre que der.
- Marque como **opcional** um clipe que só dá variedade (ex.: 2º clipe de refrão) e diga o que entra no lugar dele se não for feito.
- **Plano de dias:** 2 clipes por dia, na ordem da música, com o opcional por último.

**Prompts (inglês):**
- **Bloco fixo** por música: estilo (horizontal 16:9, 3D Pixar-like, pastel, luz), câmera, `No talking, no singing, no text on screen`, cenário em uma frase, tamanhos relativos e o prompt âncora **integral** de cada personagem que aparece (sem a frase final de estilo, que já está no topo). O usuário cola o bloco no começo de todo prompt de vídeo.
- **1º quadro de cada clipe** (imagem, Gemini): `Horizontal 16:9 image` + `Keep the characters exactly like the attached reference images` + cena com posição de cada um + `No text, no logos, no watermark.` Diga quais referências anexar.
- **Parte A:** começa com `Start exactly from the attached image.` **Parte B:** começa com `Start exactly from the attached image and continue the same scene.`
- Cada clipe parte do próprio 1º quadro. Clipes **não** precisam emendar entre si.

**O que funcionou nos testes (01/10/2026):**
- Identidade **positiva**, sem negações. Exceção útil: estados da história ("Chef Bolinha has no hat on his head") vão no começo da Parte A e da Parte B.
- Cada ação diz **quem** faz e **de que lado** ("Sementinha the red strawberry, on the right, jumps").
- Posições fixas na música inteira (padrão: **Nuvem à esquerda, Bolinha no meio, Sementinha à direita**).
- **Câmera parada** ou acompanhamento lateral lento. Plano aberto, todos inteiros no quadro.
- Ações **grandes**: correr, pular, girar, apontar, abraçar, dançar. Nada de efeito em detalhe pequeno (sementes, dedos, texto) nem objetos minúsculos.
- No máximo 3 personagens por clipe, 1 ou 2 ações por parte de 10s.
- Sem fala nem canto com a boca: a música vem do Suno e a boca não bateria com ela.

## 6. Saída: `musicas/mXX-<slug>/musica.md`

Siga as seções do `_modelo`:

1. **Cabeçalho:** status, personagens, cenário, duração, clipes novos e dias.
2. **História:** uma frase + tabela dos 4 atos + participação da criança.
3. **Ficha de variação:** comparada com as 2 músicas anteriores.
4. **Música (Suno):** Style e Lyrics com tags.
5. **Mapa de clipes:** tabela trecho → tempo → clipe (novo/reaproveitado/opcional) + plano de dias.
6. **Prompts:** bloco fixo + para cada clipe novo: 1º quadro, Parte A e Parte B.
7. **Montagem**, **Publicação** (título `[Título] [emoji] | Chef Bolinha | Música Infantil`, descrição com a letra, tags, thumbnail, checklist) e **Métricas**.

## 7. Variação entre músicas

Os personagens são fixos. Todo o resto varia: problema, cenário, luz/hora, ritmo e estilo (pop, forró/baião, marchinha, xote, reggae infantil, valsinha, rock de brinquedo), BPM (80 a 130, sem repetir em seguidas), participação e quem resolve o problema (alternar entre Bolinha, Nuvem e Sementinha). Se 3 ou mais eixos coincidirem com uma das 2 músicas anteriores, mude.

## 8. Controle de qualidade (antes de entregar)

- [ ] História com 4 atos claros e problema leve
- [ ] Refrão repetido com a mesma letra e descrevendo uma ação reaproveitável
- [ ] Ponte com participação da criança
- [ ] Letra original, sem expressões proibidas
- [ ] Duração estimada entre 2 e 4 min
- [ ] Cada clipe tem no máximo 20s de música; refrões reaproveitam
- [ ] Prompts com bloco fixo, lados definidos, câmera parada e sem fala
- [ ] Ficha de variação preenchida

## 9. Estilo de resposta

PT-BR, direto, com Markdown. Mostre resumos no chat e deixe o conteúdo completo no `musica.md`. Peça aprovação antes de editar MDs existentes e faça commits pequenos, um por etapa.
