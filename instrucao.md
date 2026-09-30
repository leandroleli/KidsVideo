# Canal de vídeos infantis com IA: passo a passo

Baseado no vídeo do TikTok (@ai.ghost29) que está nesta pasta (fora do git). A ideia: criar Shorts de **musiquinhas infantis mágicas** com o **Chef Bolinha**, animadas com IA, e postar no YouTube, cerca de 7 por semana.

> **Fluxo padrão de cada vídeo:** copie [`episodios/_modelo/`](episodios/_modelo/episodio.md) para `episodios/epXX-<slug>/` e siga o `episodio.md` do começo ao fim (roteiro → geração → música → montagem → publicação → métricas).
>
> Arquivos de apoio:
> - [`personagem.md`](personagem.md): bíblia do personagem e prompt âncora
> - [`series-e-calendario.md`](series-e-calendario.md): séries, temas e calendário

---

## Visão geral do fluxo

| # | Etapa | Ferramenta |
|---|-------|-----------|
| 1 | Achar canais de referência que estão bombando | YouTube |
| 2 | Entender quanto o YouTube paga | Google |
| 3 | Escrever roteiro e letra de um Short de 20–30s | ChatGPT (ou Claude) + `episodio.md` |
| 4 | Gerar os clipes de vídeo | **Gemini (Veo)**; alternativas: Dreamina, capafy.ai |
| 5 | Gerar a música cantada | Suno |
| 6 | Montar, publicar e medir | CapCut + YouTube Studio |

---

## Aprendizados do 1º Short ("A Sopa Mágica", 21s)

- **Comentários e notificações desativados são esperados.** Todo vídeo marcado como "Sim, é conteúdo para crianças" tem comentários, sininho de notificação e alguns recursos desligados automaticamente. Isso não é erro nem punição, e **nunca** se muda a marcação para recuperá-los.
- **O alcance vem de três lugares:** o **feed de Shorts**, a **busca** e a **retenção/replay**. Por isso:
  - **Gancho no 1º segundo:** personagem em ação e música já tocando, sem introdução.
  - **Loop:** a última cena emenda na primeira (mesma pose, mesmo enquadramento). Assim a pessoa assiste de novo sem perceber.
  - **Refrão curto repetido pelo menos 2x:** a criança pede "de novo".
  - **Título, descrição e tags em PT-BR** com o que os pais buscam: "musiquinha infantil", "música para bebê", "música para crianças" + o tema.
- O ep01 abriu sem o personagem, teve loop só parcial e não tinha música cantada. Detalhes em [`episodios/ep01-sopa-magica/episodio.md`](episodios/ep01-sopa-magica/episodio.md).

---

## Passo 1: Achar canais de referência

1. Abra o YouTube e pesquise canais infantis grandes. No vídeo ele usou o **NuNu Tv - Nursery Rhymes** (cerca de 28 milhões de inscritos).
2. Outros exemplos do mesmo nicho: Cocomelon, Super Simple Songs, ChuChu TV, BabyBus, Little Angel. Em português: Galinha Pintadinha, Mundo Bita, Bob Zoom.
3. Na aba **Vídeos** / **Shorts**, ordene por **Populares** e anote:
   - os temas que mais dão views (comida, animais, cores, números, hora de dormir…)
   - o estilo visual (3D fofinho, cores fortes, personagem bebê)
   - a duração e o formato
   - como são os títulos e as thumbnails

> **Importante:** use esses canais só como **inspiração**. Não copie personagens, músicas nem nomes deles, porque isso gera strike de direitos autorais. A lista de músicas conhecidas a evitar está em [`series-e-calendario.md`](series-e-calendario.md).

---

## Passo 2: Pesquisar quanto o YouTube paga

No Google, pesquise: `quanto o youtube paga por 1 milhão de visualizações`.

Para ter expectativas realistas:
- **Para ganhar qualquer coisa**, você precisa entrar no **Programa de Parcerias do YouTube (YPP)**. Os requisitos são 1.000 inscritos **e** 4.000 horas assistidas em 12 meses, **ou** 1.000 inscritos **e** 10 milhões de views em Shorts em 90 dias.
- **Shorts pagam bem menos** que vídeos longos (em geral centavos de dólar a cada 1.000 views).
- **Conteúdo infantil** ("Feito para crianças") não tem anúncios personalizados, então paga menos por view.
- Dá para ganhar dinheiro com isso, mas não é garantido. Leva meses de consistência.

---

## Passo 3: Roteiro e letra

1. Escolha o próximo tema em [`series-e-calendario.md`](series-e-calendario.md).
2. Copie `episodios/_modelo/` para a pasta do episódio.
3. Peça o roteiro ao ChatGPT ou ao Claude com o prompt abaixo e cole o resultado nas seções 2 a 4 do `episodio.md`.

```
Crie um Short de musiquinha infantil ORIGINAL, em português do Brasil, para o YouTube
(vertical 9:16), com o personagem Chef Bolinha (pintinho amarelo de chapéu de chef,
lenço vermelho e avental azul de bolinhas).

Série: [Comidas / Cores / Animais / Números / Rotina]
Tema: [ex: a Vaquinha Nuvem na fazendinha]
Cenário: [da série]  |  Estrutura musical: [da série]  |  Andamento: [BPM da série]

Regras:
- Duração de 24s, dividida em 3 clipes de 8s (limite do Veo). Timestamps por cena.
- Gancho no 1º segundo: personagem já em ação e música tocando, sem introdução.
- Letra original: frases curtas, palavras simples (1 a 4 anos), rima fácil,
  onomatopeias ou contagem conforme a série.
- Refrão de 2 a 4 versos, repetido pelo menos 2x.
- Nenhuma semelhança com músicas infantis conhecidas (Seu Lobato, Cinco Patinhos,
  Pintinho Amarelinho, Galinha Pintadinha, Borboletinha etc.).
- Um momento surpresa engraçado (sem "brilho mágico na panela").
- Loop: a última cena termina na mesma pose e enquadramento da primeira.
- Diga qual trecho da letra cai em cada clipe.

No final, gere um prompt de vídeo em inglês para cada clipe (Clipe 1, 2, 3), repetindo
em todos a descrição âncora do personagem e a mesma frase de cenário.
```

**Dicas:**
- Mantenha o **mesmo personagem** em todos os vídeos. Use sempre o prompt âncora do [`personagem.md`](personagem.md).
- Preencha a **ficha de variação** e compare com os últimos 3 episódios antes de gerar.

---

## Passo 4: Gerar os clipes no Gemini (Veo)

1. Abra o **Gemini** (gemini.google.com ou app) com a conta do plano Google AI.
2. **Limites atuais:** cada clipe tem **até 8s**, e o plano AI Pro permite **cerca de 3 vídeos por dia** (confira no app). Por isso o padrão é **3 clipes = 24s**.
3. Primeiro gere a **imagem do 1º frame** (Gemini, criação de imagem) anexando a referência do personagem.
4. Em **Vídeo**, anexe a imagem (ela vira o 1º frame), escolha **9:16** e cole o prompt do clipe.
5. Para o clipe seguinte, use o **último frame** do anterior como imagem inicial:

   ```
   ffmpeg -sseof -0.1 -i videos/clipe1.mp4 -frames:v 1 imagens/clipe1_ultimo_frame.png
   ```

6. O passo a passo completo, com os prompts prontos, fica na seção 5 de cada `episodio.md`.

> **Selo "Veo":** os vídeos do Gemini saem com um selo visível "Veo" (identificação de IA do Google) e a marca invisível SynthID. Não cubra nem remova o selo.

**Alternativas:**
- **Flow** (labs.google/flow): mesmo Veo, com mais controle de frames e formato vertical.
- **Dreamina**: usado no ep01. Atenção à marca d'água "Dreamina AI" nas imagens.
- **capafy.ai** ("Odeo Maker", do vídeo de referência): pago, clipes de até ~15s.
- Outras: Kling, Hailuo/MiniMax, Runway, Pika.

---

## Passo 5: Gerar a música (Suno)

1. A música inteira é feita no **Suno**, numa faixa única. Isso garante a mesma voz e melodia do começo ao fim. O áudio dos clipes do Veo é descartado.
2. Use a **Persona "Chef Bolinha"** para manter a voz entre episódios (criada no ep02).
3. Uso comercial exige **plano pago** do Suno.
4. O estilo e a letra com tags ficam na seção 6 de cada `episodio.md`.

---

## Passo 6: Montar, publicar e medir

1. **Montagem no CapCut** (seção 7 do `episodio.md`):
   - projeto 9:16;
   - clipes silenciados e música sincronizada;
   - efeitos sonoros;
   - legenda nos refrões;
   - corte seco no final para fechar o loop.
2. **YouTube Studio → Criar → Enviar vídeos.** Preencha tudo conforme a seção 8 do `episodio.md`:
   - **Título:** `[Tema] do Chef Bolinha 🍲✨ | Musiquinha Infantil`. Troque o emoji pelo da série.
   - **Descrição:** 2 ou 3 linhas + `#musicainfantil #shorts #chefbolinha`
   - **Tags:** `musiquinha infantil, música para bebê, música para crianças` + tema
   - **Playlist:** a da série (ver [`series-e-calendario.md`](series-e-calendario.md))
   - **Público:** **"Sim, é conteúdo para crianças"**. Isso é **obrigatório por lei (COPPA)**, e marcar errado pode gerar multa e derrubar o canal.
   - **Conteúdo alterado/sintético:** **Sim**
   - **Idioma:** Português (Brasil). **Categoria:** Educação.
3. **Métricas:** anote em 24h e em 7 dias (seção 10 do `episodio.md`).
4. Meta: **7 vídeos por semana** (1 por dia), conforme o calendário.

---

## Anti "conteúdo produzido em massa"

Desde 2025 o YouTube recusa monetização de canais com vídeos de IA "em série", todos iguais e com pouco valor original. O personagem fixo é a marca do canal. **Todo o resto varia.**

**Matriz de variação** (preencha a ficha de cada `episodio.md` e compare com os 3 anteriores; se 3 ou mais linhas coincidirem, mude):

| Eixo | Como variar |
|---|---|
| Série | Nunca a mesma série em dois dias seguidos (rotação no calendário) |
| Cenário | Um por série: cozinha, horta/feira, fazenda, padaria/mercadinho, casa |
| Luz / hora do dia | Manhã, meio-dia, tarde dourada, noite |
| Estrutura musical | Acumulativa, pergunta e resposta, onomatopeia, contagem, passo a passo/ninar |
| Instrumento | Marimba, piano de brinquedo, ukulele, glockenspiel, violão/caixinha de música |
| Andamento | 70 a 120 BPM conforme a série |
| Tonalidade | Não repetir em episódios seguidos (Dó → Sol → Ré → Fá → Lá) |
| Momento surpresa | Sempre diferente; nada de repetir o "brilho mágico na panela" |
| Final / loop | A pose e a ação do loop mudam por episódio |
| Personagens convidados | Os animais podem voltar em outras séries (ex.: a Vaquinha Nuvem no Bolo) |

**Outros cuidados:**
- **Direitos autorais:** nada de usar personagens, músicas ou nomes de canais existentes. Veja a lista de músicas a evitar em [`series-e-calendario.md`](series-e-calendario.md).
- **Qualidade para criança:** revise cada vídeo. Nada assustador, estranho ou inadequado, porque o YouTube é rígido com conteúdo infantil.
- **Custos:** calcule quanto gasta de IA por vídeo (plano do Gemini + Suno) e compare com o que o canal ganha.

---

## Checklist de publicação

Cada `episodio.md` tem uma cópia deste checklist. Marque lá.

- [ ] "Sim, é conteúdo para crianças" (nunca mudar para recuperar comentários)
- [ ] Divulgação de conteúdo alterado/sintético (IA) marcada
- [ ] Letra e melodia originais, sem semelhança com músicas conhecidas (risco de Content ID)
- [ ] Etapa "Verificações" do upload sem aviso de direitos autorais
- [ ] Vídeo final sem marca d'água de terceiros (o selo "Veo" do Google fica)
- [ ] Ferramentas usadas permitem uso comercial (Gemini/Veo e Suno pago)
- [ ] Título, descrição e playlist conforme o template / `episodio.md`
- [ ] Verificar no Studio → Conteúdo → Restrições 24h após postar
