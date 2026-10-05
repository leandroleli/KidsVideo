# Canal Chef Bolinha: passo a passo

Músicas infantis originais de **2 a 4 minutos**, em **vídeo horizontal 16:9**, com o **Chef Bolinha** e os amigos dele. Cada música conta uma historinha com começo, meio e fim, como no vídeo de inspiração (Vaca Lola, "O balão levou Torito e Lolinha", https://www.youtube.com/watch?v=9mnn6WMilik).

> **Fluxo de cada música:** copie [`musicas/_modelo/`](musicas/_modelo/musica.md) para `musicas/mXX-<slug>/` e siga o `musica.md` do começo ao fim.
>
> Arquivos de apoio:
> - [`personagem.md`](personagem.md): bíblia do Chef Bolinha e prompt âncora
> - [`personagem/amigos/`](personagem/amigos/): bíblias da Vaquinha Nuvem e do Sementinha
> - [`scripts/montar_musica.py`](scripts/montar_musica.py): junta os clipes com a música

---

## Visão geral do fluxo

| # | Etapa | Ferramenta | Quando |
|---|-------|-----------|--------|
| 1 | História, letra e mapa de clipes | Claude (skill `chef-bolinha-musicas`) | Dia 0 |
| 2 | Música completa (2 a 4 min) | Suno | Dia 0 |
| 3 | Mapa com os tempos reais da música | Claude (Whisper na voz do Suno) | Dia 0 |
| 4 | Clipes de 20s, **2 por dia** | Gemini (imagem do 1º quadro + Veo) | Dia 1 em diante |
| 5 | Prévia diária e montagem final | `scripts/montar_musica.py` | Todo dia / no fim |
| 6 | Publicação e métricas | YouTube Studio | No fim |

**A música vem primeiro.** Ela define a duração de cada trecho e, por isso, quantos clipes faltam. Os clipes são cortados para caber nela, e nunca o contrário.

---

## Etapa 1: história e letra

Peça ao Claude: "cria a música m02" (ou "uma música sobre X"). A skill escreve o `musica.md` com:

- **História em 4 atos:** situação → problema engraçado → tentativas → solução e festa. Nada assustador: o "problema" é leve (um chapéu que voa, um bolo que rola, uma pipa presa na árvore).
- **Letra** com refrão repetido 3 ou 4 vezes, uma **ponte** de participação (pergunta e resposta, contagem, "cadê?") e um refrão final com a letra mudada (o problema resolvido).
- **Mapa de clipes:** cada trecho de ~20s da música ganha um clipe. **Os refrões reaproveitam clipes**, então uma música de 3 min precisa de 7 a 9 clipes novos, e não de 9 a 12.

## Etapa 2: música no Suno

1. Cole o **Style** e a **Lyrics** da seção 3 do `musica.md` no Suno (modo Custom), com a **Persona "Chef Bolinha"**.
2. Gere algumas versões e escolha uma com dicção clara e duração entre 2 e 4 min.
3. Salve como `musicas/mXX-<slug>/musica.wav` (ou `.mp3`).
4. Se mudar a letra no Suno, atualize a seção 3 antes da etapa 3.
5. O uso comercial exige **plano pago** do Suno.

## Etapa 3: mapa com os tempos reais

Peça ao Claude: "mapeia a música mXX". Ele separa a voz, acha o início de cada verso e preenche o `mapa.yaml`: de que segundo a que segundo vai cada clipe e onde entram os reaproveitados. A tabela de clipes do `musica.md` é atualizada com a duração real de cada um.

## Etapa 4: clipes de 20s (2 por dia)

Para cada clipe, na ordem do **plano de dias** do `musica.md`:

1. **1º quadro:** no Gemini (criação de imagem), anexe as referências dos personagens que aparecem (`*_referencia.png`) e cole o prompt de imagem do clipe. Formato **horizontal 16:9**. Salve como `imagens/cXX_inicio.png`.
2. **Parte A (0–10s):** em Vídeo, anexe o 1º quadro e cole o **bloco fixo** + o prompt da Parte A.
3. **Parte B (10–20s):** anexe o último quadro da Parte A e cole o **bloco fixo** + o prompt da Parte B. O Gemini devolve os 20s emendados.

   ```
   ffmpeg -sseof -0.1 -i clipes/c01a.mp4 -frames:v 1 imagens/c01a_ultimo.png
   ```

4. Salve o clipe final como `clipes/cXX.mp4` (ex.: `clipes/c03.mp4`).
5. Rode a prévia (etapa 5) para ver como a música está ficando.

**Clipes não precisam emendar entre si.** Num vídeo longo, o corte de uma cena para outra é normal. Por isso cada clipe parte do seu próprio 1º quadro, gerado com as referências, e um erro num clipe não estraga os outros.

**Regras de prompt que funcionaram** (testes de 01/10/2026):
- Linha de identidade **positiva** ("Nuvem has white fur with light-gray cloud spots"), sem negações ("no beak").
- Cada ação diz **quem** faz e **de que lado** ("the red strawberry on the right jumps").
- **Câmera parada** ou movimento lento. Nada de efeito em detalhe pequeno (as sementes do Sementinha deformaram tudo).
- **Sem falar nem cantar com a boca** (o áudio do Veo é descartado e a boca não bateria com a música). Sorrisos, risadas abertas e "Muu!" curtos estão liberados.
- Posições fixas na música inteira: **Nuvem à esquerda, Bolinha no meio, Sementinha à direita**, salvo quando a história pedir outra coisa.

## Etapa 5: montagem

```
python scripts/montar_musica.py musicas/mXX-<slug>
```

- Lê o `mapa.yaml`, corta cada trecho do clipe certo, junta tudo em 1920×1080 a 24 fps e coloca a música do Suno por cima (áudio do Veo descartado, volume em -14 LUFS).
- **Clipe que ainda não existe vira uma tela cinza**, então dá para rodar todo dia e ver a música "se completando".
- Clipe mais curto que o trecho tem o último quadro congelado; o relatório avisa.
- Saída em `musicas/mXX-<slug>/montagem/`: `final.mp4` e `relatorio.md`.

## Etapa 6: publicar e medir

1. **YouTube Studio → Criar → Enviar vídeos**, com os dados da seção 7 do `musica.md`:
   - **Título:** `[Título da música] 🎩 | Chef Bolinha | Música Infantil`
   - **Descrição:** 2 ou 3 linhas sobre a história + a letra completa + `#musicainfantil #chefbolinha #desenhoinfantil`
   - **Tags:** `música infantil, musica para crianças, desenho infantil, música para bebê` + tema e personagens
   - **Público:** **"Sim, é conteúdo para crianças"**. É **obrigatório por lei (COPPA)**, e marcar errado pode gerar multa e derrubar o canal.
   - **Conteúdo alterado/sintético:** **Sim**
   - **Idioma:** Português (Brasil). **Categoria:** Educação.
2. **Thumbnail:** um quadro de um dos clipes com a ação principal (ex.: o chapéu voando), personagens grandes e sem texto pequeno.
3. **Métricas:** anote em 24h e em 7 dias na seção 8 do `musica.md`.

---

## Monetização: expectativas

- Para ganhar qualquer coisa é preciso entrar no **Programa de Parcerias (YPP)**: 1.000 inscritos **e** 4.000 horas assistidas em 12 meses. Vídeos longos contam horas assistidas, coisa que os Shorts não fazem. Por isso o formato de 2 a 4 min.
- Conteúdo **"Feito para crianças"** não tem anúncio personalizado, e por isso paga menos por view.
- Comentários e sininho desativados são **esperados** em vídeo para crianças. Nunca mude a marcação para recuperá-los.

---

## Anti "conteúdo produzido em massa"

Desde 2025 o YouTube recusa monetizar canais com vídeos de IA "em série", todos iguais e com pouco valor original. Os personagens fixos são a marca do canal. **Todo o resto varia de uma música para outra:**

| Eixo | Como variar |
|---|---|
| História / problema | Sempre um problema diferente (chapéu voou, bolo rolou, pipa presa, ovo sumiu, chuva no piquenique) |
| Cenário | Fazendinha, horta de morangos, cozinha, lagoa, jardim, parque, praia. Não repetir em músicas seguidas |
| Luz / hora do dia | Manhã, meio-dia, tarde dourada, noite estrelada |
| Ritmo e estilo | Pop infantil, forró/baião, marchinha, xote, reggae infantil, valsinha, rock de brinquedo |
| Andamento | 80 a 130 BPM, sem repetir em músicas seguidas |
| Participação | Pergunta e resposta, contagem, "cadê?", imitar som de bicho, bater palmas |
| Protagonista | Alterna quem resolve o problema: Bolinha, Nuvem ou Sementinha |

**Outros cuidados:**
- **Direitos autorais:** nada de personagens, músicas ou nomes de canais existentes (veja a lista abaixo).
- **Qualidade para criança:** assista ao vídeo inteiro antes de publicar. Nada assustador, estranho ou deformado.
- **Custos:** anote quanto gasta de IA por música (plano do Gemini + Suno).

---

## Músicas conhecidas a evitar

Nada de letra, melodia ou estrutura parecida com:

Seu Lobato ("ia-ia-ô"), Cinco Patinhos, **Pintinho Amarelinho** (o Bolinha é um pintinho amarelo: nunca use essa expressão), Galinha Pintadinha, Sapo Não Lava o Pé, Sapo Cururu, Borboletinha, Atirei o Pau no Gato, A Dona Aranha, Parabéns pra Você, Brilha Brilha Estrelinha, Ciranda Cirandinha, Baby Shark, Eguinha Pocotó, **A Vaca Lola**, **Boi da Cara Preta**.

---

## Checklist de publicação

Cada `musica.md` tem uma cópia deste checklist. Marque lá.

- [ ] "Sim, é conteúdo para crianças" (nunca mudar para recuperar comentários)
- [ ] Divulgação de conteúdo alterado/sintético (IA) marcada
- [ ] Letra e melodia originais, sem semelhança com músicas conhecidas (risco de Content ID)
- [ ] Etapa "Verificações" do upload sem aviso de direitos autorais
- [ ] Vídeo inteiro assistido: nenhum personagem deformado, nenhuma tela cinza
- [ ] Ferramentas usadas permitem uso comercial (Gemini/Veo e Suno pago)
- [ ] Título, descrição (com a letra) e thumbnail conforme a seção 7
- [ ] Verificar no Studio → Conteúdo → Restrições 24h após postar
