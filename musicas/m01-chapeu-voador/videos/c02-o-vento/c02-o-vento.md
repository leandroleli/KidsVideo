# c02: O vento

**Dia 1** · Trecho: Pré-refrão 1 (e a 2ª metade no Pré-refrão 2) · 0:20–0:30 / 1:10–1:17

## 1. Imagem do 1º quadro

Gemini → criar imagem → **16:9**. Anexar:

- [`bolinha_referencia.png`](../../../../personagem/bolinha_referencia.png)
- [`vaquinha-nuvem_referencia.png`](../../../../personagem/amigos/vaquinha-nuvem_referencia.png)
- [`sementinha-morango_referencia.png`](../../../../personagem/amigos/sementinha-morango_referencia.png)

```
Horizontal 16:9 image, cute 3D Pixar-like children's cartoon, pastel colors, warm morning light. Keep the three characters exactly like the attached reference images. A sunny pastel farm with a red-and-cream barn, green hill, white fence and sunflowers. Around a red-and-white checkered picnic blanket with a round golden corn cake: Nuvem the baby cow on the left, Chef Bolinha the yellow chick in the middle wearing his tall white chef's hat, Sementinha the strawberry on the right. All three smile. Wide shot. No text, no logos, no watermark.
```

Salvar: `musicas/m01-chapeu-voador/imagens/c02_inicio.png`

## 2. Vídeo, Parte A (0–10s)

Gemini → Vídeo. Anexar `c02_inicio.png`.

```
Horizontal 16:9 children's cartoon. Cute 3D animated style, soft Pixar-like rendering, pastel colors, warm soft morning light. Static camera, wide shot, every character fully visible. No talking, no singing, no text on screen. Same character designs in every shot.
Setting: a cute pastel farm on a sunny morning: a small red-and-cream wooden barn with a big round window, a soft green grassy hill, a white wooden fence, a few sunflowers, fluffy clouds in a light-blue sky, and a red-and-white checkered picnic blanket on the grass with a round golden corn cake on a plate.
Sizes: Nuvem is the biggest, Chef Bolinha is small and round, Sementinha is about the size of Bolinha's head.
Chef Bolinha: a tiny, round, fluffy baby chick with bright yellow fluffy feathers, big glossy turquoise-blue eyes with eyelashes, rosy pink cheeks, a small orange beak and tiny orange feet. He wears a tall, puffy white chef's hat with a small red star on the front band, a red neckerchief tied in a bow, and a light-blue apron with white polka dots and a front pocket.
Nuvem the cow: a small, cute, chubby baby cow with white fur covered in soft cloud-shaped light-gray spots (one around her eye), a fluffy white tuft of fur on top of her head, big glossy dark-brown eyes with eyelashes, a big rounded pink snout, rosy pink cheeks, white ears with pink insides, tiny rounded cream-colored horns, and a small golden bell on a blue ribbon around her neck.
Sementinha the strawberry: a small, plump, rounded, glossy bright-red strawberry character covered all over with tiny golden-yellow seeds on the outside of his body, with a fresh green leafy cap on top like a little crown and a short curly green stem, big glossy black eyes, rosy pink cheeks, a small happy smile, and tiny thin light-green arms and legs.

Start exactly from the attached image. A gentle breeze starts blowing from the left: the grass and the sunflowers sway softly and the corners of the picnic blanket flutter. Chef Bolinha's tall white chef's hat lifts off his head and floats slowly upward. Chef Bolinha, in the middle, touches the top of his head with his wing, surprised. Nuvem on the left and Sementinha on the right look up with big round surprised eyes.
```

Salvar: `musicas/m01-chapeu-voador/clipes/c02a.mp4`

## 3. Vídeo, Parte B (10–20s)

Tirar o último quadro da Parte A:

```
ffmpeg -sseof -0.1 -i musicas/m01-chapeu-voador/clipes/c02a.mp4 -frames:v 1 musicas/m01-chapeu-voador/imagens/c02a_ultimo.png
```

Gemini → Vídeo. Anexar `c02a_ultimo.png`.

```
Horizontal 16:9 children's cartoon. Cute 3D animated style, soft Pixar-like rendering, pastel colors, warm soft morning light. Static camera, wide shot, every character fully visible. No talking, no singing, no text on screen. Same character designs in every shot.
Setting: a cute pastel farm on a sunny morning: a small red-and-cream wooden barn with a big round window, a soft green grassy hill, a white wooden fence, a few sunflowers, fluffy clouds in a light-blue sky, and a red-and-white checkered picnic blanket on the grass with a round golden corn cake on a plate.
Sizes: Nuvem is the biggest, Chef Bolinha is small and round, Sementinha is about the size of Bolinha's head.
Chef Bolinha: a tiny, round, fluffy baby chick with bright yellow fluffy feathers, big glossy turquoise-blue eyes with eyelashes, rosy pink cheeks, a small orange beak and tiny orange feet. He wears a tall, puffy white chef's hat with a small red star on the front band, a red neckerchief tied in a bow, and a light-blue apron with white polka dots and a front pocket.
Nuvem the cow: a small, cute, chubby baby cow with white fur covered in soft cloud-shaped light-gray spots (one around her eye), a fluffy white tuft of fur on top of her head, big glossy dark-brown eyes with eyelashes, a big rounded pink snout, rosy pink cheeks, white ears with pink insides, tiny rounded cream-colored horns, and a small golden bell on a blue ribbon around her neck.
Sementinha the strawberry: a small, plump, rounded, glossy bright-red strawberry character covered all over with tiny golden-yellow seeds on the outside of his body, with a fresh green leafy cap on top like a little crown and a short curly green stem, big glossy black eyes, rosy pink cheeks, a small happy smile, and tiny thin light-green arms and legs.

Start exactly from the attached image and continue the same scene. The white chef's hat floats higher and drifts slowly to the right across the light-blue sky, tumbling gently. Chef Bolinha, in the middle, points at the hat with his wing. Nuvem on the left and Sementinha on the right turn their heads to follow the hat. The hat floats away over the green hill on the right.
```

## 4. Salvar

- Vídeo de 20s: `musicas/m01-chapeu-voador/clipes/c02.mp4`
- Apagar `c02a.mp4` e `c02a_ultimo.png`
- Marcar `[x]` no [juntar-tudo.md](../juntar-tudo.md)
