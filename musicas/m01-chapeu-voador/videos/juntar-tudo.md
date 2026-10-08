# m01: O Chapéu Voador, juntar tudo

## 1. Música (antes dos vídeos)

1. Suno → Custom → Persona "Chef Bolinha".
2. Preencher os campos (título, excluir estilo, gênero vocal, duração, modo Max, estranheza, variedade) e colar **Style** e **Lyrics**, tudo da seção 3 do [musica.md](../musica.md).
3. Escolher a versão com dicção clara, entre 2 e 4 min.
4. Salvar: `musicas/m01-chapeu-voador/musica.wav`
5. Pedir ao Claude: **"mapeia a m01"** (gera o `mapa.yaml`).

## 2. Vídeos (2 por dia)

| Dia | Vídeo | Feito |
|---|---|---|
| 1 | [c01 Piquenique](c01-piquenique/c01-piquenique.md) | [x] |
| 1 | [c02 O vento](c02-o-vento/c02-o-vento.md) | [x] |
| 2 | [c03 Correria](c03-correria/c03-correria.md) | [ ] |
| 2 | [c04 Boing!](c04-boing/c04-boing.md) | [ ] |
| 3 | [c06 Cadê?](c06-cade/c06-cade.md) | [ ] |
| 3 | [c07 Chef Nuvem](c07-chef-nuvem/c07-chef-nuvem.md) | [ ] |
| 4 | [c08 De volta](c08-de-volta/c08-de-volta.md) | [ ] |
| 4 | [c09 Festa](c09-festa/c09-festa.md) | [ ] |
| 5 (opcional) | [c05 Correria 2](c05-correria-2/c05-correria-2.md) | [ ] |

Sem o c05, o Refrão 2 usa o c03 espelhado.

## 3. Montar (rodar todo dia)

```
python scripts/montar_musica.py musicas/m01-chapeu-voador
```

- Saída: `musicas/m01-chapeu-voador/montagem/final.mp4` e `relatorio.md`
- Vídeo que falta aparece como tela cinza.

## 4. Antes de publicar

- [ ] Assistir o `final.mp4` inteiro: nada deformado, nenhuma tela cinza
- [ ] Ler o `relatorio.md`
- [ ] Publicar com os dados da seção 7 do [musica.md](../musica.md)
