# TASKS.md

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
- [ ] Aplicar o logo no header (trocar texto "Belorae" pela imagem)
- [ ] Aplicar o logo no footer
- [ ] Gerar favicon a partir do ícone (`assets/logo/belorae-icone-fundo-creme.jpg` ou `-fundo-verde.jpg`)

## Pendências de conteúdo (2026-07-25)

- [x] Foto de Jaque (dona da confeitaria) recebida diretamente e salva em `assets/images/jaque-sobre.jpg` — pronta para uso no "Sobre"
- [ ] Ícone do Instagram no site, linkando para `https://www.instagram.com/belorae_confeitaria`
- [ ] Rodapé: adicionar cidade de atuação (Rio Negro - PR, atende Mafra e região)
- [ ] Remover o link do cardápio da mensagem automática do WhatsApp — dono do projeto prefere enviar o cardápio manualmente pro cliente

## Melhorias (não bloqueiam lançamento)

- [x] Definir logo real — recebido, falta aplicar no código (ver acima)
- [ ] Ajustar paleta de cores em `css/style.css` (`:root`) se o logo pedir ajuste fino
- [ ] Comprar/configurar domínio próprio
- [ ] Adicionar Google Analytics
- [ ] Testar em pelo menos 2 celulares diferentes antes de divulgar

## Como usar este arquivo

Marcar `[x]` conforme for concluindo. Quando um bloqueador de lançamento for resolvido, mover para `docs/CHANGELOG.md` com a data.
