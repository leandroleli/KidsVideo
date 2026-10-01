# EPxx: [Título do episódio]

> Copie esta pasta (`_modelo/`) para `episodios/epXX-<slug>/`, crie `videos/` e `imagens/` dentro dela e preencha todos os campos.
> Este arquivo é autossuficiente: com ele você gera e publica o vídeo sem abrir outro.

Referência do personagem: [`../../personagem/bolinha_referencia.png`](../../personagem/bolinha_referencia.png)

---

## 1. Resumo

| Campo | Valor |
|---|---|
| Tipo | Apresentação (musiquinha) / Educativo (falas e interação) |
| Amigo | [nome] (novo / apresentado no epXX) |
| Área de aprendizagem | (lista da seção 5 da skill) |
| Objetivo | A criança consegue… (uma coisa observável, que cabe em 20s) |
| Idade | 1–2 anos / 2–4 anos |
| Por que funciona para essa idade | |
| Tema | |
| Duração-alvo | 20s (geração 1 de ~10s + continuação até 20s) |
| Data de publicação | AAAA-MM-DD |
| Status | roteiro / gerando / publicado |

## 2. Ficha de variação

Compare com os últimos 3 episódios (os 2 anteriores ficam nas colunas). Se 3 ou mais itens coincidirem, mude. O loop nunca repete o do episódio anterior.

| Item | Este episódio | EpN-1 | EpN-2 |
|---|---|---|---|
| Tipo | | | |
| Amigo | | | |
| Área | | | |
| Objetivo | | | |
| Cenário | | | |
| Iluminação | | | |
| Estrutura (musical ou de falas) | | | |
| Instrumento principal | | | |
| Andamento (BPM) | | | |
| Tonalidade | | | |
| Momento surpresa | | | |
| Final / loop | | | |

## 3. Roteiro por cena

| Tempo | Geração | Cena (visual) | Áudio |
|---|---|---|---|
| 0:00–0:01 | 1 | **Gancho:** personagem **já visível** e em ação + som forte (não comece com objeto, explosão ou cenário vazio) | |
| 0:01–0:06 | 1 | | Refrão (1ª vez) |
| 0:06–0:12 | 1 → 2 | Estrofe + momento surpresa | Estrofe |
| 0:12–0:18 | 2 | | Refrão (2ª vez) |
| 0:18–0:20 | 2 | **Loop:** termina na mesma pose/cena do 1º frame | |

## 4. Letra

**Refrão** (2 a 4 versos, repetido ≥ 2x):

```
```

**Letra completa, por geração:**

| Geração | Tempo | Trecho |
|---|---|---|
| 1 | 0–10s | |
| 2 | 10–20s | |

Dica: escolha um BPM em que 10s feche em compassos inteiros (96 BPM → 1 compasso = 2,5s; 120 BPM → 2s).

Regras: frases curtas, palavras simples (1 a 4 anos), rima fácil, onomatopeia ou contagem, nada parecido com músicas infantis conhecidas.

## 5. Geração no Gemini (Veo)

**Limite:** **2 gerações de vídeo por dia**, de ~10s cada. A 2ª geração, feita a partir do último frame da 1ª, devolve o **vídeo inteiro de 20s** já emendado (foi assim no ep01). Um episódio gasta as 2 gerações do dia, então **não sobra nenhuma para refazer**. Se algo sair errado, refaça no **Flow** (labs.google/flow) ou no dia seguinte.

A imagem do 1º frame (5.1) é feita no modo de **imagem** e não gasta o limite de vídeo.

### 5.1 Preparar o 1º frame (imagem)

1. No Gemini (criação de imagem), anexe a referência do personagem e peça a cena de abertura **em 9:16**, com o personagem **já visível** na pose inicial:

   ```
   [prompt da imagem do 1º frame: cenário + pose inicial + âncora do personagem]
   ```

2. Salve como `imagens/frame_inicio.png`. Esse frame também é o **alvo do loop**: a geração 2 precisa terminar igual a ele.

### 5.2 Geração 1 (0–10s)

1. Gemini → **Vídeo** → anexe `imagens/frame_inicio.png`.
2. Cole o prompt. Ele começa com `Start exactly from the attached image`: sem essa frase, o Gemini usa a imagem só como referência e inventa outra abertura.
3. Baixe → `videos/parte1.mp4`.
4. Extraia o último frame:

   ```
   ffmpeg -sseof -0.1 -i videos/parte1.mp4 -frames:v 1 imagens/parte1_ultimo_frame.png
   ```

```
[prompt: Vertical 9:16, high-quality 3D kids animation... Start exactly from the attached image... âncora do personagem + Setting + Action + Camera + Audio]
```

### 5.3 Geração 2 (continuação até 20s)

1. Gemini → **Vídeo** → anexe `imagens/parte1_ultimo_frame.png`.
2. Cole o prompt (`Start exactly from the attached image and continue the same scene...`).
3. Baixe → `videos/completo_20s.mp4`. Se vierem só os 10s novos, salve como `videos/parte2.mp4` e junte na montagem.

```
[prompt]
```

### 5.4 Continuidade

- Mesmo cenário, mesma hora do dia e mesma luz nos dois prompts (copie a frase de **Setting** igual).
- Câmera sem cortes. Movimentos suaves.
- A **1ª frase da Action** descreve o personagem já em cena. Nada de "sparkles explode and Bolinha pops out": foi isso que deixou o ep01 sem o personagem no 1º segundo.
- O áudio do Veo é descartado na montagem (música vem do Suno). Mesmo assim, peça no prompt uma música no mesmo BPM, para os movimentos já saírem no ritmo.

### 5.5 Conferir antes de aprovar

- [ ] Personagem igual à referência (chapéu com estrela, lenço vermelho, avental azul de bolinhas, olhos turquesa)
- [ ] Emenda em 10s sem salto (compare os frames 9,8s e 10,2s)
- [ ] Sem deformações (asas, olhos, bico, patas; nada "derretendo")
- [ ] Sem texto aleatório na tela
- [ ] Sem marca d'água
- [ ] Nada assustador ou perigoso
- [ ] Último frame igual ao `frame_inicio.png` (loop)

## 6. Música

**Decisão padrão:** a música inteira é gerada no **Suno**, numa faixa única, e sincronizada na edição. O áudio do Veo é descartado.

Motivo: o Veo faz bem música de fundo e falas curtas, mas cantar uma letra exata em português, com a mesma melodia do começo ao fim, é arriscado, e com 2 gerações por dia não dá para refazer. O Suno canta a letra exata numa faixa única, com a voz da Persona.

1. Suno → **Custom** → cole a letra (com as tags abaixo) e o estilo.
2. Se já existir a Persona "Chef Bolinha", selecione-a.
3. Gere 2 ou 3 versões. Escolha a que começa a cantar **imediatamente** e tem o refrão mais "grudento".
4. Baixe em MP3/WAV → `videos/musica.mp3`.
5. Ouça comparando com músicas infantis conhecidas. Se lembrar alguma, gere de novo.
6. **Uso comercial:** exige plano pago do Suno. Confira os termos da sua conta.

**Estilo (Suno):**

```
[estilo]
```

**Letra com tags (Suno):**

```
[letra]
```

Efeitos sonoros (onomatopeias de animais, "tchan", brilhos): use a biblioteca de sons do CapCut.

## 7. Montagem (CapCut)

1. Projeto **9:16**, 1080×1920, 30 fps.
2. Importe `completo_20s.mp4` (ou `parte1` + `parte2` em sequência). **Silencie** o áudio original.
3. Importe `musica.mp3`. Corte para começar **no 1º som** (sem silêncio) e para durar 20s.
4. Ajuste a velocidade de trechos do vídeo (95–105%) para que as ações caiam nos tempos da letra.
5. Adicione os efeitos sonoros marcados no roteiro.
6. **Loop:** o último frame deve estar igual ao `frame_inicio.png`. Se sobrar diferença, faça um corte seco (sem fade) no último tempo da música, sem fade-out de áudio.
7. Legenda com a letra (fonte grande e arredondada) nos refrões. Ajuda quem assiste sem som.
8. Exporte em 1080p, 30 fps → `videos/final.mp4`.

## 8. Publicação (YouTube Studio)

| Campo | Valor |
|---|---|
| Título | `[Tema] do Chef Bolinha 🐥✨ \| Musiquinha Infantil` |
| Descrição | (abaixo) |
| Playlist | |
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
[2 ou 3 linhas]

#musicainfantil #shorts #chefbolinha
```

**Tags (copiar):**

```
musiquinha infantil, música para bebê, música para crianças, música infantil, chef bolinha, [tema]
```

## 9. Checklist de publicação

- [ ] "Sim, é conteúdo para crianças" (nunca mudar para recuperar comentários)
- [ ] Divulgação de conteúdo alterado/sintético (IA) marcada
- [ ] Letra e melodia originais, sem semelhança com músicas conhecidas
- [ ] Etapa "Verificações" do upload sem aviso de direitos autorais
- [ ] Vídeo final sem marca d'água (ver nota)
- [ ] Ferramentas usadas permitem uso comercial (Gemini/Veo e Suno pago)
- [ ] Título, descrição e playlist conforme este MD
- [ ] Verificar no Studio → Conteúdo → Restrições 24h após postar

> **Marca d'água:** o ep01, gerado no Gemini, saiu **sem selo visível** (o Google mantém só a marca invisível SynthID). Se algum dia aparecer um selo "Veo" visível, não o cubra: ele é o rótulo de IA do Google. A regra vale para marcas de terceiros, como Dreamina e capafy.

## 10. Pós-publicação

| Métrica | 24h | 7 dias |
|---|---|---|
| Visualizações | | |
| Duração média da visualização | | |
| % média visualizada | | |
| Deslizaram vs. assistiram (Shorts) | | |
| Inscritos ganhos | | |
| Restrições (Studio) | | — |

Aprendizados:

-
