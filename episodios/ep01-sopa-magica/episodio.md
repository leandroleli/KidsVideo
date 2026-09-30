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
| Melodia | **Sem música cantada**: só falas e um jingle de fundo |
| Andamento | — |
| Instrumento principal | Jingle de fundo |
| Cenário | Cozinha pastel (paredes creme, armários menta, prateleira rosa com bules), panela turquesa no fogão |
| Estrutura musical | Nenhuma (falas soltas) |
| Momento surpresa | A panela solta brilhos e bolhas de sabão coloridas (a sopa "fica mágica") |

## 3. Roteiro por cena

Reconstruído a partir dos frames do vídeo. As falas foram transcritas com Whisper (`medium`, pt).

| Tempo | Cena (visual) | Áudio / fala |
|---|---|---|
| 0:00–0:01 | Panela vazia no fogão, **sem o personagem** | Jingle |
| 0:01–0:03 | Explosão de brilhos coloridos saindo da panela | Jingle |
| 0:03–0:06 | Close do Bolinha, animado, olhando para a câmera | **"Ei! Olha a sopa mágica!"** (0:00–0:04 na transcrição) |
| 0:06–0:12 | Bolinha mexe a sopa; bolhas de sabão coloridas flutuam | Jingle |
| 0:12–0:16 | Bolinha de olhos fechados, mexendo feliz | Jingle |
| 0:16–0:18 | Bolinha prova a sopa na colher | **"Hum, de novo!"** |
| 0:18–0:20 | A panela brilha forte; brilhos cobrem o Bolinha | Jingle |

## 4. Letra

Não tem letra cantada. Falas:

```
Ei! Olha a sopa mágica!
Hum, de novo!
```

## 5–7. Geração, música e montagem

Gerado antes da adoção deste modelo (clipes do Dreamina, com a imagem de referência que tem a marca d'água "Dreamina AI"). Sem registro dos prompts usados.

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

1. **Gancho sem o personagem no 1º segundo.** O vídeo abre na panela vazia e o Bolinha só aparece por volta de 3s. No feed de Shorts, quem desliza decide no 1º segundo. **Regra:** o 1º frame já mostra o Bolinha em ação, com som forte.
2. **Loop parcial.** O fim (panela brilhando com o Bolinha coberto de brilhos) não bate com o começo (panela vazia sem personagem). A emenda existe pelo brilho, mas não é a mesma pose nem a mesma cena. **Regra:** o último clipe termina na **mesma pose e enquadramento** do 1º frame (usar `frame_inicio.png` como alvo).
3. **Sem musiquinha cantada.** Só duas falas e um jingle, sem refrão para a criança repetir nem melodia que "gruda". **Regra:** a partir do ep02, todo episódio tem letra original cantada, com refrão de 2 a 4 versos repetido pelo menos 2x.
4. **Conceito igual ao do tutorial.** "Sopa mágica de um mini chef" é o exemplo do TikTok de referência. **Regra:** os próximos temas partem da lista em `series-e-calendario.md`, não de exemplos de tutoriais.
5. **Marca d'água de terceiros.** A imagem de referência veio do Dreamina com marca d'água. **Regra:** usar a referência limpa gerada no Gemini (ver `personagem.md`).
