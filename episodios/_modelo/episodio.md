# EPxx: [Título do episódio]

> Copie esta pasta (`_modelo/`) para `episodios/epXX-<slug>/`, crie `videos/` e `imagens/` dentro dela e preencha todos os campos.
> Este arquivo é autossuficiente: com ele você gera e publica o vídeo sem abrir outro.

Referência do personagem: [`../../personagem/bolinha_referencia.png`](../../personagem/bolinha_referencia.png) (use a versão `_limpa` quando existir)

---

## 1. Resumo

| Campo | Valor |
|---|---|
| Série | Comidas / Cores / Animais / Números / Rotina |
| Tema | |
| Duração-alvo | 24s (3 clipes de 8s) |
| Data de publicação | AAAA-MM-DD |
| Status | roteiro / gerando / publicado |

## 2. Ficha de variação

Compare com os últimos 3 episódios. Se 3 ou mais itens coincidirem, mude.

| Item | Este episódio |
|---|---|
| Melodia (tonalidade, contorno, motivo) | |
| Andamento (BPM) | |
| Instrumento principal | |
| Cenário | |
| Estrutura musical | acumulativa / pergunta e resposta / onomatopeia / contagem / ninar |
| Momento surpresa | |

## 3. Roteiro por cena

| Tempo | Clipe | Cena (visual) | Áudio |
|---|---|---|---|
| 0:00–0:01 | 1 | **Gancho:** personagem já em ação + som forte | |
| 0:01–0:08 | 1 | | Refrão (1ª vez) |
| 0:08–0:16 | 2 | Estrofe + momento surpresa | Estrofe |
| 0:16–0:21 | 3 | | Refrão (2ª vez) |
| 0:21–0:24 | 3 | **Loop:** termina na mesma pose/cena do 1º frame | |

## 4. Letra

**Refrão** (2 a 4 versos, repetido ≥ 2x):

```
```

**Letra completa, por clipe:**

| Clipe | Tempo | Trecho |
|---|---|---|
| 1 | 0–8s | |
| 2 | 8–16s | |
| 3 | 16–24s | |

Regras: frases curtas, palavras simples (1 a 4 anos), rima fácil, onomatopeia ou contagem, nada parecido com músicas infantis conhecidas.

## 5. Geração no Gemini (Veo)

**Limite atual:** clipes de **até 8s** por geração. No plano AI Pro são **cerca de 3 gerações por dia** (confira o contador no app). Por isso o padrão é **3 clipes × 8s = 24s**. Se precisar refazer um clipe, deixe para o dia seguinte ou use o **Flow** (labs.google/flow) com o mesmo plano.

### 5.1 Preparar o 1º frame

1. No Gemini (criação de imagem), anexe a referência do personagem e peça a cena de abertura **em 9:16**:

   ```
   [prompt da imagem do 1º frame: cenário + pose inicial + âncora do personagem]
   ```

2. Salve como `imagens/frame_inicio.png`. Esse frame também é o **frame do loop**: o clipe 3 precisa terminar igual a ele.

### 5.2 Gerar cada clipe

1. Gemini → **Vídeo** (Veo) → anexe a imagem indicada no clipe (vira o 1º frame).
2. Escolha **9:16** (vertical) se o seletor aparecer. Se o app só oferecer 16:9, gere no **Flow**, que tem formato vertical.
3. Cole o prompt do clipe **inteiro** (já contém a âncora do personagem).
4. Baixe e salve em `videos/clipeN.mp4`.
5. Extraia o último frame para usar no próximo clipe:

   ```
   ffmpeg -sseof -0.1 -i videos/clipeN.mp4 -frames:v 1 imagens/clipeN_ultimo_frame.png
   ```

**Clipe 1 (0–8s)**, imagem inicial: `imagens/frame_inicio.png`

```
[prompt]
```

**Clipe 2 (8–16s)**, imagem inicial: `imagens/clipe1_ultimo_frame.png`

```
[prompt]
```

**Clipe 3 (16–24s)**, imagem inicial: `imagens/clipe2_ultimo_frame.png`

```
[prompt]
```

### 5.3 Continuidade

- O último frame de um clipe é o 1º do próximo (passo 5 acima).
- Mesmo cenário, mesma hora do dia e mesma luz em todos os prompts (copie a frase de cenário igual).
- Câmera sem cortes dentro do clipe. Movimentos suaves.
- O áudio do Veo é descartado na montagem. Os prompts pedem "no dialogue, no music" para não atrapalhar.

### 5.4 Conferir antes de aprovar cada clipe

- [ ] Personagem igual à referência (chapéu com estrela, lenço vermelho, avental azul de bolinhas, olhos turquesa)
- [ ] Sem deformações (asas, olhos, bico, patas; nada "derretendo")
- [ ] Sem texto aleatório na tela
- [ ] Sem marca d'água de terceiros (Dreamina etc.)
- [ ] Nada assustador ou perigoso
- [ ] Último frame limpo (sem borrão) para servir de início ao próximo clipe

## 6. Música

**Decisão padrão:** a música inteira é gerada no **Suno**, numa faixa única, e sincronizada na edição. O áudio do Veo é descartado.

Motivo: o Veo gera o áudio clipe por clipe, então a voz, o tom e o andamento mudam entre clipes. Uma faixa única garante voz e melodia consistentes.

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
2. Coloque os clipes 1, 2 e 3 em sequência. **Silencie** o áudio original dos clipes.
3. Importe `musica.mp3`. Corte para começar **no 1º som** (sem silêncio) e para durar 24s.
4. Ajuste a velocidade dos clipes (95–105%) para que as ações caiam nos tempos da letra.
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
- [ ] Vídeo final sem marca d'água de terceiros (ver nota)
- [ ] Ferramentas usadas permitem uso comercial (Gemini/Veo e Suno pago)
- [ ] Título, descrição e playlist conforme este MD
- [ ] Verificar no Studio → Conteúdo → Restrições 24h após postar

> **Nota sobre o selo "Veo":** vídeos do Gemini saem com um selo visível "Veo", que é a identificação de IA do Google (além da marca invisível SynthID). **Não cubra nem remova esse selo.** Ele funciona como rótulo de IA. Se quiser o vídeo sem selo, gere onde o seu plano exportar sem ele e confira no próprio app. A regra "sem marca d'água" vale para marcas de terceiros, como Dreamina e capafy.

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
