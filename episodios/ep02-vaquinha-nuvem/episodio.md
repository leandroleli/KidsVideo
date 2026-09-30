# EP02: A Vaquinha Nuvem

Referência do personagem: [`../../personagem/bolinha_referencia.png`](../../personagem/bolinha_referencia.png) (use `bolinha_referencia_limpa.png` se já tiver gerado. Ver `personagem.md`)

---

## 1. Resumo

| Campo | Valor |
|---|---|
| Série | 🐮 Animais |
| Tema | O Chef Bolinha conhece a Vaquinha Nuvem na fazendinha |
| Por que Animais | Onomatopeias ("muu", "blim-blom") são o que crianças de 1 a 4 anos mais repetem, "musiquinha dos animais" é busca forte dos pais, e a fazenda afasta o canal da cozinha/sopa do tutorial |
| Duração-alvo | **20s** (geração 1 de ~10s + continuação até 20s) |
| Data de publicação | 2026-09-29 |
| Status | roteiro |

## 2. Ficha de variação

| Item | Este episódio | Ep01 (comparação) |
|---|---|---|
| Melodia | Sol maior; "Muu, muu, muu" em notas repetidas e resposta descendente | Sem melodia cantada (música de fundo do Veo) |
| Andamento | **96 BPM** (1 compasso = 2,5s; 20s = 8 compassos) | ~120 BPM |
| Instrumento principal | Ukulele + palmas + sininho | Ukulele + xilofone + palmas |
| Cenário | Fazendinha de manhã: celeiro com janela redonda, morro verde, girassóis | Cozinha pastel |
| Estrutura musical | Onomatopeia + chamada e resposta ("Cadê?" → "MUU!") | Falas soltas |
| Momento surpresa | O "MUU" gigante faz o chapéu do Bolinha voar e cair torto | Cenoura vira estrela; panela brilha |

> O ep01 também usou ukulele e palmas. Para diferenciar, aqui o xilofone sai, o sininho entra e o andamento cai de ~120 para 96 BPM.

## 3. Roteiro por cena

| Tempo | Geração | Cena (visual) | Áudio |
|---|---|---|---|
| 0:00–0:01 | 1 | **Gancho:** a Vaquinha Nuvem **surge de repente** na janela redonda do celeiro; o Bolinha, já no quadro, dá um pulinho de susto feliz com o chapéu balançando | Música tocando + efeito **"MUU!"** |
| 0:01–0:06 | 1 | Bolinha dança de um lado para o outro batendo as asinhas; Nuvem balança a cabeça na janela | **Refrão (1ª vez)** |
| 0:06–0:10 | 1 | Nuvem balança a cabeça e o sininho dourado balança junto; Bolinha imita | Estrofe, verso 1 |
| 0:10–0:11 | 2 | Nuvem enche o peito de ar | Estrofe, verso 2 |
| 0:11–0:13 | 2 | **Surpresa:** "MUU" gigante; o chapéu do Bolinha voa, gira e cai torto; ele dá risadinha | Efeito **"MUU!"** grande + "hi-hi!" |
| 0:13–0:18 | 2 | Bolinha ajeita o chapéu e os dois dançam | **Refrão (2ª vez)** |
| 0:18–0:20 | 2 | **Loop:** Nuvem se esconde no celeiro; Bolinha olha para a janela vazia, curioso, asinhas levantadas (**mesma pose do 1º frame**) | "Cadê?" sussurrado → emenda no "MUU!" do início |

## 4. Letra

**Refrão (2 versos, cantado 2x):**

```
Muu, muu, muu, a vaquinha diz,
Muu, muu, muu, e o Bolinha é feliz!
```

**Letra completa, por geração** (96 BPM, 1 compasso = 2,5s):

| Geração | Tempo | Trecho |
|---|---|---|
| 1 | 0,0–1,25s | *(efeito: MUU!)* |
| 1 | 1,25–3,75s | Muu, muu, muu, a vaquinha diz, |
| 1 | 3,75–6,25s | Muu, muu, muu, e o Bolinha é feliz! |
| 1 | 6,25–8,75s | Blim-blom, sininho, pra lá e pra cá, |
| 1 → 2 | 8,75–11,25s | um muu bem grandão faz o chapéu voar! |
| 2 | 11,25–12,5s | *(efeito: MUUU! + chapéu voando + "hi-hi!")* |
| 2 | 12,5–15,0s | Muu, muu, muu, a vaquinha diz, |
| 2 | 15,0–17,5s | Muu, muu, muu, e o Bolinha é feliz! |
| 2 | 17,5–20,0s | *(Nuvem se esconde)* … *(sussurrado)* Cadê? |

## 5. Geração no Gemini (Veo)

**Limite:** **2 gerações por dia**, de ~10s cada. A 2ª geração, feita a partir do último frame, devolve o **vídeo inteiro de 20s**, já emendado. Este episódio gasta exatamente as 2 gerações do dia, então **não sobra nenhuma para refazer**. Se algo sair errado, refaça no **Flow** (labs.google/flow) ou amanhã, e publique amanhã.

A imagem de abertura (5.1) é feita no modo de **imagem**, então não gasta o limite de vídeo.

### 5.1 Preparar o 1º frame (imagem)

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

### 5.2 Geração 1 (0–10s)

Gemini → **Vídeo** → anexe `imagens/frame_inicio.png` → cole o prompt → baixe como `videos/parte1.mp4`.

```
Vertical 9:16, high-quality 3D kids animation, soft lighting, vibrant pastel colors. Start exactly from the attached image; keep the character and setting identical.
Chef Bolinha: a tiny, round, fluffy baby chick with bright yellow fluffy feathers, big glossy turquoise-blue eyes with eyelashes, rosy pink cheeks, a small orange beak and tiny orange feet. He wears a tall, puffy white chef's hat with a small red star on the front band, a red neckerchief tied in a bow, and a light-blue apron with white polka dots and a front pocket.
Nuvem the cow: a small, cute, chubby baby cow with white fur covered in soft cloud-shaped light-gray spots, big friendly dark eyes, a pink nose, pink cheeks, tiny rounded horns, and a small golden bell on a blue ribbon around her neck.
Setting: a cute pastel farm on a sunny morning: a small red-and-cream wooden barn with a big round window, a soft green grassy hill, a white wooden fence, a few sunflowers, fluffy clouds, warm golden morning light.
Action: In the very first second, Nuvem suddenly pops her head out of the round barn window with a big happy moo, and Bolinha does a small surprised happy hop, his chef's hat bouncing. Then Bolinha giggles and dances side to side in rhythm, flapping his little wings and opening and closing his beak as if singing, while Nuvem sways her head in the window, smiling. In the last seconds, Nuvem swings her head left and right so her golden bell swings, and Bolinha happily copies the movement.
Camera: static medium shot, very slight slow push-in, no cuts.
Audio: cheerful ukulele music and hand claps, about 96 BPM, one short cow moo at the start, no dialogue.
```

Extraia o último frame (Git Bash ou PowerShell, dentro da pasta do episódio):

```
ffmpeg -sseof -0.1 -i videos/parte1.mp4 -frames:v 1 imagens/parte1_ultimo_frame.png
```

### 5.3 Geração 2 (continuação até 20s)

Gemini → **Vídeo** → anexe `imagens/parte1_ultimo_frame.png` → cole o prompt → baixe como `videos/completo_20s.mp4`.

O Gemini devolve os 20s já emendados, como aconteceu no ep01. Se vierem só os 10s novos, salve como `videos/parte2.mp4` e junte as duas partes na montagem.

```
Vertical 9:16, high-quality 3D kids animation, soft lighting, vibrant pastel colors. Start exactly from the attached image and continue the same scene; keep both characters, the setting, the lighting and the camera framing identical.
Chef Bolinha: a tiny, round, fluffy baby chick with bright yellow fluffy feathers, big glossy turquoise-blue eyes with eyelashes, rosy pink cheeks, a small orange beak and tiny orange feet. He wears a tall, puffy white chef's hat with a small red star on the front band, a red neckerchief tied in a bow, and a light-blue apron with white polka dots and a front pocket.
Nuvem the cow: a small, cute, chubby baby cow with white fur covered in soft cloud-shaped light-gray spots, big friendly dark eyes, a pink nose, pink cheeks, tiny rounded horns, and a small golden bell on a blue ribbon around her neck.
Setting: a cute pastel farm on a sunny morning: a small red-and-cream wooden barn with a big round window, a soft green grassy hill, a white wooden fence, a few sunflowers, fluffy clouds, warm golden morning light.
Action: Nuvem takes a big breath and lets out a huge happy moo; a playful gust of wind lifts Bolinha's white chef's hat off his head, it spins in the air and lands back on his head crooked. Bolinha blinks and giggles, then straightens his hat with both wings and dances happily side to side with Nuvem swaying in the window. In the last two seconds, Nuvem playfully ducks back inside the barn and disappears, leaving the round window open and empty. Bolinha turns and stands on the grass in the lower center of the frame in three-quarter view, looking up with a curious smile at the empty round window, both little wings slightly raised, and holds that pose until the end.
Camera: static medium shot, no cuts. Nothing scary.
Audio: the same cheerful ukulele music and hand claps, about 96 BPM, one big cow moo, a short giggle, no dialogue.
```

### 5.4 Continuidade

- As frases de **Setting** e as âncoras dos personagens são idênticas nos prompts de vídeo. Não edite uma sem editar a outra.
- A pose final da geração 2 precisa bater com `frame_inicio.png` (Bolinha embaixo no centro, de 3/4, olhando para a janela vazia no canto superior esquerdo).

### 5.5 Conferir antes de aprovar

- [ ] Bolinha igual à referência (chapéu com estrela, lenço vermelho, avental azul de bolinhas, olhos turquesa)
- [ ] Nuvem igual nas duas partes (manchas de nuvem cinza-claro, sino dourado com fita azul)
- [ ] Emenda em 10s sem salto (compare os frames 9,8s e 10,2s)
- [ ] Sem deformações (asas, olhos, bico, patas, focinho)
- [ ] Sem texto aleatório nem marca d'água
- [ ] Chapéu voando de um jeito engraçado, não assustador
- [ ] Final com a janela vazia e o Bolinha na pose inicial

## 6. Música

**Opção escolhida:** faixa única no **Suno** + efeitos no CapCut. O áudio do Veo é descartado.

Motivo: no ep01 o Veo fez bem a música de fundo e as falas, mas **cantar uma letra específica** em português, com a mesma melodia no começo e no fim, é bem mais arriscado. E como o limite é de 2 gerações por dia, não dá para refazer. O Suno canta a letra exata, e a voz vira Persona para os próximos episódios.

> **Plano B (teste futuro):** se o Suno não ficar bom, dá para pedir que o próprio Veo cante o refrão, colocando no prompt `singing in Brazilian Portuguese: "Muu, muu, muu, a vaquinha diz…"`. Vale testar num episódio sem pressa.

1. Suno → **Create** → **Custom**.
2. **Lyrics:** cole a letra abaixo.
3. **Style of Music:** cole o estilo abaixo.
4. **Exclude styles** (se disponível): `adult voice, rock, heavy drums, autotune, long intro`
5. **Title:** `A Vaquinha Nuvem`
6. Gere 2 ou 3 versões. Escolha a que canta "Muu, muu, muu" logo no começo, fica perto de 96 BPM e tem voz infantil clara.
7. Ouça pensando em músicas conhecidas (Seu Lobato/"ia-ia-ô", Galinha Pintadinha, "Borboletinha"). **Se lembrar alguma, gere de novo.**
8. Baixe → `videos/musica.mp3`.
9. Salve a voz como **Persona "Chef Bolinha"** (menu da música → Create Persona).
10. Uso comercial exige plano pago do Suno.

**Style of Music:**

```
children's nursery song, cheerful and playful, 96 BPM, G major, ukulele, hand claps, small bell, light shaker, cute high-pitched young child voice, sweet and clear, Brazilian Portuguese, no vibrato, very short intro
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

[Chorus]
Muu, muu, muu, a vaquinha diz
Muu, muu, muu, e o Bolinha é feliz

[Outro]
Cadê?

[End]
```

O Suno costuma gerar mais de 20s. Você vai cortar na montagem. Se ele não cantar o "Cadê?", grave com a sua voz e aplique o efeito de voz infantil do CapCut, ou use o texto-para-fala do CapCut com voz infantil.

**Efeitos sonoros (biblioteca do CapCut):**

| Tempo | Efeito | Busca no CapCut |
|---|---|---|
| 0,0s | Mugido curto e alegre | "vaca", "cow moo" |
| 6,25–8,75s | Sininho no ritmo (opcional) | "sino", "bell" |
| 11,25s | Mugido grande + "whoosh" | "cow moo", "whoosh" |
| 12,0s | Risadinha "hi-hi" | "giggle", "risada criança" |

## 7. Montagem (CapCut)

1. Novo projeto **9:16**, 1080×1920, 30 fps.
2. Importe `completo_20s.mp4` (ou `parte1` + `parte2` em sequência). **Silencie** o áudio original.
3. Importe `musica.mp3`:
   - Posicione o 1º "Muu, muu, muu" cantado em **1,25s**.
   - Se o Suno demorou mais entre a estrofe e o 2º refrão, corte o trecho sobrando para o 2º refrão começar em **12,5s**.
   - Corte a música em **20,0s**, logo depois do "Cadê?". **Sem fade-out.**
4. Acerte a sincronia visual:
   - Nuvem aparecendo = 0,0s, junto com o mugido.
   - Chapéu voando = cerca de 11s, junto com o mugido grande.
   - Nuvem sumindo = cerca de 18s.
   - Use velocidade de 95–105% em trechos do vídeo para ajustar.
5. Adicione os efeitos da tabela acima.
6. **Loop:** o último frame deve ser praticamente igual a `frame_inicio.png`. Corte seco no final, sem transição.
7. Legenda com a letra nos refrões (fonte arredondada, grande, contorno escuro), no terço superior.
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
- [ ] Vídeo final sem marca d'água
- [ ] Ferramentas usadas permitem uso comercial (Gemini/Veo e Suno pago)
- [ ] Título, descrição e playlist conforme este MD
- [ ] Verificar no Studio → Conteúdo → Restrições 24h após postar

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
