# Gerar os vídeos pela API do Gemini (Veo)

Com a API, o Claude gera o 1º frame e o vídeo de um episódio sozinho, sem você copiar e colar prompts no app do Gemini. Ele também baixa os arquivos e já monta o episódio. Este guia mostra o que **você** precisa fazer uma vez e quanto custa.

> Preços e regras conferidos em 01/10/2026 em [ai.google.dev/gemini-api/docs/pricing](https://ai.google.dev/gemini-api/docs/pricing), [.../billing](https://ai.google.dev/gemini-api/docs/billing) e [.../veo](https://ai.google.dev/gemini-api/docs/veo). Eles mudam com frequência. Confira antes de comprar créditos.

---

## 1. O que muda em relação ao app do Gemini

| | App do Gemini (hoje) | API (Google AI Studio) |
|---|---|---|
| Quem gera | Você, copiando e colando os prompts | O Claude, por script |
| Limite | 2 gerações por dia | Sem limite diário fixo, paga por segundo |
| Pagamento | Assinatura | Créditos pré-pagos, por segundo de vídeo |
| Plano grátis | Incluso na assinatura | **O Veo não tem plano grátis na API** |
| Duração | ~10s + continuação até 20s | **8s** + extensões de **7s** cada (8 → 15 → 22s, cortado em 20s) |
| Resolução | 720×1280 | 720×1280 (a extensão só funciona em 720p, a mesma resolução do ep03) |

**Atenção:** a assinatura do app do Gemini **não** dá crédito na API. Os US$ 300 de boas-vindas do Google Cloud também **não** servem para o Gemini API desde março de 2026. É uma cobrança separada.

## 2. Passo a passo (só você pode fazer)

### 2.1 Criar a chave da API

1. Entre em [aistudio.google.com](https://aistudio.google.com) com a conta Google do canal.
2. Menu **Get API key** → **Create API key**. Ele cria um projeto ("Free Tier") junto com a chave.
3. Copie a chave (começa com `AIza...`). **Não cole a chave no chat nem em nenhum arquivo do repositório.**

### 2.2 Ativar o pagamento com créditos pré-pagos

1. No AI Studio, abra **API keys** (ou **Projects**), ache o projeto e clique em **Set up billing**.
2. Escolha o país (Brasil), aceite os termos e preencha os dados e o cartão. Precisa ser um cartão internacional, e o IOF é cobrado à parte.
3. Em **plano de cobrança**, escolha **Prepay** (pré-pago). Assim você só gasta o que colocou, sem surpresa na fatura.
   - Compra mínima: **US$ 5**. Máxima: US$ 5.000.
4. Compre os créditos (sugestão na seção 3).
5. **Deixe a recarga automática (auto-reload) desligada** durante os testes.
6. Opcional: na página **Spend**, defina um limite de gasto no projeto (por exemplo, US$ 10).

### 2.3 Deixar a chave disponível para o Claude

No PowerShell (uma vez só):

```
setx GEMINI_API_KEY "cole-a-chave-aqui"
```

Depois **feche e abra de novo** o VS Code (ou o terminal do Claude Code) para ele enxergar a variável. A chave fica só no Windows, fora do repositório e fora do OneDrive.

### 2.4 Me avisar

Diga "a chave está configurada". Eu cuido do resto:

- instalar a biblioteca `google-genai` no Python;
- criar o `scripts/gerar_video.py`, que lê os prompts do `episodio.md`, gera o 1º frame e o vídeo e baixa tudo em `imagens/` e `videos/`;
- **mostrar o custo estimado e pedir sua confirmação antes de cada geração paga.**

## 3. Quanto custa

Preço por segundo de vídeo gerado, com áudio incluso:

| Modelo | 720p (o que usamos) |
|---|---|
| Veo 3.1 (padrão, melhor qualidade) | US$ 0,40/s |
| Veo 3.1 Fast | US$ 0,10/s |
| Veo 3.1 Lite | US$ 0,05/s *(não aceita imagens de referência; ainda vou confirmar se faz extensão)* |

Imagem do 1º frame (Nano Banana 2, 1K): cerca de US$ 0,07 cada.

### Um episódio de 20s (como o ep03)

Uma tentativa é: 1º frame + geração de 8s + 2 extensões de 7s = **22s de vídeo**.

| Modelo | 1 tentativa | Com folga (3 tentativas) |
|---|---|---|
| **Fast** | ~US$ 2,30 | ~US$ 7 |
| Padrão | ~US$ 9 | ~US$ 27 |

Considerei que cada extensão cobra só os 7s novos. Confiro isso no painel de gastos depois da primeira geração.

### Sugestão para o nosso teste

**Compre US$ 10 e use o Veo 3.1 Fast.** Isso dá para cerca de 4 tentativas completas de um episódio. Se a qualidade do Fast não ficar boa, gastamos uma tentativa com o modelo padrão (~US$ 9) para comparar antes de colocar mais crédito.

## 4. O que precisa mudar nos roteiros

- **Tempos:** a API gera em blocos de 8s + 7s + 7s, e não 10s + 10s. As falas e as ações dos prompts passam a ser divididas em `0–8s`, `8–15s` e `15–22s`, e o vídeo é cortado em 20s na montagem. Ajusto o `_modelo` e a skill quando você aprovar a API.
- **Continuidade:** a extensão continua o próprio vídeo, e não um print do último frame, então a emenda tende a sair melhor que no app.
- **Personagens:** a API aceita o 1º frame e até 3 imagens de referência, mas as referências não funcionam junto com a extensão. Por isso, o 1º frame continua sendo a âncora visual, como já fazemos.
- **Vozes:** a receita de tom da Nuvem (ver [`personagem.md`](personagem.md#voz-nas-falas-do-veo)) continua valendo na montagem.

## 5. Cuidados

- Os vídeos ficam só **2 dias** no servidor do Google. O script baixa na hora.
- Uma geração leva de alguns segundos a ~6 minutos.
- Se a chave vazar, apague-a no AI Studio e crie outra. Com o pré-pago sem recarga automática, o prejuízo máximo é o saldo que estiver lá.
