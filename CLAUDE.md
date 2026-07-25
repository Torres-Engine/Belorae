# CLAUDE.md — Contexto do Projeto

> Este arquivo é lido automaticamente pela extensão Claude Code no VS Code.
> Ele existe para o Claude nunca precisar perguntar "o que é esse projeto" de novo — economiza tokens e evita respostas genéricas.

## Fonte única da verdade

`SPEC.md` (raiz do projeto) é a especificação completa, seguindo Spec-Driven Development (SDD). Qualquer dúvida sobre requisito, conteúdo, regra de estilo (ex: proibição de travessão e emoji) ou critério de aceite: consultar `SPEC.md` primeiro. Este `CLAUDE.md` cobre convenções de código; `SPEC.md` cobre o quê e por quê.

## O que é

Site institucional **one-page** da **Belorae Confeitaria Saudável**. Objetivo único: converter visitantes em pedidos via WhatsApp. Não é loja virtual, não tem carrinho, não tem pagamento online.

## Stack

- HTML5 + CSS3 + JavaScript puro (vanilla). Sem framework, sem build step.
- Sem backend. Sem banco de dados.
- Hospedagem: GitHub Pages (estático).
- Cardápio: PDF hospedado em `assets/cardapio/`, linkado no botão de pedido.
- Pedido: botão abre WhatsApp via link `wa.me` com mensagem pré-escrita.

## Estrutura

```
index.html          → página única
css/style.css        → todo o estilo
js/script.js          → interações (menu mobile, link do whats)
assets/images/        → fotos dos produtos
assets/cardapio/       → PDF do cardápio
docs/                  → documentação do projeto (ver README.md)
```

## Convenções

- Um único `index.html`. Não criar múltiplas páginas sem necessidade.
- CSS em `css/style.css` — não usar CSS inline nem `<style>` no HTML.
- JS mínimo, só o necessário (menu mobile + montar link do WhatsApp).
- Não instalar dependências/npm sem justificativa forte — o projeto é intencionalmente sem build step.
- Cores e nomes de produtos: ver `docs/PROJECT_SCOPE.md`.

## O que NÃO fazer

- Não adicionar backend, banco de dados, autenticação ou carrinho de compras sem alinhar antes (ver `docs/DECISIONS.md`).
- Não trocar a hospedagem de GitHub Pages sem atualizar `docs/ARCHITECTURE.md`.
- Não commitar números de telefone/e-mails reais de clientes.

## Dono do projeto

Iniciante em programação — ao sugerir mudanças, explicar de forma simples e em pequenos passos.

## Idioma

Sempre responder, perguntar e pedir confirmações em português do Brasil (pt-BR), inclusive nos prompts de permissão/aprovação.

## Time de agentes

Este projeto tem um time hierárquico de subagentes em `.claude/agents/`, cada um com nome próprio: Ricardo (CEO AI) → Fernanda (Product Manager) → Eduardo (Solution Architect) → Marcos (Backend/DB Guardian) → Camila (Frontend Engineer) → Rafael (QA) → Beatriz (Security) → Lucas (DevOps) → Juliana (Technical Writer). Fluxo completo e tabela de referência em `docs/AGENTS.md`. Para pedidos amplos ou ambíguos, acionar o Ricardo primeiro.
