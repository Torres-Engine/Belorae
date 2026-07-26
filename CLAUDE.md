# CLAUDE.md — Contexto do Projeto

> Este arquivo é lido automaticamente pela extensão Claude Code no VS Code.
> Atualizado: 2026-07-26 — Rebuild v1.0.0 publicado, documentação fechada em v1.2.0, simplificação de CTAs em v1.3.0, reversão parcial (WhatsApp no rodapé) em v1.5.0

## Status Atual

✅ **Site em Produção** — Versão 1.5.0 ao vivo em https://gplansb.github.io/Belorae-Start-R0/

- ✅ Reconstruído do zero (Etapa 4 — Camila)
- ✅ Testado: 11/11 itens do Definition of Done passaram (Etapa 5 — Rafael)
- ✅ Segurança validada: zero vulnerabilidades (Etapa 6 — Beatriz)
- ✅ Conteúdo validado: zero travessão, zero emoji (Etapa 7 — Ricardo)
- ✅ Publicado no GitHub Pages (Etapa 8 — Lucas)
- ✅ Documentação atualizada (Etapa 9 — Juliana)
- ✅ v1.3.0: site simplificado para um único botão ("Ver Cardápio"); os 3 botões de WhatsApp que existiam no site (header, hero, CTA final) foram removidos; o link de WhatsApp passou a ficar só no rodapé do PDF do cardápio; `js/script.js` está vazio (ver `docs/CHANGELOG.md`)
- ✅ v1.5.0: reversão parcial. O botão único "Ver Cardápio" continua igual, mas o rodapé do site voltou a ter acesso direto ao WhatsApp, agora como ícone (ao lado do ícone de Instagram), por causa da fricção de precisar abrir o PDF para contatar. Também: enquadramento da foto da Jaque ajustado, responsividade mobile revisada e logo do header aumentada (ver `docs/CHANGELOG.md`)

## Fonte única da verdade

`SPEC.md` (raiz do projeto) é a especificação completa, seguindo Spec-Driven Development (SDD). Qualquer dúvida sobre requisito, conteúdo, regra de estilo (ex: proibição de travessão e emoji) ou critério de aceite: consultar `SPEC.md` primeiro. Este `CLAUDE.md` cobre convenções de código; `SPEC.md` cobre o quê e por quê.

## O que é

Site institucional **one-page** da **Belorae Confeitaria Saudável**. Objetivo único: converter visitantes em pedidos via WhatsApp. Não é loja virtual, não tem carrinho, não tem pagamento online.

**URL ao vivo:** https://gplansb.github.io/Belorae-Start-R0/

## Stack

- HTML5 + CSS3 + JavaScript puro (vanilla). Sem framework, sem build step.
- Sem backend. Sem banco de dados.
- Hospedagem: GitHub Pages (estático).
- Cardápio: PDF hospedado em `assets/cardapio/`. O botão principal do site é "Ver Cardápio".
- Pedido: o link `wa.me` com mensagem pré-escrita fica no rodapé do PDF do cardápio e também como ícone de WhatsApp no rodapé do `index.html` (acesso direto, ao lado do ícone de Instagram).

## Estrutura

```
index.html               → página única
css/style.css            → todo o estilo (mobile-first, responsivo)
js/script.js             → vazio hoje (nenhum botão do site precisa de JS)
assets/
  logo/                  → 6 arquivos da marca
  images/                → fotos (Jaque, produtos)
  cardapio/              → PDF + gerador Python
docs/                    → documentação completa
  SPEC.md                → especificação v1.0.0 (fonte única da verdade)
  CHANGELOG.md           → histórico de versões
  AGENTS.md              → time de agentes Claude
```

## Metodologia

**Spec-Driven Development (SDD):** SPEC.md é a fonte única da verdade. Toda implementação valida contra a spec. Não reutilizar código antigo sem revisar.

Plano de rebuild (Seção 12 de SPEC.md):
1. ✅ Eduardo (viabilidade técnica)
2. ✅ Fernanda (conteúdo)
3. ✅ Marcos (zero backend)
4. ✅ Camila (implementação)
5. ✅ Rafael (QA/testes)
6. ✅ Beatriz (segurança)
7. ✅ Ricardo (travessão/emoji)
8. ✅ Lucas (deploy)
9. ✅ Juliana (documentação)

Rodada extra depois da Etapa 9 (v1.3.0): Camila simplificou os CTAs do site (um único botão, "Ver Cardápio") e moveu o link de WhatsApp para o rodapé do PDF do cardápio. Detalhes em `docs/CHANGELOG.md` e motivo da decisão em `docs/DECISIONS.md`.

Rodada extra depois disso (v1.5.0): reversão parcial. O botão único "Ver Cardápio" não mudou, mas o rodapé do site voltou a ter um ícone de WhatsApp com acesso direto, ao lado do ícone de Instagram, porque a fricção de precisar abrir o PDF só para contatar era grande demais. Detalhes em `docs/CHANGELOG.md` e motivo em `docs/DECISIONS.md`.

## Convenções

- Um único `index.html`. Não criar múltiplas páginas sem necessidade.
- CSS em `css/style.css` — não usar CSS inline nem `<style>` no HTML.
- JS mínimo — hoje `js/script.js` está vazio, porque não sobrou nenhum botão que precise de comportamento em JS (o menu some só via CSS, e o ícone de WhatsApp do rodapé é um link simples). Só adicionar código ali se realmente for necessário no futuro.
- Não instalar dependências/npm sem justificativa forte — o projeto é intencionalmente sem build step.
- Cores e nomes de produtos: ver `docs/PROJECT_SCOPE.md`.

## O que NÃO fazer

- Não adicionar backend, banco de dados, autenticação sem alinhar antes
- Não trocar hospedagem sem atualizar docs/ARCHITECTURE.md
- Não commitar números de telefone/dados reais de clientes
- Não copiar código antigo sem revisar contra SPEC.md

## Dono do projeto

Iniciante em programação — ao sugerir mudanças, explicar de forma simples e em pequenos passos.

## Idioma

Português do Brasil (pt-BR).

## Time de Agentes (Claude Code)

10 agentes especializados em `.claude/agents/`, incluindo a Sofia (UX/UI Designer), adicionada para elevar o nível visual do site. Ver `docs/AGENTS.md` para detalhes.
