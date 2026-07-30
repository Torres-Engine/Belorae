# CLAUDE.md — Contexto do Projeto

> Este arquivo é lido automaticamente pela extensão Claude Code no VS Code.
> Atualizado: 2026-07-30 — Rebuild v1.0.0 publicado, documentação fechada em v1.2.0, simplificação de CTAs em v1.3.0, reversão parcial (WhatsApp no rodapé) em v1.5.0, segunda reversão parcial (botão "Fazer Pedido" no cardápio) em v1.6.0, ícones viram botões flutuantes fixos em v1.7.0, redesign visual "v2.0 — Blocos e Cápsulas" em v1.9.0, alegação "sem açúcar refinado" removida do site e do cardápio em v1.17.0

## Status Atual

✅ **Site em Produção** — Versão 1.9.0 ao vivo em https://gplansb.github.io/Belorae-Start-R0/

- ✅ Reconstruído do zero (Etapa 4 — Camila)
- ✅ Testado: 11/11 itens do Definition of Done passaram (Etapa 5 — Rafael)
- ✅ Segurança validada: zero vulnerabilidades (Etapa 6 — Beatriz)
- ✅ Conteúdo validado: zero travessão, zero emoji (Etapa 7 — Ricardo)
- ✅ Publicado no GitHub Pages (Etapa 8 — Lucas)
- ✅ Documentação atualizada (Etapa 9 — Juliana)
- ✅ v1.3.0: site simplificado para um único botão ("Ver Cardápio"); os 3 botões de WhatsApp que existiam no site (header, hero, CTA final) foram removidos; o link de WhatsApp passou a ficar só no rodapé do PDF do cardápio; `js/script.js` está vazio (ver `docs/CHANGELOG.md`)
- ✅ v1.5.0: reversão parcial. O botão único "Ver Cardápio" continua igual, mas o rodapé do site voltou a ter acesso direto ao WhatsApp, agora como ícone (ao lado do ícone de Instagram), por causa da fricção de precisar abrir o PDF para contatar. Também: enquadramento da foto da Jaque ajustado, responsividade mobile revisada e logo do header aumentada (ver `docs/CHANGELOG.md`)
- ✅ v1.6.0: segunda reversão parcial. A seção Cardápio ganhou o botão "Fazer Pedido" ao lado do botão "Ver Cardápio" (os dois convivem, lado a lado), e o ícone de Instagram do rodapé passou a usar o gradiente oficial da marca em vez do contorno verde da Belorae. Site não tem mais "único botão" (ver `docs/CHANGELOG.md` e `docs/DECISIONS.md`)
- ✅ v1.7.0: os ícones de WhatsApp e Instagram saíram do rodapé e viraram botões flutuantes fixos no canto inferior direito da tela, visíveis durante toda a rolagem da página. O rodapé agora só tem logo, nome da marca e localização. Ícone da logo do rodapé aumentado de 1.5rem para 1.75rem (ver `docs/CHANGELOG.md` e `docs/DECISIONS.md`)
- ✅ v1.9.0: redesign visual "v2.0 — Blocos e Cápsulas" (direção de Sofia, implementado por Camila). O sistema visual mudou de "faixas empilhadas" para "blocos arredondados sobre fundo creme": header virou cápsula sólida verde flutuante e sticky (nova cor `--cor-verde-marca`, logo trocado para a versão de fundo verde), hero ganhou foto grande com chips flutuantes (Cookies e Brownie), cartões de produto viraram horizontais em mobile, seção Sobre ganhou bloco de fundo suave com moldura na foto da Jaque, seção Cardápio virou painel de cor sólida (era gradiente) com glifo decorativo, rodapé virou bloco marrom com 2 colunas (marca + nova coluna "Navegação"), e os botões flutuantes de WhatsApp/Instagram passaram a ficar dentro de uma única cápsula creme. Nenhuma cor oficial da paleta foi redefinida (só tokens novos adicionados) e nenhum link de contato mudou de destino ou comportamento. Correção de contraste no botão "Fazer Pedido" incluída na mesma entrega (ver `docs/CHANGELOG.md` e `docs/DECISIONS.md`)
- ✅ v1.17.0: alegação "sem açúcar refinado" removida de todo o site (meta description, hero, chip do brownie, card do Bolo de Cenoura, seção Sobre) e de todas as 13 descrições de produto no gerador do PDF do cardápio (`assets/cardapio/gerar_cardapio.py`), com PDF regenerado. Pedido direto do dono do projeto: ele não tem como comprovar essa alegação hoje (a ficha técnica já indicava açúcar demerara/mascavo em várias receitas). Nenhum outro texto, preço ou link mudou (ver `docs/CHANGELOG.md`)

## Fonte única da verdade

`SPEC.md` (raiz do projeto) é a especificação completa, seguindo Spec-Driven Development (SDD). Qualquer dúvida sobre requisito, conteúdo, regra de estilo (ex: proibição de travessão e emoji) ou critério de aceite: consultar `SPEC.md` primeiro. Este `CLAUDE.md` cobre convenções de código; `SPEC.md` cobre o quê e por quê.

## O que é

Site institucional **one-page** da **Belorae Confeitaria Saudável**. Objetivo único: converter visitantes em pedidos via WhatsApp. Não é loja virtual, não tem carrinho, não tem pagamento online.

**URL ao vivo:** https://gplansb.github.io/Belorae-Start-R0/

## Stack

- HTML5 + CSS3 + JavaScript puro (vanilla). Sem framework, sem build step.
- Sem backend. Sem banco de dados.
- Hospedagem: GitHub Pages (estático).
- Cardápio: PDF hospedado em `assets/cardapio/`. A seção Cardápio do site tem 2 botões lado a lado: "Fazer Pedido" (WhatsApp) e "Ver Cardápio" (abre o PDF).
- Pedido: o link `wa.me` com mensagem pré-escrita fica em 3 lugares: botão "Fazer Pedido" na seção Cardápio, botão flutuante fixo de WhatsApp no canto inferior direito da tela (`.social-float`, dentro de uma cápsula única junto com o botão flutuante de Instagram, sempre visível durante a rolagem) e rodapé do PDF do cardápio. O rodapé do site (`footer`) não tem mais nenhum ícone de contato; desde a v1.9.0, ele tem 2 colunas: marca (logo, nome, localização) e uma coluna "Navegação" com os mesmos 3 links do menu do header.
- Visual: desde a v1.9.0 ("v2.0 — Blocos e Cápsulas"), o site usa um sistema de blocos arredondados sobre fundo creme (header em cápsula verde, painel sólido na seção Cardápio, bloco suave na seção Sobre). Paleta de cores oficial (`docs/PROJECT_SCOPE.md` e SPEC.md 6.1) não mudou; foram só adicionados tokens novos de cor e de raio de borda em `css/style.css` (`:root`).

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

Rodada extra depois disso (v1.6.0): segunda reversão parcial, pedida diretamente pelo dono do projeto. A seção Cardápio ganhou o botão "Fazer Pedido" (WhatsApp) ao lado do botão "Ver Cardápio" (os dois coexistem), e o ícone de Instagram do rodapé passou a usar o gradiente oficial da marca. O site não tem mais "um único botão"; tem 2 na seção Cardápio, mais os ícones do rodapé. Detalhes em `docs/CHANGELOG.md` e motivo em `docs/DECISIONS.md`.

Rodada extra depois disso (v1.7.0): os ícones de WhatsApp e Instagram saíram do rodapé e viraram botões flutuantes fixos no canto inferior direito da tela, sempre visíveis durante a rolagem da página, pedido diretamente pelo dono do projeto para dar acesso mais rápido ao contato. O rodapé passou a ter só logo, nome da marca e localização. Detalhes em `docs/CHANGELOG.md` e motivo em `docs/DECISIONS.md`.

Rodada extra depois disso (v1.9.0): redesign visual completo, "v2.0 — Blocos e Cápsulas", a partir de uma referência visual trazida pelo dono do projeto e adaptada por Sofia à paleta de cores já existente da Belorae. Implementado por Camila, aprovado por Rafael (QA). Header, hero, cartões de produto, seção Sobre, seção Cardápio, rodapé e botões flutuantes ganharam a nova linguagem visual de blocos arredondados; nenhuma cor oficial da paleta foi redefinida e nenhum link de contato mudou de destino ou comportamento. Detalhes em `docs/CHANGELOG.md` e motivo em `docs/DECISIONS.md`.

## Convenções

- Um único `index.html`. Não criar múltiplas páginas sem necessidade.
- CSS em `css/style.css` — não usar CSS inline nem `<style>` no HTML.
- JS mínimo — hoje `js/script.js` está vazio, porque não sobrou nenhum botão que precise de comportamento em JS (o menu some só via CSS, e os botões flutuantes de WhatsApp/Instagram são links simples). Só adicionar código ali se realmente for necessário no futuro.
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

Dois times, ambos em `.claude/agents/`:

- **Time técnico** (10 agentes, liderado por Ricardo): cuida do site. Ver `docs/AGENTS.md`.
- **Time de negócio** (9 agentes, liderado por Marina): cuida da empresa (produção, insumos, financeiro, marketing, atendimento, qualidade, jurídico, pessoas). Ver `docs/EQUIPE_NEGOCIO.md`.
