# Belorae Confeitaria Saudável — Site

Landing page de conversão de encomendas via WhatsApp.

> **`SPEC.md`** é a fonte única da verdade do projeto (Spec-Driven Development). Qualquer implementação, atual ou reconstrução do zero, segue exatamente o que está lá.

## Status Atual

**Versão:** 1.9.0 (Redesign visual "v2.0 — Blocos e Cápsulas")  
**Data:** 2026-07-26  
**Status:** ✅ **EM PRODUÇÃO** — Site ao vivo

**URL do Site:** https://gplansb.github.io/Belorae-Start-R0/

### Checklist de Lançamento
- [x] HTML/CSS/JS reconstruído do zero
- [x] Definition of Done: 11/11 itens passaram (QA)
- [x] Segurança: Zero vulnerabilidades (Security)
- [x] Conteúdo: Zero travessão, zero emoji (QA/CEO)
- [x] Responsivo: Testado em mobile, tablet, desktop
- [x] GitHub Pages: Ativado e publicado
- [ ] Produtos e preços reais (bloqueador menor — dados pendentes do dono)
- [ ] Fotos reais dos produtos (bloqueador menor — dados pendentes do dono)

## Como Acessar

1. **Site ao vivo:** https://gplansb.github.io/Belorae-Start-R0/
2. **Repositório:** https://github.com/GPlanSB/Belorae-Start-R0
3. **Documentação:** Ver pasta `docs/` ou arquivo `SPEC.md`

## Estrutura

```
index.html                 — Página única (HTML5)
css/style.css             — Estilos (CSS3, mobile-first)
js/script.js              — Vazio hoje: o site não tem nenhum botão que precise de JavaScript
                            (os botões da seção Cardápio e os botões flutuantes de contato são links simples, não precisam de JS)
assets/
  logo/                   — 6 arquivos de identidade visual
  images/                 — Fotos (Jaque + produtos)
  cardapio/               — PDF + gerador Python
docs/
  SPEC.md                 — Fonte única da verdade (v1.0.0)
  CHANGELOG.md            — Histórico de versões
  ARCHITECTURE.md         — Stack técnica
  DECISIONS.md            — Justificativas de design
  AGENTS.md               — Time de agentes Claude
  ROADMAP.md              — Próximas fases
  DEPLOY.md               — Instruções de publicação
```

## Tecnologia

- **Frontend:** HTML5 + CSS3 (sem framework, sem JavaScript no momento)
- **Hospedagem:** GitHub Pages (estático)
- **Cardápio:** PDF gerado por Python (reportlab + Pillow)
- **Contato:** Link `wa.me` (WhatsApp) em 3 lugares: botão "Fazer Pedido" na seção Cardápio, botão flutuante fixo no canto inferior direito da tela (dentro de uma cápsula única, junto com o botão flutuante de Instagram, desde o redesign v2.0) e rodapé do PDF do cardápio
- **Versionamento:** Git + GitHub

## Metodologia

**Spec-Driven Development (SDD):** O projeto segue uma especificação única em `SPEC.md`. Toda implementação é validada contra essa spec (não copiar código antigo sem revisar).

## Documentação

| Arquivo | Para que serve |
|---|---|
| `docs/SPEC.md` | Especificação completa (fonte única da verdade) |
| `docs/PROJECT_SCOPE.md` | O que o projeto é e não é |
| `docs/ARCHITECTURE.md` | Decisões técnicas e por quê |
| `docs/ROADMAP.md` | O que vem agora, depois e no futuro |
| `docs/TASKS.md` | Checklist de pendências |
| `docs/DECISIONS.md` | Histórico de decisões importantes |
| `docs/CHANGELOG.md` | Histórico de versões |
| `docs/DEPLOY.md` | Passo a passo para publicar o site (GitHub Pages) |
| `docs/AGENTS.md` | Time de agentes do Claude Code (`.claude/agents/`) e fluxo de revisão |

## Próximos Passos

Ver `docs/ROADMAP.md` para:
- Domínio customizado
- Melhorias de performance
- Automação de pedidos
- Analytics
