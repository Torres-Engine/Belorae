# CHANGELOG.md

## [1.9.0] — 2026-07-26 — Redesign visual "v2.0 — Blocos e Cápsulas"

### Alterado
- Todo o sistema visual do site mudou de "faixas empilhadas" para "blocos arredondados sobre fundo creme", brief de Sofia (UX/UI), implementado por Camila em `index.html` e `css/style.css`
- Header virou uma cápsula sólida verde, flutuante e sticky no topo da página. Nova cor de marca, `--cor-verde-marca` (`#4A543C`), medida por pixel do arquivo `assets/logo/belorae-logo-horizontal-fundo-verde.jpg`. O header trocou o logo de fundo creme pelo logo de fundo verde (`belorae-logo-horizontal-fundo-verde.jpg`), já que agora fica sobre um fundo escuro
- Hero ganhou uma foto grande, com dois "chips" flutuantes ao lado mostrando Cookies Sem Glúten e Brownie Fit de Amêndoas
- Cartões de produto (seção Destaques) viraram horizontais em telas pequenas (foto ao lado do texto, não em cima)
- Seção Sobre ganhou um bloco de fundo com a cor nova `--cor-fundo-suave`, com uma moldura branca ao redor da foto da Jaque; o recorte da foto também mudou, mostrando mais dela
- Seção Cardápio virou um painel de fundo sólido na cor `--cor-verde-marca` (antes era um gradiente), com um glifo SVG decorativo em formato de "raminho" acima do título (símbolo `#ico-raminho`, definido inline logo depois da abertura do `<body>`, reaproveitado também acima de "Destaques")
- Rodapé virou um bloco marrom (`--cor-texto`) com 2 colunas: marca (logo, nome, localização) e uma coluna nova, "Navegação", com os mesmos 3 links do menu do header (Produtos, Sobre, Cardápio)
- Os botões flutuantes de WhatsApp e Instagram, que antes ficavam soltos lado a lado no canto inferior direito, agora ficam dentro de uma única cápsula creme (`.social-float`)

### Corrigido
- Contraste do texto do botão "Fazer Pedido" estava abaixo do mínimo AA (4.48:1, o exigido é 4.5:1). Corrigido trocando a cor do texto para o token novo `--cor-texto-forte` (`#2A1F16`), sem mudar a cor de fundo do botão

### Adicionado
- 4 tokens de cor novos em `:root`: `--cor-verde-marca`, `--cor-fundo-suave`, `--cor-texto-forte`, `--cor-ouro` (este último só decorativo, usado no glifo sobre fundo verde, nunca em texto ou botão). Nenhum dos 6 tokens de cor já existentes (`--cor-fundo`, `--cor-primaria`, `--cor-primaria-escura`, `--cor-texto`, `--cor-acento`, `--cor-branco`) foi redefinido
- Tokens novos de raio de borda (`--raio-medio`, `--raio-grande`, `--raio-bloco`, `--raio-pilula`) e de sombra, usados nos blocos arredondados do redesign

### Testado
- Rafael (QA) aprovou o redesign completo. Sinalizou, como observação de rastreabilidade (não bug): `SPEC.md` RF-03 ainda citava o logo de fundo creme no header (agora é fundo verde), e a seção 7 (Footer) não mencionava a coluna "Navegação" nem o painel de Cardápio ter virado cor sólida. Ambos os pontos corrigidos nesta entrega
- Nenhum link de WhatsApp ou Instagram mudou de destino, comportamento ou atributo (`target`, `rel="noopener"`); confirmado pelo Rafael. Mudou só o estilo visual ao redor
- `js/script.js` continua vazio: nada no redesign precisou de JavaScript

### Documentação
- `SPEC.md`: RF-03 corrigido (logo do header agora é o de fundo verde); seção 6.1 ganhou um adendo documentando os 4 tokens de cor novos, deixando explícito que os tokens originais não mudaram; seção 6.3 (tabela de uso do logo) corrigida para refletir a troca do header; seção 7 atualizada (linha Cardápio: painel sólido em vez de gradiente; linha Footer: nova coluna de navegação)
- `docs/DECISIONS.md`: nova entrada registrando o motivo do redesign (referência visual trazida pelo dono do projeto, adaptada com a paleta de cores já existente da Belorae)
- `README.md` e `CLAUDE.md` atualizados para a versão 1.9.0

### Notes
- Motivo: o dono do projeto trouxe uma referência visual de layout que gostou (blocos arredondados, cápsulas, painéis de cor sólida) e pediu para aplicar esse estilo ao site, sem trocar a identidade de cores da Belorae. Sofia adaptou a referência usando a paleta já aprovada (nenhuma cor oficial foi trocada, só adicionados tokens novos para os elementos que a paleta original não cobria, como o verde do header)
- Projetado por Sofia, implementado por Camila, aprovado por Rafael (QA), sem bloqueadores
- Decisão de produto registrada em `docs/DECISIONS.md`

## [1.8.0] — 2026-07-26 — Novo time: Equipe de Negócio da Belorae

### Adicionado
- Segundo time de agentes, independente do time técnico: **Marina** (Diretora Geral / CEO do Negócio, modelo Opus) e 8 setores: **Vitor** (Produção), **Patrícia** (Compras & Insumos), **Renato** (Financeiro), **Bianca** (Marketing & Vendas), **Diego** (Atendimento & Operações de Pedido), **Helena** (Qualidade & Segurança Alimentar), **Otávio** (Jurídico & Regulatório), **Fabiana** (Recursos Humanos)
- Arquivos em `.claude/agents/`: `diretora-negocio.md`, `producao-confeitaria.md`, `compras-insumos.md`, `financeiro.md`, `marketing-vendas.md`, `atendimento-operacoes.md`, `qualidade-seguranca-alimentar.md`, `juridico-regulatorio.md`, `recursos-humanos.md`
- Nova documentação: `docs/EQUIPE_NEGOCIO.md`, com fluxo de acionamento e tabela de referência
- `CLAUDE.md` atualizado para referenciar os dois times (técnico e de negócio)
- Objetivo do time registrado em `docs/DECISIONS.md`: transformar a Belorae na melhor confeitaria saudável da região

## [1.7.0] — 2026-07-26 — Ícones de WhatsApp e Instagram viram botões flutuantes fixos

### Alterado
- Os ícones de WhatsApp e Instagram saíram do rodapé do site e viraram botões flutuantes fixos no canto inferior direito da tela (`.social-float`), visíveis o tempo todo durante a rolagem da página, não só quando a pessoa chega ao final
- Botões flutuantes têm uma animação sutil de entrada (aparecem com um pequeno deslizar de baixo para cima e fade, meio segundo depois da página carregar)
- Suporte a `prefers-reduced-motion`: quem tem essa preferência de acessibilidade ativada no navegador não vê a animação de entrada nem as transições de hover dos botões
- Posição dos botões respeita a área segura de iPhones com notch/barra inferior (`env(safe-area-inset-right)` e `env(safe-area-inset-bottom)`), para não ficarem cobertos ou cortados
- Botões flutuantes ficam ocultos na impressão da página (`@media print`), já que não fazem sentido em papel
- Reservado um espaço extra no rodapé em telas pequenas (mobile) para os botões flutuantes não ficarem sobrepostos ao texto do rodapé
- Ícone da logo no rodapé (`.footer-icon`) aumentado de 1.5rem para 1.75rem
- O rodapé do site agora tem só logo, nome da marca e localização (Rio Negro, PR. Atendemos Mafra e região) — sem nenhum ícone de contato

### Testado
- Rafael (QA) aprovou, sem bloqueadores
- Beatriz (Security) aprovou, sem bloqueadores

### Documentação
- `SPEC.md`: seção 6.6, seção 7 (tabela de seções) corrigidas de "ícone no rodapé" para "botões flutuantes fixos no canto inferior direito"
- `docs/ARCHITECTURE.md`: diagrama de fluxo atualizado (ícone de WhatsApp deixou de aparecer como item do rodapé e passou a ser descrito como flutuante; ícone de Instagram incluído no diagrama)
- `docs/PROJECT_SCOPE.md` e `assets/cardapio/LEIA-ME.md` revisados para não deixarem menções desatualizadas sobre pontos de acesso ao WhatsApp
- `docs/DECISIONS.md`: nova entrada registrando o motivo da mudança de posição
- `docs/TASKS.md`: pendência apontada pelo Rafael (desalinhamento de `docs/PROJECT_SCOPE.md`, `docs/ARCHITECTURE.md` e `assets/cardapio/LEIA-ME.md` sobre os pontos de acesso ao WhatsApp) marcada como resolvida
- `README.md` e `CLAUDE.md` atualizados para a versão 1.7.0 e para não falarem mais em "ícone no rodapé"

### Notes
- Motivo: o dono do projeto pediu que os ícones ficassem sempre visíveis durante a navegação, sem precisar rolar até o fim da página para encontrá-los. Botões flutuantes no canto inferior direito são um padrão comum em sites de contato rápido (WhatsApp, chat) e resolvem exatamente essa fricção
- Projetado por Sofia, implementado por Camila, aprovado por Rafael (QA) e Beatriz (Security), sem bloqueadores
- Decisão de produto registrada em `docs/DECISIONS.md`

## [1.6.0] — 2026-07-26 — Segunda reversão parcial: botão "Fazer Pedido" na seção Cardápio + Instagram com gradiente oficial

### Adicionado
- Novo botão "Fazer Pedido" na seção Cardápio (`#cardapio`), posicionado ao lado do botão "Ver Cardápio", dentro de um painel visual novo (`.cardapio-panel` / `.cardapio-buttons`). "Fazer Pedido" abre o WhatsApp direto (`wa.me/5541996123682`) com a mesma mensagem da seção 6.6 do `SPEC.md`; "Ver Cardápio" continua abrindo o PDF. Desenhado por Sofia, implementado por Camila

### Alterado
- Ícone de Instagram do rodapé deixou de ser contornado na cor verde da Belorae e passou a usar o gradiente oficial da marca Instagram (amarelo, laranja, rosa, roxo), por preferência explícita do dono do projeto
- A cor `--cor-acento` (terracota) ficou reservada só para o botão principal ("Fazer Pedido"), reforçando qual dos dois botões é a ação prioritária
- Adicionado suporte a `prefers-reduced-motion`: quem usa essa preferência de acessibilidade no navegador deixa de ver as transições e animações de hover nos botões e ícones

### Testado
- Rafael (QA) aprovou o fluxo completo, com ressalva só de documentação (o `SPEC.md` ainda descrevia "único botão do site"), corrigida nesta entrega
- Beatriz (Security) aprovou sem ressalvas

### Documentação
- `SPEC.md`: RF-01 e RF-02 corrigidos (a seção Cardápio agora tem 2 botões, não um só); RF-06 detalhado com o gradiente oficial do Instagram; seção 6.6 e tabela da seção 7 (linha Cardápio e linha Footer) atualizadas para descrever os 2 botões e os 3 pontos de acesso ao WhatsApp no site (botão "Fazer Pedido", ícone do rodapé, link dentro do PDF); Definition of Done (seção 11) ajustada
- `docs/DECISIONS.md`: nova entrada registrando a segunda reversão parcial (contexto, decisão, motivo, quando revisitar)
- `docs/TASKS.md`: pendência de desalinhamento do `SPEC.md` (aberta na v1.3.0) marcada como resolvida
- `README.md` e `CLAUDE.md` atualizados para a versão 1.6.0 e para não afirmarem mais "único botão do site"

### Notes
- Motivo: o dono do projeto avaliou que o ícone de WhatsApp do rodapé (adicionado na v1.5.0) ainda deixava o acesso ao WhatsApp pouco visível, longe de onde a pessoa decide pedir. O botão "Fazer Pedido" na seção Cardápio resolve isso sem remover o ícone do rodapé (os dois convivem, junto com o link dentro do PDF: 3 pontos de acesso ao WhatsApp no total)
- Decisão de produto tomada diretamente pelo dono do projeto, registrada em `docs/DECISIONS.md`

## [1.5.0] — 2026-07-26 — Reversão parcial: WhatsApp de volta no rodapé + ajustes de polimento (Sofia)

### Alterado
- Rodapé (`footer`) do site ganhou de volta um ícone de WhatsApp com acesso direto, ao lado de um ícone de Instagram (antes era só um link de texto). Ícones em SVG inline, desenhados pela Sofia: WhatsApp em verde oficial `#25D366` preenchido, Instagram contornado na cor da marca. Implementado por Camila
- O botão único "Ver Cardápio" na seção de cardápio continua exatamente igual, sem nenhuma mudança
- Enquadramento da foto da Jaque na seção "Sobre" ajustado (novo arquivo `assets/images/jaque-sobre-v2.jpg`)
- Ajustes de responsividade mobile no header e na tipografia, revisados pela Sofia
- Logo do header aumentada (revisão de polimento da Sofia), com `scroll-padding-top` adicionado ao `html` para a navegação por âncora não ficar escondida atrás do header sticky

### Documentação
- `docs/DECISIONS.md`: nova entrada registrando a reversão parcial (contexto, decisão, motivo, quando revisitar)
- `SPEC.md`: seção 6.6 e tabela da seção 7 atualizadas (o site voltou a ter acesso direto ao WhatsApp, agora como ícone no rodapé, não mais ausente); novo requisito RF-10 (ícone de WhatsApp no rodapé); RF-01 e Definition of Done (seção 11) ajustados para refletir os dois lugares onde o link de WhatsApp aparece (PDF e rodapé do site)
- `README.md` e `CLAUDE.md` atualizados para versão 1.5.0 e para não afirmarem mais que "o site não tem nenhum link de WhatsApp"

### Notes
- Motivo da reversão: o dono do projeto avaliou o site ao vivo e considerou a fricção grande demais para contatar via WhatsApp (era preciso abrir o PDF do cardápio e rolar até o rodapé). O ícone do rodapé resolve isso sem voltar a ter os 3 botões de WhatsApp removidos na v1.3.0 (header, hero, CTA final) — é uma posição discreta, de contato/rede social, não um CTA duplicado
- Decisão de produto registrada em `docs/DECISIONS.md`

## [1.4.0] — 2026-07-25 — Novo agente: Sofia (UX/UI Designer)

### Adicionado
- Novo agente no time: **Sofia (UX/UI Designer)**, `.claude/agents/ux-ui-designer.md`, modelo Opus — padrão de exigência de agência premium, foco em elevar o nível visual do site
- Posicionada no fluxo: define direção visual antes de Camila implementar, e revisa polimento visual depois, antes de Rafael testar
- `docs/AGENTS.md`, `SPEC.md` (seção 9) e `CLAUDE.md` atualizados para o time de 10 agentes
- Decisão registrada em `docs/DECISIONS.md`

## [1.3.0] — 2026-07-25 — Simplificação de CTAs (um único botão no site)

### Alterado
- Removido o botão "Fazer Pedido" do cabeçalho (header) do site
- Removida a `.hero-buttons` inteira do hero: não existem mais ali os botões "Fazer Pedido pelo WhatsApp" e "Ver Cardápio"
- Removida a seção inteira de CTA final (`.cta-final`, era "Pronto para pedir? ... Fazer Pedido pelo WhatsApp")
- A seção "Cardápio" (`#cardapio`) passou a ter o único botão do site inteiro: "Ver Cardápio", que abre `assets/cardapio/cardapio-belorae.pdf`, posicionado perto do rodapé
- `js/script.js` foi esvaziado (ficou só um comentário explicando o motivo) e a tag `<script src="js/script.js">` foi removida do `index.html` — o site não usa mais nenhum JavaScript, porque não sobrou nenhum botão que precise de clique em JS (o menu nunca teve toggle: ele já sumia só via CSS em telas pequenas)
- CSS: removidas as regras que ficaram órfãs (`.hero-buttons`, `.btn-secondary`, `.btn-light`, `.cta-final` e as referências dentro dos media queries) e corrigida uma chave `}` solta que tinha sobrado no arquivo

### Adicionado
- Cardápio em PDF (script `assets/cardapio/gerar_cardapio.py`) ganhou um link clicável "Fazer pedido pelo WhatsApp" no rodapé, apontando para `https://wa.me/5541996123682` com a mensagem pronta
- O caminho do projeto usado pelo script (antes fixo em `/sessions/...`, resquício de um ambiente antigo) agora é calculado a partir da posição do próprio arquivo — funciona em qualquer computador
- `assets/cardapio/cardapio-belorae.pdf` foi regenerado (pelo dono do projeto, fora deste ambiente) já com o link de WhatsApp no rodapé

### Testado
- Responsividade revisada em 375px, 390px e 428px — nenhuma quebra encontrada além do bug de CSS já corrigido acima

### Documentação
- `SPEC.md` realinhado com o fluxo novo: RF-01 (link de WhatsApp agora descrito como vivendo no rodapé do PDF, não em botão do site), tabela de seções (seção 7: header e hero sem botão, sem seção "CTA final", cardápio como único botão do site) e seção 6.6 (mensagem descrita como do link do PDF, não de um botão) e item de Definition of Done (seção 11) atualizados
- `docs/PROJECT_SCOPE.md` (escopo) e `docs/ARCHITECTURE.md` (diagrama de fluxo) atualizados para mostrar o caminho único: site → botão "Ver Cardápio" → PDF → link de WhatsApp dentro do PDF
- `assets/cardapio/LEIA-ME.md` corrigido: não menciona mais "botão do site" apontando para o WhatsApp, e sim o botão único "Ver Cardápio" e o link dentro do PDF

### Notes
- Essa mudança inverte a lógica de conversão do site: antes, o WhatsApp era o botão principal em 3 lugares (header, hero e CTA final), e o cardápio em PDF não tinha nenhum link. Agora o site só tem um botão ("Ver Cardápio"), e é o PDF que leva ao WhatsApp, no rodapé. Motivo: menos botões repetidos, caminho único e claro (site → cardápio → WhatsApp)
- Decisão de produto registrada em `docs/DECISIONS.md`

## [1.2.0] — 2026-07-25 — Documentação Pós-Deploy (Fechamento da Onda 5)

### Adicionado
- Etapa 9 do plano de execução (Juliana) formalmente concluída: documentação revisada e alinhada após o rebuild completo (Onda 2 a 4) e a publicação no GitHub Pages (Onda 4)
- `CLAUDE.md` passou a registrar explicitamente o status de produção e a URL do site ao vivo

### Corrigido
- URL do GitHub Pages tinha um erro de digitação em `README.md` e `docs/CHANGELOG.md` (aparecia como `gpansb`, faltando a letra "l"). Corrigido para `https://gplansb.github.io/Belorae-Start-R0/`, que corresponde ao nome real do usuário/organização do repositório (`GPlanSB`, em minúsculas conforme o padrão do GitHub Pages)
- Mesma correção aplicada em `CLAUDE.md`

### Notes
- Com esta entrega, todas as 9 etapas do plano de execução do rebuild (seção 12 do `SPEC.md`) estão concluídas: Eduardo, Fernanda, Marcos, Camila, Rafael, Beatriz, Ricardo, Lucas e Juliana
- Pendências que não bloqueiam o site continuar no ar (produtos/preços reais, fotos reais) seguem registradas em `docs/TASKS.md`

## [1.1.0] — 2026-07-25

### Adicionado
- Plano de execução do `SPEC.md` (seção 12) reorganizado em ondas: agentes independentes entre si rodam em paralelo, só espera quem realmente depende do resultado de outro
- Ricardo (CEO AI) ganhou a responsabilidade permanente de identificar quando pode agrupar agentes em ondas, não só nesse rebuild
- `docs/AGENTS.md` documenta a execução em ondas como padrão do time

## [1.0.0] — 2026-07-25 — Rebuild do Zero (Versão Inicial)

### Added
- **Novo:** Reconstrução completa do site seguindo SPEC.md v1.0.0 (Spec-Driven Development)
- **Novo:** HTML5 semântico, CSS3 responsivo (375px–1440px), JavaScript vanilla
- **Novo:** Design System completo: 6 cores CSS, tipografia em Georgia/sans-serif
- **Novo:** 7 seções: Header, Hero, Produtos (4 cards), Sobre (foto Jaque), Cardápio (PDF), CTA final, Footer
- **Novo:** Link WhatsApp integrado (RF-01): mensagem exata "Olá! Vi o site da Belorae e quero fazer um pedido."
- **Novo:** Logo real (header, footer, favicon), foto da Jaque com legenda
- **Novo:** Footer com localização "Rio Negro, PR. Atendemos Mafra e região." + Instagram link

### Quality Assurance
- ✅ **Definition of Done:** Todos os 11 critérios passaram (Rafael)
- ✅ **Segurança:** Zero vulnerabilidades, zero credenciais commitadas (Beatriz)
- ✅ **Conteúdo:** Zero travessão, zero emoji (Ricardo)
- ✅ **Responsividade:** Testado em 375px, 768px, 1440px (Camila + Rafael)

### Deployment
- ✅ **GitHub Pages:** Site ao vivo em https://gplansb.github.io/Belorae-Start-R0/
- ✅ **Repositório:** https://github.com/GPlanSB/Belorae-Start-R0 (Public)
- ✅ **Branch:** main

### Technical Details
- **Stack:** HTML5 + CSS3 (mobile-first) + JavaScript vanilla
- **Build:** Sem framework, sem bundler, sem build step
- **Hospedagem:** GitHub Pages (estático)
- **Cardápio:** PDF em `assets/cardapio/cardapio-belorae.pdf`
- **Metodologia:** Spec-Driven Development (SDD)

### Notes
- Produtos e preços no cardápio são rascunho — substituir por dados reais antes de anunciar ao público (ver `docs/TASKS.md`)
- Fotos de produtos são placeholders — substituir por fotos reais (ver `docs/TASKS.md`)
- Pronto para melhorias futuras: domínio customizado, analytics, automação de pedidos

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
