# c03: Correria

**Dia 2** · Trecho: Refrão 1 · 0:30–0:50

## 1. Imagem do 1º quadro

Gemini → criar imagem → **16:9**. Anexar:

- [`bolinha_referencia.png`](../../../../personagem/bolinha_referencia.png)
- [`vaquinha-nuvem_referencia.png`](../../../../personagem/amigos/vaquinha-nuvem_referencia.png)
- [`sementinha-morango_referencia.png`](../../../../personagem/amigos/sementinha-morango_referencia.png)

```
Horizontal 16:9 image, cute 3D Pixar-like children's cartoon, pastel colors, warm morning light. Keep the three characters exactly like the attached reference images. A wide view of a soft green grassy hill on a sunny pastel farm, fluffy clouds in a light-blue sky, a few sunflowers. High in the sky on the right, a tall white chef's hat with a small red star floats in the air. On the left side of the hill, running toward the right with happy faces: Nuvem the baby cow, Chef Bolinha the yellow chick without his hat, and Sementinha the strawberry hopping. Wide shot. No text, no logos, no watermark.
```

Salvar: `musicas/m01-chapeu-voador/imagens/c03_inicio.png`

## 2. Vídeo, Parte A (0–10s)

Gemini → Vídeo. Anexar `c03_inicio.png`.

```
Horizontal 16:9 children's cartoon. Cute 3D animated style, soft Pixar-like rendering, pastel colors, warm soft morning light. Static camera, wide shot, every character fully visible. No talking, no singing, no text on screen. Same character designs in every shot.
Setting: a cute pastel farm on a sunny morning: a small red-and-cream wooden barn with a big round window, a soft green grassy hill, a white wooden fence, a few sunflowers, fluffy clouds in a light-blue sky, and a red-and-white checkered picnic blanket on the grass with a round golden corn cake on a plate.
Sizes: Nuvem is the biggest, Chef Bolinha is small and round, Sementinha is about the size of Bolinha's head.
Chef Bolinha: a tiny, round, fluffy baby chick with bright yellow fluffy feathers, big glossy turquoise-blue eyes with eyelashes, rosy pink cheeks, a small orange beak and tiny orange feet. He wears a tall, puffy white chef's hat with a small red star on the front band, a red neckerchief tied in a bow, and a light-blue apron with white polka dots and a front pocket.
Nuvem the cow: a small, cute, chubby baby cow with white fur covered in soft cloud-shaped light-gray spots (one around her eye), a fluffy white tuft of fur on top of her head, big glossy dark-brown eyes with eyelashes, a big rounded pink snout, rosy pink cheeks, white ears with pink insides, tiny rounded cream-colored horns, and a small golden bell on a blue ribbon around her neck.
Sementinha the strawberry: a small, plump, rounded, glossy bright-red strawberry character covered all over with tiny golden-yellow seeds on the outside of his body, with a fresh green leafy cap on top like a little crown and a short curly green stem, big glossy black eyes, rosy pink cheeks, a small happy smile, and tiny thin light-green arms and legs.

Start exactly from the attached image. Chef Bolinha has no hat on his head. The white chef's hat floats slowly through the sky from left to right. Nuvem the cow, Chef Bolinha the chick and Sementinha the strawberry run happily across the green hill after it, from left to right, laughing with open smiles. Sementinha bounces with small hops. Smooth, slow side-tracking camera.
```

Salvar: `musicas/m01-chapeu-voador/clipes/c03a.mp4`

## 3. Vídeo, Parte B (10–20s)

Tirar o último quadro da Parte A:

```
ffmpeg -sseof -0.1 -i musicas/m01-chapeu-voador/clipes/c03a.mp4 -frames:v 1 musicas/m01-chapeu-voador/imagens/c03a_ultimo.png
```

Gemini → Vídeo. Anexar `c03a_ultimo.png`.

```
Horizontal 16:9 children's cartoon. Cute 3D animated style, soft Pixar-like rendering, pastel colors, warm soft morning light. Static camera, wide shot, every character fully visible. No talking, no singing, no text on screen. Same character designs in every shot.
Setting: a cute pastel farm on a sunny morning: a small red-and-cream wooden barn with a big round window, a soft green grassy hill, a white wooden fence, a few sunflowers, fluffy clouds in a light-blue sky, and a red-and-white checkered picnic blanket on the grass with a round golden corn cake on a plate.
Sizes: Nuvem is the biggest, Chef Bolinha is small and round, Sementinha is about the size of Bolinha's head.
Chef Bolinha: a tiny, round, fluffy baby chick with bright yellow fluffy feathers, big glossy turquoise-blue eyes with eyelashes, rosy pink cheeks, a small orange beak and tiny orange feet. He wears a tall, puffy white chef's hat with a small red star on the front band, a red neckerchief tied in a bow, and a light-blue apron with white polka dots and a front pocket.
Nuvem the cow: a small, cute, chubby baby cow with white fur covered in soft cloud-shaped light-gray spots (one around her eye), a fluffy white tuft of fur on top of her head, big glossy dark-brown eyes with eyelashes, a big rounded pink snout, rosy pink cheeks, white ears with pink insides, tiny rounded cream-colored horns, and a small golden bell on a blue ribbon around her neck.
Sementinha the strawberry: a small, plump, rounded, glossy bright-red strawberry character covered all over with tiny golden-yellow seeds on the outside of his body, with a fresh green leafy cap on top like a little crown and a short curly green stem, big glossy black eyes, rosy pink cheeks, a small happy smile, and tiny thin light-green arms and legs.

Start exactly from the attached image and continue the same scene. Chef Bolinha has no hat on his head. The white chef's hat makes a slow loop in the sky above the three friends. Nuvem the cow, Chef Bolinha the chick and Sementinha the strawberry stop, look up and turn around in a little circle following the hat, then start running again to the right, laughing.
```

## 4. Salvar

- Vídeo de 20s: `musicas/m01-chapeu-voador/clipes/c03.mp4`
- Apagar `c03a.mp4` e `c03a_ultimo.png`
- Marcar `[x]` no [juntar-tudo.md](../juntar-tudo.md)
