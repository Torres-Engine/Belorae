# TASKS.md

## Pendências de alinhamento (2026-07-25 — pós simplificação de CTAs v1.3.0)

- [ ] `SPEC.md` ficou desatualizado depois da v1.3.0: seção 7 e RF-01 ainda descrevem botão "Fazer Pedido" no header, botões no hero e CTA final com WhatsApp — isso não existe mais no site (ver `docs/CHANGELOG.md` v1.3.0 e `docs/DECISIONS.md`). Precisa de alinhamento com o dono do projeto antes de editar o `SPEC.md` (não é decisão da Juliana)
- [ ] `docs/PROJECT_SCOPE.md` e `docs/ARCHITECTURE.md` também mencionam o botão "Fazer Pedido" e o fluxo antigo (2 botões no `index.html`) — desatualizados desde antes da v1.3.0, agora ainda mais

## Bloqueadores de lançamento (fazer antes de publicar)

- [x] Confirmar nome oficial da marca (Belorae Confeitaria **Saudável**?)
- [x] Trocar número de WhatsApp placeholder em `js/script.js` (linha com `NUMERO_WHATSAPP`)
- [x] Gerar `assets/cardapio/cardapio-belorae.pdf` — versão RASCUNHO pronta, com fotos de exemplo, fonte serifada e layout de menu de verdade (conteúdo de exemplo, ver `docs/CARDAPIO-RASCUNHO.md`). Ainda falta substituir por produtos/preços/fotos reais.
- [ ] Baixar as 4 fotos de exemplo que faltam pro cardápio (banana com canela, trufa, pavê, mini quiche) — URLs prontas, ver conversa/prompt do Ricardo
- [ ] Substituir imagens de placeholder em `assets/images/` por fotos reais dos produtos
- [x] Revisar todos os textos do `index.html` (nomes de produtos, descrições, preços de exemplo)
- [x] Foto da Jaque (fundadora) para a seção "Sobre" — recebida e salva em `assets/images/jaque-sobre.jpg`

## Identidade visual (logo real recebida — 2026-07-25)

- [x] Logo real da Belorae salvo em `assets/logo/` (6 variações: vertical, horizontal fundo verde/creme, selo circular, ícones)
- [x] Aplicar o logo no header (trocar texto "Belorae" pela imagem) — concluído no rebuild v1.0.0 (Camila)
- [x] Aplicar o logo no footer — concluído no rebuild v1.0.0 (Camila)
- [x] Gerar favicon a partir do ícone (`assets/logo/belorae-icone-fundo-creme.jpg`) — concluído no rebuild v1.0.0 (Camila)

## Pendências de conteúdo (2026-07-25)

- [x] Foto de Jaque (dona da confeitaria) recebida diretamente e salva em `assets/images/jaque-sobre.jpg` — pronta para uso no "Sobre"
- [x] Ícone do Instagram no site, linkando para `https://www.instagram.com/belorae_confeitaria` — concluído no rebuild v1.0.0 (Camila)
- [x] Rodapé: adicionar cidade de atuação (Rio Negro - PR, atende Mafra e região) — concluído no rebuild v1.0.0 (Camila)
- [x] Remover o link do cardápio da mensagem automática do WhatsApp — confirmado em `js/script.js`: mensagem fixa é só "Olá! Vi o site da Belorae e quero fazer um pedido.", sem link do PDF

## Melhorias (não bloqueiam lançamento)

- [x] Definir logo real — recebido e aplicado no header, footer e favicon
- [ ] Ajustar paleta de cores em `css/style.css` (`:root`) se o logo pedir ajuste fino
- [ ] Comprar/configurar domínio próprio
- [ ] Adicionar Google Analytics
- [ ] Testar em pelo menos 2 celulares diferentes antes de divulgar

## Como usar este arquivo

Marcar `[x]` conforme for concluindo. Quando um bloqueador de lançamento for resolvido, mover para `docs/CHANGELOG.md` com a data.
