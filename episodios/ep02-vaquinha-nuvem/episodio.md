# EP02: A Vaquinha Nuvem

Referência do personagem: [`../../personagem/bolinha_referencia.png`](../../personagem/bolinha_referencia.png) (use `bolinha_referencia_limpa.png` se já tiver gerado. Ver `personagem.md`)

---

## 1. Resumo

| Campo | Valor |
|---|---|
| Série | 🐮 Animais |
| Tema | O Chef Bolinha conhece a Vaquinha Nuvem na fazendinha |
| Por que Animais | Onomatopeias ("muu", "blim-blom") são o que crianças de 1 a 4 anos mais repetem, "musiquinha dos animais" é busca forte dos pais, e a fazenda afasta o canal da cozinha/sopa do tutorial |
| Duração-alvo | 24s (3 clipes de 8s) |
| Data de publicação | 2026-09-29 |
| Status | roteiro |

## 2. Ficha de variação

| Item | Este episódio | Ep01 (comparação) |
|---|---|---|
| Melodia | Sol maior; "Muu, muu, muu" em notas repetidas e resposta descendente | Sem melodia cantada (jingle de fundo) |
| Andamento | **90 BPM** (3 compassos = 8s exatos, 1 clipe) | — |
| Instrumento principal | Ukulele + xilofone + palmas | Jingle |
| Cenário | Fazendinha de manhã: celeiro com janela redonda, morro verde, girassóis | Cozinha pastel |
| Estrutura musical | Onomatopeia + chamada e resposta ("Cadê?" → "MUU!") | Falas soltas |
| Momento surpresa | O "MUU" gigante faz o chapéu do Bolinha voar e cair torto | Panela brilha (mágica) |

## 3. Roteiro por cena

90 BPM → 1 compasso = 2,67s → cada clipe de 8s = 3 compassos.

| Tempo | Clipe | Cena (visual) | Áudio |
|---|---|---|---|
| 0:00–0:01 | 1 | **Gancho:** a Vaquinha Nuvem **surge de repente** na janela redonda do celeiro; o Bolinha dá um pulinho de susto feliz, com o chapéu balançando | Música já tocando + efeito **"MUU!"** |
| 0:01–0:03 | 1 | Bolinha ri e começa a dançar | Instrumental (fim do 1º compasso) |
| 0:03–0:08 | 1 | Bolinha dança de um lado para o outro batendo as asinhas; Nuvem balança a cabeça na janela | **Refrão (1ª vez)** |
| 0:08–0:13 | 2 | Nuvem balança a cabeça e o sininho dourado balança junto; Bolinha imita o movimento | Estrofe |
| 0:13–0:16 | 2 | **Surpresa:** Nuvem solta um "MUU" gigante; o vento faz o chapéu do Bolinha voar, girar e cair torto na cabeça dele; ele dá risadinha | Efeito **"MUU!"** grande + "hi-hi!" |
| 0:16–0:21 | 3 | Bolinha ajeita o chapéu e os dois dançam juntos | **Refrão (2ª vez)** |
| 0:21–0:24 | 3 | **Loop:** Nuvem se esconde dentro do celeiro; Bolinha fica olhando para a janela vazia, curioso, asinhas levantadas (**mesma pose do 1º frame**) | "Cadê?" sussurrado → emenda no "MUU!" do início |

## 4. Letra

**Refrão (2 versos, cantado 2x):**

```
Muu, muu, muu, a vaquinha diz,
Muu, muu, muu, e o Bolinha é feliz!
```

**Letra completa, por clipe:**

| Clipe | Tempo | Trecho |
|---|---|---|
| 1 | 0,0–2,7s | *(efeito: MUU!)* instrumental |
| 1 | 2,7–5,3s | Muu, muu, muu, a vaquinha diz, |
| 1 | 5,3–8,0s | Muu, muu, muu, e o Bolinha é feliz! |
| 2 | 8,0–10,7s | Blim-blom, sininho, pra lá e pra cá, |
| 2 | 10,7–13,3s | um muu bem grandão faz o chapéu voar! |
| 2 | 13,3–16,0s | *(efeito: MUUU! + chapéu voando + "hi-hi!")* |
| 3 | 16,0–18,7s | Muu, muu, muu, a vaquinha diz, |
| 3 | 18,7–21,3s | Muu, muu, muu, e o Bolinha é feliz! |
| 3 | 21,3–24,0s | *(sussurrado)* Cadê? |

## 5. Geração no Gemini (Veo)

**Limite atual:** clipes de **até 8s**. No AI Pro são **cerca de 3 gerações de vídeo por dia**, o número exato de clipes deste episódio. **Não gaste gerações testando.** Se um clipe sair ruim, refaça no **Flow** (labs.google/flow) ou no dia seguinte (e publique no dia seguinte).

### 5.1 Preparar o 1º frame

1. Gemini → criação de imagem → anexe a referência do personagem.
2. Cole:

```
Use the attached image as the exact character reference. Vertical 9:16 image.
Chef Bolinha: a tiny, round, fluffy baby chick with bright yellow fluffy feathers, big glossy turquoise-blue eyes with eyelashes, rosy pink cheeks, a small orange beak and tiny orange feet. He wears a tall, puffy white chef's hat with a small red star on the front band, a red neckerchief tied in a bow, and a light-blue apron with white polka dots and a front pocket. Cute 3D animated style, soft Pixar-like rendering, pastel colors, warm soft lighting.
Setting: a cute pastel farm on a sunny morning: a small red-and-cream wooden barn with a big round window, a soft green grassy hill, a white wooden fence, a few sunflowers, fluffy clouds in a light-blue sky, warm golden morning light.
Composition: Bolinha stands on the grass in the lower center of the frame, three-quarter view, looking up with a curious smile at the round barn window in the upper left, both little wings slightly raised. The round window is open and empty, nobody inside.
No text, no logos, no watermark.
```

3. Confira o personagem, o formato vertical e a janela **vazia**. Salve como `imagens/frame_inicio.png`. Esse frame também é o **alvo do loop**.

### 5.2 Gerar os clipes

Para cada clipe:
1. Gemini → **Vídeo**.
2. Anexe a imagem indicada.
3. Escolha 9:16 se o seletor aparecer.
4. Cole o prompt.
5. Baixe e salve em `videos/`.

Depois de cada clipe, extraia o último frame (Git Bash ou PowerShell, dentro da pasta do episódio):

```
ffmpeg -sseof -0.1 -i videos/clipe1.mp4 -frames:v 1 imagens/clipe1_ultimo_frame.png
```

**Clipe 1 (0–8s)**, imagem inicial: `imagens/frame_inicio.png` → salvar `videos/clipe1.mp4`

```
Animate the attached image. Keep the exact same character, setting and lighting.
Chef Bolinha: a tiny, round, fluffy baby chick with bright yellow fluffy feathers, big glossy turquoise-blue eyes with eyelashes, rosy pink cheeks, a small orange beak and tiny orange feet. He wears a tall, puffy white chef's hat with a small red star on the front band, a red neckerchief tied in a bow, and a light-blue apron with white polka dots and a front pocket.
Nuvem the cow: a small, cute, chubby baby cow with white fur covered in soft cloud-shaped light-gray spots, big friendly dark eyes, a pink nose, pink cheeks, tiny rounded horns, and a small golden bell on a blue ribbon around her neck.
Setting: a cute pastel farm on a sunny morning: a small red-and-cream wooden barn with a big round window, a soft green grassy hill, a white wooden fence, a few sunflowers, fluffy clouds, warm golden morning light.
Action: In the very first second, Nuvem suddenly pops her head out of the round barn window with a big happy open-mouth moo expression, and Bolinha does a small surprised happy hop, his chef's hat bouncing. Then Bolinha giggles and dances side to side in rhythm, flapping his little wings and opening and closing his beak as if singing happily, while Nuvem sways her head in the window and smiles.
Camera: static vertical 9:16 medium shot, very slight slow push-in, no cuts.
Style: cute 3D animation, soft Pixar-like rendering, pastel colors.
Audio: no dialogue, no singing, no music, only soft ambient farm sounds.
```

**Clipe 2 (8–16s)**, imagem inicial: `imagens/clipe1_ultimo_frame.png` → salvar `videos/clipe2.mp4`

```
Animate the attached image as a direct continuation. Keep the exact same characters, setting, lighting and camera framing.
Chef Bolinha: a tiny, round, fluffy baby chick with bright yellow fluffy feathers, big glossy turquoise-blue eyes with eyelashes, rosy pink cheeks, a small orange beak and tiny orange feet. He wears a tall, puffy white chef's hat with a small red star on the front band, a red neckerchief tied in a bow, and a light-blue apron with white polka dots and a front pocket.
Nuvem the cow: a small, cute, chubby baby cow with white fur covered in soft cloud-shaped light-gray spots, big friendly dark eyes, a pink nose, pink cheeks, tiny rounded horns, and a small golden bell on a blue ribbon around her neck.
Setting: a cute pastel farm on a sunny morning: a small red-and-cream wooden barn with a big round window, a soft green grassy hill, a white wooden fence, a few sunflowers, fluffy clouds, warm golden morning light.
Action: For the first five seconds, Nuvem gently swings her head left and right in the barn window so her golden bell swings, and Bolinha happily copies the movement, swaying left and right. Then Nuvem takes a big breath and lets out a huge happy moo; a playful gust of wind lifts Bolinha's white chef's hat off his head, it spins in the air and lands back on his head crooked. Bolinha blinks, then giggles with his wings over his beak.
Camera: static vertical 9:16 medium shot, no cuts.
Style: cute 3D animation, soft Pixar-like rendering, pastel colors. Nothing scary.
Audio: no dialogue, no singing, no music, only soft ambient farm sounds.
```

**Clipe 3 (16–24s)**, imagem inicial: `imagens/clipe2_ultimo_frame.png` → salvar `videos/clipe3.mp4`

```
Animate the attached image as a direct continuation. Keep the exact same characters, setting, lighting and camera framing.
Chef Bolinha: a tiny, round, fluffy baby chick with bright yellow fluffy feathers, big glossy turquoise-blue eyes with eyelashes, rosy pink cheeks, a small orange beak and tiny orange feet. He wears a tall, puffy white chef's hat with a small red star on the front band, a red neckerchief tied in a bow, and a light-blue apron with white polka dots and a front pocket.
Nuvem the cow: a small, cute, chubby baby cow with white fur covered in soft cloud-shaped light-gray spots, big friendly dark eyes, a pink nose, pink cheeks, tiny rounded horns, and a small golden bell on a blue ribbon around her neck.
Setting: a cute pastel farm on a sunny morning: a small red-and-cream wooden barn with a big round window, a soft green grassy hill, a white wooden fence, a few sunflowers, fluffy clouds, warm golden morning light.
Action: Bolinha quickly straightens his chef's hat with both wings, then dances happily side to side, opening and closing his beak as if singing, while Nuvem sways her head in the window. In the last three seconds, Nuvem playfully ducks back inside the barn and disappears, leaving the round window open and empty. Bolinha stops, turns and stands on the grass in the lower center of the frame in three-quarter view, looking up with a curious smile at the empty round window, both little wings slightly raised, and holds that pose still until the end.
Camera: static vertical 9:16 medium shot, no cuts.
Style: cute 3D animation, soft Pixar-like rendering, pastel colors.
Audio: no dialogue, no singing, no music, only soft ambient farm sounds.
```

### 5.3 Continuidade

- A frase de **Setting** e as âncoras dos personagens são idênticas nos 3 prompts. Não edite uma sem editar as outras.
- Cada clipe começa no último frame do anterior (comando `ffmpeg` acima).
- Se a Nuvem mudar de aparência no clipe 2 ou 3 (manchas, sino, chifres), refaça só esse clipe.
- A pose final do clipe 3 precisa bater com `frame_inicio.png` (Bolinha embaixo no centro, de 3/4, olhando para a janela vazia no canto superior esquerdo).

### 5.4 Conferir antes de aprovar cada clipe

- [ ] Bolinha igual à referência (chapéu com estrela, lenço vermelho, avental azul de bolinhas, olhos turquesa)
- [ ] Nuvem igual entre os clipes (manchas de nuvem cinza-claro, sino dourado com fita azul)
- [ ] Sem deformações (asas, olhos, bico, patas, focinho)
- [ ] Sem texto aleatório
- [ ] Sem marca d'água de terceiros
- [ ] Chapéu voando de um jeito engraçado, não assustador (clipe 2)
- [ ] Clipe 3 termina com a janela vazia e o Bolinha na pose inicial

## 6. Música

**Opção escolhida:** faixa única no **Suno** + efeitos no CapCut. O áudio do Veo é descartado.

Motivo: gerando clipe por clipe, o Veo muda a voz e a melodia entre os 3 clipes. Com o Suno, a voz e a melodia são uma só, e a voz pode virar Persona para os próximos episódios.

1. Suno → **Create** → **Custom**.
2. **Lyrics:** cole a letra abaixo.
3. **Style of Music:** cole o estilo abaixo.
4. **Exclude styles** (se disponível): `adult voice, rock, heavy drums, autotune, long intro`
5. **Title:** `A Vaquinha Nuvem`
6. Gere 2 ou 3 versões. Escolha a que:
   - canta "Muu, muu, muu" logo no começo (intro curta);
   - mantém o andamento próximo de 90 BPM;
   - tem voz infantil clara.
7. Ouça pensando em músicas conhecidas (Seu Lobato/"ia-ia-ô", Galinha Pintadinha, "Borboletinha"). **Se lembrar alguma, gere de novo.**
8. Baixe → `videos/musica.mp3`.
9. Salve a voz como **Persona "Chef Bolinha"** (menu da música → Create Persona).
10. Uso comercial exige plano pago do Suno.

**Style of Music:**

```
children's nursery song, cheerful and playful, 90 BPM, G major, ukulele, xylophone, hand claps, light shaker, cute high-pitched young child voice, sweet and clear, Brazilian Portuguese, no vibrato, very short intro
```

**Lyrics:**

```
[Intro]

[Chorus]
Muu, muu, muu, a vaquinha diz
Muu, muu, muu, e o Bolinha é feliz

[Verse]
Blim-blom, sininho, pra lá e pra cá
Um muu bem grandão faz o chapéu voar

[Instrumental Break]

[Chorus]
Muu, muu, muu, a vaquinha diz
Muu, muu, muu, e o Bolinha é feliz

[Outro]
Cadê?

[End]
```

O Suno costuma gerar mais de 24s. Você vai cortar na montagem. Se ele não cantar o "Cadê?" sussurrado, grave com a sua voz e aplique o efeito de voz infantil do CapCut, ou use o texto-para-fala do CapCut com voz infantil.

**Efeitos sonoros (biblioteca do CapCut):**

| Tempo | Efeito | Busca no CapCut |
|---|---|---|
| 0,0s | Mugido curto e alegre | "vaca", "cow moo" |
| 8,0–13,3s | Sininho leve no ritmo (opcional) | "sino", "bell" |
| 13,3s | Mugido grande + "whoosh" do vento | "cow moo", "whoosh" |
| 14,0s | Risadinha "hi-hi" | "giggle", "risada criança" |

## 7. Montagem (CapCut)

1. Novo projeto **9:16**, 1080×1920, 30 fps.
2. Linha do tempo: `clipe1` → `clipe2` → `clipe3`. **Silencie** os 3.
3. Importe `musica.mp3`:
   - Ache onde começa o 1º "Muu, muu, muu" cantado e posicione esse ponto em **2,7s**. O que sobrar de intro antes disso fica entre 0 e 2,7s. Se a intro for maior, corte o começo.
   - Encaixe o 2º refrão em **16,0s**. Se o Suno fez a estrofe mais longa, corte o intervalo instrumental.
   - Corte a música em **24,0s**, logo depois do "Cadê?". **Sem fade-out.**
4. Acerte a sincronia visual:
   - Nuvem aparecendo = 0,0s, junto com o mugido.
   - Chapéu voando = 13,3s, junto com o mugido grande.
   - Nuvem sumindo = cerca de 21s.
   - Use velocidade de 95–105% nos clipes para ajustar.
5. Adicione os efeitos da tabela acima.
6. **Loop:** o último frame deve ser praticamente igual ao `frame_inicio.png`. Corte seco no final, sem transição.
7. Legenda com a letra nos refrões (fonte arredondada, grande, contorno escuro), centralizada no terço superior para não cobrir o personagem.
8. Exporte em 1080p, 30 fps → `videos/final.mp4`.
9. Assista 3 vezes em loop no celular. A emenda "Cadê?" → "MUU!" tem de soar natural.

## 8. Publicação (YouTube Studio)

| Campo | Valor |
|---|---|
| Título | `Vaquinha Nuvem do Chef Bolinha 🐮✨ \| Musiquinha Infantil` |
| Descrição | (abaixo) |
| Playlist | **Fazendinha do Chef Bolinha 🐮 (Animais)**: criar agora |
| Público | **Sim, é conteúdo para crianças** |
| Restrição de idade | Não |
| Promoção paga | Não |
| Conteúdo alterado ou sintético | **Sim** |
| Tags | (abaixo) |
| Idioma do vídeo | Português (Brasil) |
| Idioma do título e descrição | Português (Brasil) |
| Certificação de legendas | Este conteúdo nunca foi exibido na TV dos EUA |
| Licença | Licença padrão do YouTube |
| Permitir incorporação | Sim |
| Publicar no feed de inscrições | Sim |
| Categoria | Educação |
| Comentários | Desativados automaticamente (conteúdo para crianças), é o esperado |

**Descrição (copiar):**

```
Muu, muu, muu! 🐮 O Chef Bolinha encontra a Vaquinha Nuvem na fazendinha, e um muu bem grandão faz o chapéu voar! 🎩💨
Musiquinha infantil para cantar junto e aprender o som dos animais. Novo episódio todo dia! 🐥

#musicainfantil #shorts #chefbolinha
```

**Tags (copiar):**

```
musiquinha infantil, música para bebê, música para crianças, música infantil, chef bolinha, vaquinha, música da vaquinha, som dos animais, animais da fazenda, musiquinha dos animais, vaca faz muu
```

## 9. Checklist de publicação

- [ ] "Sim, é conteúdo para crianças" (nunca mudar para recuperar comentários)
- [ ] Divulgação de conteúdo alterado/sintético (IA) marcada
- [ ] Letra e melodia originais, sem semelhança com músicas conhecidas
- [ ] Etapa "Verificações" do upload sem aviso de direitos autorais
- [ ] Vídeo final sem marca d'água de terceiros (ver nota)
- [ ] Ferramentas usadas permitem uso comercial (Gemini/Veo e Suno pago)
- [ ] Título, descrição e playlist conforme este MD
- [ ] Verificar no Studio → Conteúdo → Restrições 24h após postar

> **Nota sobre o selo "Veo":** os vídeos do Gemini saem com um selo visível "Veo", que é a identificação de IA do Google. Não cubra nem remova o selo. A regra "sem marca d'água" vale para marcas de terceiros (Dreamina, capafy).

## 10. Pós-publicação

| Métrica | 24h (30/09) | 7 dias (06/10) |
|---|---|---|
| Visualizações | | |
| Duração média da visualização | | |
| % média visualizada | | |
| Deslizaram vs. assistiram (Shorts) | | |
| Inscritos ganhos | | |
| Restrições (Studio) | | — |

Aprendizados:

-
