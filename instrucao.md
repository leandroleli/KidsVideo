# Canal de vídeos infantis com IA: passo a passo

Baseado no vídeo do TikTok (@ai.ghost29) que está nesta pasta. A ideia: criar vídeos curtos de musiquinhas infantis animadas (estilo "nursery rhymes") com IA e postar no YouTube, cerca de 7 por semana.

---

## Visão geral do fluxo

| # | Etapa | Ferramenta |
|---|-------|-----------|
| 1 | Achar um canal de referência que está bombando | YouTube |
| 2 | Entender quanto o YouTube paga | Google |
| 3 | Gerar o roteiro/prompt de um vídeo viral de 60s | ChatGPT (ou Claude) |
| 4 | Abrir o agente gerador de vídeo | capafy.ai → "Odeo Maker" |
| 5 | Colar o prompt e deixar a IA gerar os clipes | capafy.ai |
| 6 | Baixar os clipes e postar | YouTube Studio |

---

## Passo 1: Achar um canal de referência

1. Abra o YouTube e pesquise canais infantis grandes. No vídeo ele usou o **NuNu Tv - Nursery Rhymes** (cerca de 28 milhões de inscritos).
2. Outros exemplos do mesmo nicho: Cocomelon, Super Simple Songs, ChuChu TV, BabyBus, Little Angel.
3. Na aba **Vídeos** / **Shorts**, ordene por **Populares** e anote:
   - os temas que mais dão views (comida, animais, cores, números, hora de dormir, "wheels on the bus"…)
   - o estilo visual (3D fofinho, cores fortes, personagem bebê)
   - a duração e o formato (Shorts de até 60s ou vídeos longos)
   - como são os títulos e as thumbnails

> **Importante:** use esses canais só como **inspiração**. Não copie personagens, músicas nem nomes deles, porque isso gera strike de direitos autorais.

---

## Passo 2: Pesquisar quanto o YouTube paga

No Google, pesquise: `how much does youtube pay for 1 million views`.

Para ter expectativas realistas:
- **Para ganhar qualquer coisa**, você precisa entrar no **Programa de Parcerias do YouTube (YPP)**. Os requisitos são 1.000 inscritos **e** 4.000 horas assistidas em 12 meses, **ou** 1.000 inscritos **e** 10 milhões de views em Shorts em 90 dias.
- **Shorts pagam bem menos** que vídeos longos (em geral centavos de dólar a cada 1.000 views).
- **Conteúdo infantil** ("Feito para crianças") não tem anúncios personalizados, então paga menos por view.
- Dá para ganhar dinheiro com isso, mas não é garantido. Leva meses de consistência.

---

## Passo 3: Gerar o prompt do vídeo no ChatGPT

Abra o ChatGPT (ou o Claude) e peça um roteiro. Modelo de prompt:

```
Crie um roteiro para um vídeo infantil viral de 60 segundos, no estilo nursery rhyme
(musiquinha infantil) para YouTube Shorts, formato vertical 9:16.

Requisitos:
- Personagem principal fofo e original (descreva aparência de forma consistente)
- Estilo visual: animação 3D fofa, cores vibrantes, estilo Pixar/Cocomelon
- Hook forte nos primeiros 3 segundos
- Música simples e repetitiva, com refrão fácil de cantar
- Divida em cenas com timestamp (ex: 0:00–0:05, 0:05–0:15...)
- Para cada cena: descrição visual + letra cantada
- Tema: [ex: um mini chef fazendo uma sopa mágica]

No final, gere um prompt de vídeo para IA de cada cena (em inglês),
separados como Clip 1, Clip 2, Clip 3...
```

No vídeo, o resultado foi **"Tiny Chef's Magic Soup"**, dividido em cenas:
- `0:00–0:05`: **Hook**: um mini chef pula num balcão de cozinha gigante e canta.
- `0:05–0:15`: **Ingredient Song**: os ingredientes pulam na panela um por um.
- … (refrão, reviravolta engraçada, final em loop)

**Dicas:**
- Mantenha o **mesmo personagem** em todos os vídeos. Isso cria uma "marca" para o canal.
- Termine o vídeo de um jeito que "emende" no começo (loop), porque isso aumenta a retenção.

---

## Passo 4: Abrir o agente gerador de vídeo (capafy.ai)

1. Acesse **capafy.ai** (marketplace de agentes de IA).
2. Crie uma conta.
3. Na busca, digite **"Odeo Maker"**. O agente é descrito como "Generate AI videos from images or prompts, optimized for watch time and completion…".
4. Abra um **chat** com o agente. No vídeo aparece também o agente "Viral Clone / CloneCut", que usa o modelo **Seedance 2.0**.

> É uma plataforma **paga** (no vídeo aparece um saldo em USD no canto da tela). Veja o preço por vídeo/clipe **antes** de gerar muita coisa. Pelo que aparece, cada clipe tem no máximo ~15s, então um vídeo de 60s = uns 4 a 5 clipes.

**Alternativas** se não quiser usar o capafy: Kling, Hailuo/MiniMax, Runway, Google Veo, Pika, ou o próprio Seedance direto. Para a música: Suno ou Udio.

---

## Passo 5: Colar o prompt e deixar a IA trabalhar

1. Cole no chat o roteiro/prompts do Passo 3.
2. O agente gera **um clipe por vez** (ex: `tiny_chef_clip1_hook_and_ingredients.mp4`).
3. O primeiro clipe vira a **âncora de estilo/personagem**. Confira se o personagem ficou bom antes de pedir os próximos.
4. Peça: *"Pronto para o Clip 2"*, depois Clip 3, e assim por diante.
5. Se algo ficar estranho (mão deformada, personagem mudando), peça para refazer só aquele clipe.

---

## Passo 6: Baixar e postar

1. Clique em **Download** em cada clipe. No vídeo foram 5 arquivos:
   - `tiny_chef_clip1_hook_and_ingredients.mp4`
   - `tiny_chef_clip2_surprise.mp4`
   - `tiny_chef_clip3_chorus.mp4`
   - `tiny_chef_clip4_…moment.mp4`
   - `tiny_chef_clip5_end_loop.mp4`
2. **Opção A (igual ao vídeo):** posta cada clipe como um Short separado.
   **Opção B (recomendado):** junta os clipes num vídeo só de 60s no CapCut ou no Canva, com música/legenda, e posta como um Short.
3. No **YouTube Studio → Criar → Enviar vídeos**:
   - **Título:** curto e chamativo (ex: `Tiny Chef's Magic Soup 🍲 | Nursery Rhymes & Kids Songs`)
   - **Descrição:** 2 ou 3 linhas + hashtags (`#nurseryrhymes #kidssongs #shorts`)
   - **Público:** marque **"Sim, é conteúdo para crianças"**. Isso é **obrigatório por lei (COPPA)**, e marcar errado pode gerar multa e derrubar o canal.
   - **Conteúdo alterado/sintético:** marque a opção de **conteúdo gerado por IA** quando o YouTube pedir.
4. Meta do vídeo: **7 vídeos por semana** (1 por dia).

---

## Cuidados importantes

- **Conteúdo repetitivo/produzido em massa:** desde 2025 o YouTube recusa monetização de canais com vídeos de IA "em série", todos iguais e com pouco valor original. Para evitar isso, varie os temas, crie músicas/letras próprias e mantenha qualidade.
- **Direitos autorais:** nada de usar personagens, músicas ou nomes de canais existentes.
- **Qualidade para criança:** revise cada vídeo. Nada assustador, estranho ou inadequado, porque o YouTube é rígido com conteúdo infantil.
- **Custos:** calcule quanto gasta de IA por vídeo e compare com o que o canal ganha.

---

## Checklist rápido por vídeo

- [ ] Escolher tema (com base nos Populares dos canais de referência)
- [ ] Gerar roteiro + prompts no ChatGPT/Claude
- [ ] Gerar clipes no capafy.ai (Odeo Maker), um por vez
- [ ] Revisar a qualidade de cada clipe
- [ ] Baixar e (opcional) juntar no CapCut
- [ ] Subir no YouTube: título, descrição, "Feito para crianças", aviso de IA
- [ ] Repetir: 7x por semana
