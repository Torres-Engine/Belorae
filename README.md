# Belorae Confeitaria Saudável — Site

Landing page de conversão de encomendas via WhatsApp.

> **`SPEC.md`** é a fonte única da verdade do projeto (Spec-Driven Development). Qualquer implementação, atual ou reconstrução do zero, segue exatamente o que está lá.

## Estrutura

```
index.html            página única do site
css/style.css          estilos
js/script.js            interações
assets/images/          fotos dos produtos (adicionar depois)
assets/cardapio/        PDF do cardápio (adicionar depois)
docs/                   documentação do projeto
CLAUDE.md               contexto para o Claude Code no VS Code
```

## Documentação

| Arquivo | Para que serve |
|---|---|
| `docs/PROJECT_SCOPE.md` | O que o projeto é e não é |
| `docs/ARCHITECTURE.md` | Decisões técnicas e por quê |
| `docs/ROADMAP.md` | O que vem agora, depois e no futuro |
| `docs/TASKS.md` | Checklist de pendências |
| `docs/DECISIONS.md` | Histórico de decisões importantes |
| `docs/CHANGELOG.md` | Histórico de versões |
| `docs/DEPLOY.md` | Passo a passo para publicar o site (GitHub Pages) |
| `docs/AGENTS.md` | Time de agentes do Claude Code (`.claude/agents/`) e fluxo de revisão |

## Como ver o site no seu computador

1. Abra a pasta no VS Code.
2. Instale a extensão **Live Server** (ícone de extensões → buscar "Live Server" → Install).
3. Clique com botão direito em `index.html` → **Open with Live Server**.
4. O site abre no navegador e atualiza sozinho a cada alteração salva.

## Pendências antes de publicar

Ver checklist completo em `docs/TASKS.md`. Os 3 itens que travam o lançamento:

1. Número de WhatsApp real em `js/script.js`.
2. PDF real do cardápio em `assets/cardapio/`.
3. Fotos reais dos produtos em `assets/images/`.

## Deploy

Guia completo passo a passo em `docs/DEPLOY.md`.
