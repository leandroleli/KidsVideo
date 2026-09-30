# EP01: A Sopa Mágica

Referência do personagem: [`../../personagem/bolinha_referencia.png`](../../personagem/bolinha_referencia.png)

> Episódio **já publicado**. Não será reenviado nem terá "v2", para não ser tratado como conteúdo duplicado. Este MD documenta o que foi feito e o que aprendemos.

---

## 1. Resumo

| Campo | Valor |
|---|---|
| Série | 🍲 Comidas |
| Tema | O Chef Bolinha faz uma sopa que fica mágica |
| Duração | 21s publicado (arquivo `videos/Videos2.mp4`: 20s, 720×1280, 24 fps) |
| Data de publicação | 2026-09-28 |
| Status | publicado |

## 2. Ficha de variação

| Item | Este episódio |
|---|---|
| Melodia | **Sem música cantada**: só falas e música de fundo gerada pelo próprio Veo |
| Andamento | ~120 BPM (pedido no prompt) |
| Instrumento principal | Ukulele + xilofone + palmas (pedido no prompt) |
| Cenário | Cozinha pastel (paredes creme, armários menta, prateleira rosa com bules), panela turquesa no fogão |
| Estrutura musical | Nenhuma (falas soltas) |
| Momento surpresa | Explosão de brilhos na panela; uma cenoura sorridente pula na sopa e vira estrela; a panela brilha no final |

## 3. Roteiro por cena

Reconstruído a partir dos frames do vídeo. As falas foram transcritas com Whisper (`medium`, pt).

| Tempo | Cena (visual) | Áudio / fala |
|---|---|---|
| 0:00–0:01 | Panela vazia no fogão, **sem o personagem** | Jingle |
| 0:01–0:03 | Explosão de brilhos coloridos saindo da panela | Jingle |
| 0:03–0:06 | Close do Bolinha, animado, olhando para a câmera | **"Ei! Olha a sopa mágica!"** (0:00–0:04 na transcrição) |
| 0:06–0:10 | Bolinha mexe a sopa e dança; bolhas coloridas estouram virando estrelas | Jingle |
| 0:10–0:16 | *(geração 2)* Bolinha continua mexendo; uma cenoura sorridente pula na sopa | Jingle |
| 0:16–0:18 | Bolinha prova a sopa na colher | **"Hum, de novo!"** (o prompt pedia "Hummm! De novo?!") |
| 0:18–0:20 | A panela brilha forte; brilhos cobrem o Bolinha | Jingle |

## 4. Letra

Não tem letra cantada. Falas:

```
Ei! Olha a sopa mágica!
Hum, de novo!
```

## 5–7. Geração, música e montagem

Gerado no **Gemini (Veo)** em 2 gerações, antes da adoção deste modelo. A imagem de referência anexada foi a do Dreamina (com marca d'água), mas o vídeo final saiu **sem marca d'água visível**. Áudio (música + falas) gerado pelo próprio Veo.

**Geração 1** → vídeo de 10s. Anexo: imagem de referência do personagem.

```
Vertical 9:16, high-quality 3D kids animation, soft lighting, vibrant pastel colors. Use the reference image for the main character, Chef Bolinha, a round fluffy yellow baby chick chef; keep it identical. Cozy pastel kitchen, turquoise cauldron on a small stove. A burst of rainbow sparkles explodes from the cauldron and Bolinha pops out, lands and looks at the camera, excited, saying in Brazilian Portuguese: "Ei! Olha a sopa mágica!" Then it starts stirring the cauldron with a golden-tipped spoon, dancing, as colorful bubbles pop into stars. Cheerful ukulele and xylophone music, hand claps, ~120 BPM.
```

**Geração 2** → o Gemini devolveu o **vídeo completo de 20s** (os 10s anteriores + a continuação, sem salto na emenda). Anexo: último frame da geração 1 (`imagens/bolinha_parte1_ultimo_frame.png`).

```
Vertical 9:16, high-quality 3D kids animation, soft lighting, vibrant pastel colors. Start exactly from the attached image: Chef Bolinha stirring the turquoise cauldron with a golden-tipped wooden spoon in the same pastel kitchen; keep the character identical. A smiling cartoon carrot jumps into the soup and turns into a spinning orange star. Bolinha tastes a spoonful, eyes sparkle, feathers fluff up with joy, winks at the camera and says in Brazilian Portuguese: "Hummm! De novo?!" At the end the cauldron bubbles and glows brightly with rainbow sparkles. Cheerful ukulele and xylophone music, hand claps, ~120 BPM.
```

**Montagem:** `videos/Videos2.mp4` (20s) publicado praticamente direto. A versão publicada tem 21s.

**O que funcionou:**
- A frase `Start exactly from the attached image` fez a continuação sem salto.
- Os mesmos parâmetros de estilo nos dois prompts mantiveram o personagem idêntico.
- O Veo falou português corretamente.

## 8. Publicação (YouTube Studio): metadados novos para aplicar manualmente

| Campo | Valor |
|---|---|
| Título | `Sopa Mágica do Chef Bolinha 🍲✨ \| Musiquinha Infantil` |
| Playlist | **Cozinha do Chef Bolinha 🍲 (Comidas)** |
| Público | Sim, é conteúdo para crianças (não alterar) |
| Conteúdo alterado ou sintético | Sim |
| Idioma do vídeo / título e descrição | Português (Brasil) |
| Categoria | Educação |

> Como o ep01 não tem musiquinha cantada, uma alternativa de título mais fiel é `Sopa Mágica do Chef Bolinha 🍲✨ | Desenho Infantil`.

**Descrição (copiar):**

```
Ei, olha a sopa mágica! ✨ O Chef Bolinha mexe, mexe a panela e a sopa se enche de brilhos e bolhas coloridas! 🍲🫧
Desenho infantil para bebês e crianças. Novo episódio todo dia! 🐥

#musicainfantil #shorts #chefbolinha
```

**Tags (copiar):**

```
musiquinha infantil, música para bebê, música para crianças, desenho infantil, chef bolinha, sopa mágica, sopa, comida, cozinha infantil
```

## 9. Checklist (ao aplicar os metadados novos)

- [ ] Título, descrição, tags e playlist atualizados
- [ ] "Sim, é conteúdo para crianças" mantido
- [ ] Conteúdo alterado/sintético marcado
- [ ] Verificar no Studio → Conteúdo → Restrições

## 10. Pós-publicação

| Métrica | 24h (29/09) | 7 dias (05/10) |
|---|---|---|
| Visualizações | | |
| Duração média da visualização | | |
| % média visualizada | | |
| Deslizaram vs. assistiram (Shorts) | | |
| Inscritos ganhos | | |
| Restrições (Studio) | | — |

## Aprendizados para os próximos episódios

1. **Gancho sem o personagem no 1º segundo.** O vídeo abre na panela vazia e o Bolinha só aparece por volta de 3s. A causa estava no prompt: "a burst of rainbow sparkles explodes... and Bolinha pops out" pediu a explosão antes do personagem, e o Veo seguiu a ordem. No feed de Shorts, quem desliza decide no 1º segundo. **Regra:** gerar antes um `frame_inicio.png` com o Bolinha já em cena, e a 1ª frase da ação descreve o personagem em movimento.
2. **Loop parcial.** O fim (panela brilhando com o Bolinha coberto de brilhos) não bate com o começo (panela vazia sem personagem). A emenda existe pelo brilho, mas não é a mesma pose nem a mesma cena. **Regra:** o último clipe termina na **mesma pose e enquadramento** do 1º frame (usar `frame_inicio.png` como alvo).
3. **Sem musiquinha cantada.** Só duas falas e um jingle, sem refrão para a criança repetir nem melodia que "gruda". **Regra:** a partir do ep02, todo episódio tem letra original cantada, com refrão de 2 a 4 versos repetido pelo menos 2x.
4. **Conceito igual ao do tutorial.** "Sopa mágica de um mini chef" é o exemplo do TikTok de referência. **Regra:** os próximos temas partem da lista em `series-e-calendario.md`, não de exemplos de tutoriais.
5. **Marca d'água de terceiros.** A imagem de referência veio do Dreamina com marca d'água. Desta vez ela não passou para o vídeo, mas não há garantia. **Regra:** usar a referência limpa gerada no Gemini (ver `personagem.md`).
6. **Limite de 2 gerações por dia.** Cada geração dá ~10s, e a continuação devolve o vídeo inteiro de 20s. **Regra:** episódios de 20s em 2 gerações, com o roteiro dividido em 0–10s e 10–20s.
