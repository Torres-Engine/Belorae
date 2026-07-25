# DEPLOY.md — Colocar o site no ar (passo a passo para iniciante)

## O que é

"Deploy" é publicar o site na internet, com um link que qualquer pessoa pode acessar. Vamos usar **GitHub Pages** — hospedagem gratuita que já explica em `docs/ARCHITECTURE.md` por que foi escolhida.

## Passo 1 — Criar conta no GitHub

1. Acesse [github.com](https://github.com) e crie uma conta gratuita (se ainda não tiver).

## Passo 2 — Criar um repositório

1. No GitHub, clique em **New repository** (botão verde).
2. Nome: `belorae-site` (ou outro nome, sem espaços).
3. Marque **Public**.
4. **Não** marque "Add a README" (o projeto já tem um).
5. Clique **Create repository**. Deixe essa página aberta.

## Passo 3 — Enviar o projeto pelo VS Code

1. Abra a pasta `Belorae Start R0` no VS Code (**File → Open Folder**).
2. Clique no ícone de **Source Control** na barra lateral esquerda (parece uma ramificação de galho).
3. Clique em **Initialize Repository**.
4. No campo de mensagem, escreva `primeira versão do site` e clique no ✓ (**Commit**).
   - Se pedir para configurar nome/e-mail do Git, siga a instrução na tela (é rápido, só uma vez).
5. Clique em **Publish Branch**.
6. Escolha **Publish to GitHub public repository** e selecione o repositório `belorae-site` criado no Passo 2.

Pronto — o código já está no GitHub.

## Passo 4 — Ativar o GitHub Pages

1. No site do GitHub, abra o repositório `belorae-site`.
2. Vá em **Settings** (aba do repositório) → **Pages** (menu lateral).
3. Em **Branch**, selecione `main` e pasta `/ (root)`. Clique **Save**.
4. Aguarde 1–2 minutos. Atualize a página — vai aparecer o link do site, algo como:
   `https://SEU-USUARIO.github.io/belorae-site/`

Esse é o link para colocar no Instagram, WhatsApp, etc.

## Como atualizar o site depois

Sempre que editar algum arquivo (ex: trocar o número do WhatsApp):

1. Salve o arquivo (Ctrl+S).
2. Vá em **Source Control** no VS Code.
3. Clique no `+` ao lado do arquivo alterado (ou "+" ao lado de "Changes" para tudo).
4. Escreva uma mensagem curta explicando o que mudou (ex: `atualiza numero whatsapp`).
5. Clique ✓ **Commit**.
6. Clique em **Sync Changes** (ícone de setas circulares).

Em 1–2 minutos a mudança aparece no site publicado.

## Usando a extensão Claude no VS Code neste projeto

O arquivo `CLAUDE.md` na raiz do projeto já dá contexto automático pro Claude — ele vai saber que é um site estático, sem backend, com paleta de cores definida, etc. Você pode simplesmente pedir coisas como:

- "atualiza os produtos do cardápio no index.html"
- "troca a cor de destaque pra um tom mais escuro"
- "adiciona um menu mobile funcional"

sem precisar reexplicar o projeto toda vez.

## Erro comum

Esquecer de clicar em **Sync Changes** depois do commit — o arquivo fica salvo só no seu computador e não atualiza o site publicado.

## Exercício rápido

Depois do site no ar: abra `js/script.js`, troque `NUMERO_WHATSAPP` por um número de teste seu, salve, publique (Passo "como atualizar"), e clique no botão "Fazer Pedido" no site publicado — confirme que abre o WhatsApp com a mensagem certa.
