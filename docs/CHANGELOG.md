# CHANGELOG.md

## [1.1.0] — 2026-07-25

### Adicionado
- Plano de execução do `SPEC.md` (seção 12) reorganizado em ondas: agentes independentes entre si rodam em paralelo, só espera quem realmente depende do resultado de outro
- Ricardo (CEO AI) ganhou a responsabilidade permanente de identificar quando pode agrupar agentes em ondas, não só nesse rebuild
- `docs/AGENTS.md` documenta a execução em ondas como padrão do time

## [1.0.0] — 2026-07-25

### Adicionado
- `SPEC.md` na raiz do projeto: especificação técnica e de produto completa, seguindo Spec-Driven Development (SDD) — fonte única da verdade para o rebuild do zero
- README.md e CLAUDE.md atualizados para referenciar `SPEC.md`

## [0.7.0] — 2026-07-25

### Adicionado
- Fotos de exemplo em cada item do cardápio (script `assets/cardapio/gerar_cardapio.py` agora recorta e insere uma foto por produto)
- 4 dos 8 itens já usam as mesmas fotos de exemplo do site (bolo de cenoura, brownie, cookies, cheesecake)
- Pendente: baixar 4 fotos de exemplo restantes (bolo de banana, trufa, pavê, mini quiche) — ver docs/TASKS.md

## [0.6.0] — 2026-07-25

### Corrigido (redesign completo do cardápio em PDF)
- Trocada a fonte de Helvetica genérica para serifada (Liberation Serif), coerente com a identidade visual da marca
- Fundo creme de página inteira + moldura fina verde (antes: fundo branco puro, sem nenhum elemento de design)
- Logo trocado do lockup horizontal (que deixava muito espaço vazio) para o selo circular, mais compacto e charmoso
- Aviso de "rascunho" agora em um bloco destacado (badge), não mais um texto solto
- Preço de cada item alinhado à direita na mesma linha do nome (padrão visual de cardápio), não mais empilhado abaixo da descrição
- Linhas divisórias sutis entre itens
- Motivo: a primeira versão (v0.5.0) usava fonte e layout genéricos de relatório/documento — o dono do projeto avaliou como "nada profissional" e teve razão. Reportado em detalhe na conversa.

## [0.5.0] — 2026-07-25

### Corrigido
- `cardapio-belorae.pdf` regenerado: removidos travessões do aviso de rascunho, subtítulo e rodapé; corrigida acentuação inconsistente (conteudo/precos/serao/Cardapio/Saudavel/regiao estavam sem acento)

## [0.4.0] — 2026-07-25

### Alterado
- Todos os 9 subagentes em `.claude/agents/` ganharam nomes próprios para facilitar reconhecimento: Ricardo (CEO AI), Fernanda (Product Manager), Eduardo (Solution Architect), Marcos (Backend & Database Guardian), Camila (Frontend Engineer), Rafael (QA Engineer), Beatriz (Security Engineer), Lucas (DevOps Engineer), Juliana (Technical Writer)
- `docs/AGENTS.md` atualizado com os novos nomes, fluxo e tabela de referência

## [0.3.0] — 2026-07-25

### Adicionado
- Identidade visual real da Belorae salva em `assets/logo/` (6 variações: vertical, horizontal fundo verde, horizontal fundo creme, selo circular, ícone fundo creme, ícone fundo verde)
- `assets/cardapio/cardapio-belorae.pdf` gerado (versão RASCUNHO, com aviso visível de que o conteúdo é de exemplo)

### Pendente
- Aplicar o logo real no header/footer/favicon do site
- Foto da fundadora (Jaque) para a seção "Sobre"
- Ícone/link do Instagram
- Cidade de atuação no rodapé (Rio Negro - PR / Mafra e região)
- Remover link do cardápio da mensagem automática do WhatsApp

## [0.2.0] — 2026-07-25

### Adicionado
- Time hierárquico de 9 subagentes em `.claude/agents/` (CEO AI, Product Manager, Solution Architect, Backend & Database Guardian, Frontend Engineer, QA Engineer, Security Engineer, DevOps Engineer, Technical Writer)
- `docs/AGENTS.md` com fluxo de orquestração e tabela de referência

## [0.1.0] — 2026-07-25

### Adicionado
- Estrutura inicial do projeto e documentação (README, PROJECT_SCOPE, ARCHITECTURE, ROADMAP, TASKS, DECISIONS)
- `CLAUDE.md` com contexto para a extensão Claude Code no VS Code
- Site one-page inicial (`index.html`, `css/style.css`, `js/script.js`)
- Estrutura de pastas para imagens e cardápio (`assets/`)
