# c09: Festa

**Dia 4** · Trecho: Refrão final · 2:37–2:57

## 1. Imagem do 1º quadro

Gemini → criar imagem → **16:9**. Anexar:

- [`bolinha_referencia.png`](../../../../personagem/bolinha_referencia.png)
- [`vaquinha-nuvem_referencia.png`](../../../../personagem/amigos/vaquinha-nuvem_referencia.png)
- [`sementinha-morango_referencia.png`](../../../../personagem/amigos/sementinha-morango_referencia.png)

```
Horizontal 16:9 image, cute 3D Pixar-like children's cartoon, pastel colors, warm morning light. Keep the three characters exactly like the attached reference images. A sunny pastel farm with the barn, green hill, sunflowers and a red-and-white checkered picnic blanket. Nuvem the baby cow on the left, Chef Bolinha the yellow chick in the middle wearing his tall white chef's hat, and Sementinha the strawberry on the right, standing side by side in front of the blanket, facing the camera, ready to dance with big smiles. Wide shot. No text, no logos, no watermark.
```

Salvar: `musicas/m01-chapeu-voador/imagens/c09_inicio.png`

## 2. Vídeo, Parte A (0–10s)

Gemini → Vídeo. Anexar `c09_inicio.png`.

```
Horizontal 16:9 children's cartoon. Cute 3D animated style, soft Pixar-like rendering, pastel colors, warm soft morning light. Static camera, wide shot, every character fully visible. No talking, no singing, no text on screen. Same character designs in every shot.
Setting: a cute pastel farm on a sunny morning: a small red-and-cream wooden barn with a big round window, a soft green grassy hill, a white wooden fence, a few sunflowers, fluffy clouds in a light-blue sky, and a red-and-white checkered picnic blanket on the grass with a round golden corn cake on a plate.
Sizes: Nuvem is the biggest, Chef Bolinha is small and round, Sementinha is about the size of Bolinha's head.
Chef Bolinha: a tiny, round, fluffy baby chick with bright yellow fluffy feathers, big glossy turquoise-blue eyes with eyelashes, rosy pink cheeks, a small orange beak and tiny orange feet. He wears a tall, puffy white chef's hat with a small red star on the front band, a red neckerchief tied in a bow, and a light-blue apron with white polka dots and a front pocket.
Nuvem the cow: a small, cute, chubby baby cow with white fur covered in soft cloud-shaped light-gray spots (one around her eye), a fluffy white tuft of fur on top of her head, big glossy dark-brown eyes with eyelashes, a big rounded pink snout, rosy pink cheeks, white ears with pink insides, tiny rounded cream-colored horns, and a small golden bell on a blue ribbon around her neck.
Sementinha the strawberry: a small, plump, rounded, glossy bright-red strawberry character covered all over with tiny golden-yellow seeds on the outside of his body, with a fresh green leafy cap on top like a little crown and a short curly green stem, big glossy black eyes, rosy pink cheeks, a small happy smile, and tiny thin light-green arms and legs.

Start exactly from the attached image. Chef Bolinha is wearing his white chef's hat. The three friends dance happily to the beat: Nuvem on the left sways her head side to side so her golden bell swings, Chef Bolinha in the middle flaps his little wings and hops, Sementinha on the right bounces up and down. Sunflowers sway in the breeze.
```

Salvar: `musicas/m01-chapeu-voador/clipes/c09a.mp4`

## 3. Vídeo, Parte B (10–20s)

Tirar o último quadro da Parte A:

```
ffmpeg -sseof -0.1 -i musicas/m01-chapeu-voador/clipes/c09a.mp4 -frames:v 1 musicas/m01-chapeu-voador/imagens/c09a_ultimo.png
```

Gemini → Vídeo. Anexar `c09a_ultimo.png`.

```
Horizontal 16:9 children's cartoon. Cute 3D animated style, soft Pixar-like rendering, pastel colors, warm soft morning light. Static camera, wide shot, every character fully visible. No talking, no singing, no text on screen. Same character designs in every shot.
Setting: a cute pastel farm on a sunny morning: a small red-and-cream wooden barn with a big round window, a soft green grassy hill, a white wooden fence, a few sunflowers, fluffy clouds in a light-blue sky, and a red-and-white checkered picnic blanket on the grass with a round golden corn cake on a plate.
Sizes: Nuvem is the biggest, Chef Bolinha is small and round, Sementinha is about the size of Bolinha's head.
Chef Bolinha: a tiny, round, fluffy baby chick with bright yellow fluffy feathers, big glossy turquoise-blue eyes with eyelashes, rosy pink cheeks, a small orange beak and tiny orange feet. He wears a tall, puffy white chef's hat with a small red star on the front band, a red neckerchief tied in a bow, and a light-blue apron with white polka dots and a front pocket.
Nuvem the cow: a small, cute, chubby baby cow with white fur covered in soft cloud-shaped light-gray spots (one around her eye), a fluffy white tuft of fur on top of her head, big glossy dark-brown eyes with eyelashes, a big rounded pink snout, rosy pink cheeks, white ears with pink insides, tiny rounded cream-colored horns, and a small golden bell on a blue ribbon around her neck.
Sementinha the strawberry: a small, plump, rounded, glossy bright-red strawberry character covered all over with tiny golden-yellow seeds on the outside of his body, with a fresh green leafy cap on top like a little crown and a short curly green stem, big glossy black eyes, rosy pink cheeks, a small happy smile, and tiny thin light-green arms and legs.

Start exactly from the attached image and continue the same scene. Chef Bolinha is wearing his white chef's hat. The three friends hold hands and turn in a small happy circle around the picnic blanket, then stop side by side facing the camera: Nuvem on the left, Chef Bolinha in the middle, Sementinha on the right. They finish with a cheerful pose, wings and arms up.
```

## 4. Salvar

- Vídeo de 20s: `musicas/m01-chapeu-voador/clipes/c09.mp4`
- Apagar `c09a.mp4` e `c09a_ultimo.png`
- Marcar `[x]` no [juntar-tudo.md](../juntar-tudo.md)
