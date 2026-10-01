# Chef Bolinha: bíblia do personagem

Referência visual oficial: [`personagem/bolinha_referencia.png`](personagem/bolinha_referencia.png): corpo inteiro, de frente, fundo creme, sem marca d'água. É a imagem que se anexa nos prompts.

Ficha com detalhes (estrela do chapéu, olho, laço do lenço, bolso do avental): [`personagem/bolinha_ficha.png`](personagem/bolinha_ficha.png). Serve para consulta; não anexe nos prompts, porque os círculos de detalhe podem aparecer no frame gerado.

---

## Aparência fixa (PT-BR)

- **Espécie:** pintinho bebê, pequeno e redondinho (daí o nome "Bolinha").
- **Penas:** amarelo-vivo, bem fofas e macias.
- **Olhos:** grandes, brilhantes, azul-esverdeado (turquesa), com cílios.
- **Bochechas:** rosadas.
- **Bico e pés:** laranja, pequenos.
- **Chapéu:** de chef, branco e bem fofo (alto e "estufado"), com uma **estrelinha vermelha** na faixa da frente.
- **Lenço:** vermelho, amarrado no pescoço com um laço.
- **Avental:** azul-claro com **bolinhas brancas** e um bolso na frente.
- **Estilo:** animação 3D fofa, acabamento suave, cores pastel, luz quente e macia.

## Prompt âncora (EN) — colar em TODO prompt de vídeo

```
Chef Bolinha: a tiny, round, fluffy baby chick with bright yellow fluffy feathers, big glossy turquoise-blue eyes with eyelashes, rosy pink cheeks, a small orange beak and tiny orange feet. He wears a tall, puffy white chef's hat with a small red star on the front band, a red neckerchief tied in a bow, and a light-blue apron with white polka dots and a front pocket. Cute 3D animated style, soft Pixar-like rendering, pastel colors, warm soft lighting. Same character design in every shot.
```

## Personalidade

- Curioso, animado e gentil. Adora cozinhar e fazer amigos (animais, frutas, objetos da cozinha).
- Resolve tudo com alegria. Nunca fica bravo nem assusta ninguém.
- Faz pequenas trapalhadas engraçadas (bigode de leite, farinha no bico), mas sem se machucar.

## Bordão

**"Pi-piu, que delícia!"**: usado quando prova algo ou quando algo dá certo. Não precisa aparecer em todo episódio. Use em no máximo metade deles, para não virar fórmula.

## Voz (tom e estilo do canto)

- Voz **aguda e doce de criança pequena**, clara e afinada, sem exagero "de esquilo".
- Canto alegre, em andamento médio, sem vibrato, com dicção bem clara (o público tem de 1 a 4 anos).
- **Consistência:** a voz é gerada no **Suno**. Depois do 1º episódio cantado (ep02), salve a voz como **Persona "Chef Bolinha"** no Suno e reutilize em todos os episódios.
- Descrição para o Suno: `cute high-pitched young child voice, sweet and clear, Brazilian Portuguese, cheerful, no vibrato`

### Voz nas falas do Veo

Nos episódios educativos, as falas vêm do Veo, que cria uma voz nova a cada geração e costuma dar a mesma voz ao Bolinha e ao amigo.

- **Amostra oficial:** [`personagem/vozes/bolinha_voz.wav`](personagem/vozes/bolinha_voz.wav) (falas do ep03). A da Nuvem fica em [`personagem/vozes/nuvem_voz.wav`](personagem/vozes/nuvem_voz.wav).
- **Receita (ep03):** o Bolinha fica sem ajuste e a Nuvem desce **3 semitons**, com o timbre preservado. A sincronia com a boca não muda.
- **Como aplicar:** anote os trechos de cada personagem (o `silencedetect` do ffmpeg mostra as pausas entre as falas) e rode, na pasta `videos/`, trocando os tempos de `N` (falas da Nuvem):

  ```
  N="between(t,1.95,3.6)+between(t,6.3,8.1)+between(t,10.0,11.8)+between(t,13.9,16.5)"
  ffmpeg -i completo_20s.mp4 -filter_complex "[0:a]asplit=2[o][n];[n]rubberband=pitch=0.8409:formant=preserved:pitchq=quality,volume='if($N,1,0)':eval=frame[nn];[o]volume='if($N,0,1)':eval=frame[oo];[nn][oo]amix=inputs=2:normalize=0[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k completo_vozes.mp4
  ```

- Ouça o resultado junto com as amostras oficiais. O timbre ainda pode variar um pouco de episódio para episódio. Para uma voz idêntica sempre, o próximo passo é uma troca de voz (ElevenLabs Voice Changer ou um modelo RVC treinado com essas amostras).

## Paleta de cores (aprox.)

| Elemento | Cor | Hex aprox. |
|---|---|---|
| Penas | Amarelo-vivo | `#F7CB3D` |
| Chapéu | Branco | `#F8F6F2` |
| Estrela e lenço | Vermelho | `#D8433A` |
| Avental | Azul-claro | `#AFD6E8` |
| Bico e pés | Laranja | `#F29A2E` |
| Olhos | Turquesa | `#2E9DB0` |

Cenários em tons pastel (rosa, menta, creme) combinam com a paleta. Evite fundos escuros ou saturados demais.

## O que NUNCA mudar

- Espécie, cor das penas e proporção (pequeno e redondo).
- Chapéu de chef com estrela vermelha, lenço vermelho e avental azul de bolinhas. Um acessório temático pode ser **somado** (galochas, cachecol), mas nunca substitui o uniforme.
- Olhos turquesa e bochechas rosadas.
- Tom: nada assustador, triste demais, violento ou perigoso (fogo alto, facas, quedas).
- Nome: sempre "Chef Bolinha".

---

## Referência no Gemini

A referência atual foi gerada assim em 2026-09-30, substituindo a antiga com marca d'água "Dreamina AI" (que continua no histórico do git). Use para refazer se precisar.

1. Abra o **Gemini** → modo de criação de imagem.
2. Anexe `personagem/bolinha_referencia.png`.
3. Cole o prompt:

   ```
   Recreate the chick in this image as a clean character reference sheet. Vertical 9:16, plain soft cream background.
   Center: full body, front view, standing on his two tiny orange feet, little wings slightly open at his sides, gentle happy smile, centered and large in the frame.
   Keep every detail identical: a tiny, round, fluffy baby chick with bright yellow fluffy feathers, big glossy turquoise-blue eyes with eyelashes, rosy pink cheeks, a small orange beak and tiny orange feet. He wears a tall, puffy white chef's hat with a small red star on the front band, a red neckerchief tied in a bow, and a light-blue apron with white polka dots and a front pocket.
   Around him, four round close-up detail circles, one in each corner, not overlapping the full body: top-left the red star on the chef's hat band, top-right one turquoise-blue eye with eyelashes, bottom-left the red neckerchief bow, bottom-right the apron front pocket with white polka dots.
   Cute 3D Pixar-like style, soft lighting. Remove any watermark, logo or label from the original image. No text, no logos, no watermark.
   ```

4. Gere 2 ou 3 variações e escolha a mais fiel (compare chapéu, estrela, lenço e avental com a original).
5. Salve a folha inteira em PNG como `personagem/bolinha_ficha.png`.
6. Recorte só o corpo inteiro, sem os círculos (se sobrar borda de círculo nos cantos, pinte com a cor do fundo), e salve como `personagem/bolinha_referencia.png`.
7. Opcional: gere também uma **visão de lado** e uma **de costas** com o mesmo prompt, trocando `front view` por `side view` ou `back view`. Isso ajuda o Veo em cenas com o personagem de lado.
