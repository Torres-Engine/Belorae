# DECISIONS.md

Registro de decisões técnicas importantes — para lembrar o "porquê" no futuro.

## 2026-07-26 — Salgados voltam ao cardápio (supera decisão anterior)

**Contexto:** Na mesma rodada de reestruturação do cardápio (ver decisão "Cardápio reestruturado com base em referência de mercado", acima), a categoria "Salgados" tinha sido removida do escopo.
**Decisão:** O dono do projeto pediu para incluir 2 itens salgados específicos: Mini Pão Sírio de Frango com Alface, Requeijão e Cenoura, e Sanduíche Natural em 2 sabores (frango e atum).
**Motivo:** Não deixar de atender esse público de cliente, mesmo com o foco principal do cardápio em doces.
**Revisitar se:** o negócio quiser expandir ainda mais a linha salgada no futuro.

## 2026-07-26 — Cardápio reestruturado com base em referência de mercado

**Contexto:** O dono do projeto trouxe o cardápio de uma confeitaria saudável concorrente como referência e pediu para usar como inspiração para definir o cardápio real da Belorae.
**Decisão:** Cardápio reorganizado em 4 categorias (Bolos, Brownies, Bolachas, Doces e Brigadeiros), com nomes, descrições, preços e fotos próprios da Belorae, sem copiar texto do concorrente. Categorias "Sem açúcar / diet" e "Salgados" removidas do escopo desta rodada.
**Motivo:** O dono decidiu focar primeiro nas categorias mais centrais da confeitaria (doces assados e brigadeiros), deixando salgados para uma fase futura.
**Revisitar se:** o negócio decidir entrar em salgados, ou se quiser adicionar uma linha "zero açúcar" separada como o concorrente tem.

## 2026-07-26 — Redesign visual "v2.0 — Blocos e Cápsulas"

**Contexto:** O dono do projeto trouxe uma referência visual de outro site/layout que gostou: blocos arredondados, cápsulas flutuantes e painéis de cor sólida, em vez do estilo anterior de "faixas empilhadas" (seções retangulares simples, uma embaixo da outra).
**Decisão:** Aplicar esse estilo de layout ao site da Belorae, mantendo a paleta de cores oficial (SPEC.md 6.1) intacta. O header virou uma cápsula sólida verde flutuante e sticky; o hero ganhou uma foto grande com chips flutuantes; os cartões de produto viraram horizontais em mobile; a seção Sobre ganhou um bloco de fundo suave com moldura na foto da Jaque; a seção Cardápio virou um painel de cor sólida com um glifo decorativo; o rodapé virou um bloco com 2 colunas (marca + navegação); e os botões flutuantes de contato passaram a ficar dentro de uma única cápsula. Para viabilizar isso sem redefinir as cores oficiais, foram adicionados 4 tokens novos (`--cor-verde-marca`, `--cor-fundo-suave`, `--cor-texto-forte`, `--cor-ouro`) mais tokens de raio e sombra.
**Motivo:** O dono do projeto queria o visual mais moderno e "premium" da referência trazida, sem perder a identidade de cores já aprovada da Belorae (a mesma preocupação que motivou a criação da Sofia como agente). Sofia adaptou a referência à paleta existente, em vez de simplesmente copiar as cores da referência.
**Detalhe:** Direção visual de Sofia, implementação de Camila, aprovado por Rafael (QA) sem bloqueadores; correção de contraste do botão "Fazer Pedido" (estava abaixo do mínimo AA) feita na mesma entrega, usando o novo token `--cor-texto-forte`.
**Revisitar se:** o dono do projeto trouxer uma nova referência visual, ou se algum elemento do redesign (por exemplo, o painel sólido da seção Cardápio) se mostrar menos eficaz para conversão do que o formato anterior.

## 2026-07-26 — Criação do Time de Negócio (separado do time técnico)

**Decisão:** Criar um segundo time de 9 agentes (Marina, CEO do Negócio, mais 8 setores: Vitor, Patrícia, Renato, Bianca, Diego, Helena, Otávio, Fabiana), independente do time técnico que cuida do site.
**Motivo:** O time técnico (Ricardo e equipe) cuida só do site. O negócio em si (produção, insumos, financeiro, marketing, atendimento, qualidade, jurídico, pessoas) precisa da própria estrutura de documentação e decisão, do zero até a operação completa.
**Objetivo declarado:** transformar a Belorae na melhor confeitaria saudável da região, com toda a operação documentada e estruturada, não só o site.
**Revisitar se:** algum setor virar redundante para o tamanho do negócio, ou se surgir necessidade de mais um setor (ex: expansão para outra cidade).

## 2026-07-25 — Site estático, sem backend

**Decisão:** HTML/CSS/JS puro, sem framework, sem backend, sem banco de dados.
**Motivo:** Site é só página de conversão para WhatsApp; não guarda dados. Backend seria custo/complexidade sem retorno nesta fase.
**Revisitar se:** o negócio precisar de pagamento online, cadastro de clientes ou painel de pedidos.

## 2026-07-25 — Adição da Sofia (UX/UI Designer) ao time

**Decisão:** Novo agente dedicado só a julgamento visual/UX, com padrão de exigência alto (nível agência premium), posicionado antes de Camila implementar (define direção) e depois (revisão de polimento).
**Motivo:** Nenhum agente existente tinha como responsabilidade central "isso está no nível profissional que a marca merece" — Fernanda define conteúdo, Camila implementa, mas ninguém tinha a palavra final sobre hierarquia visual, espaçamento e consistência de marca.
**Revisitar se:** o site atingir maturidade visual estável e as revisões da Sofia pararem de gerar mudanças relevantes.

## 2026-07-25 — WhatsApp via link `wa.me`, sem API paga

**Decisão:** Botão de pedido usa link `wa.me` com mensagem pré-escrita, não a API oficial do WhatsApp Business.
**Motivo:** Grátis, sem aprovação da Meta, sem servidor. Suficiente para o volume inicial de uma confeitaria começando do zero.
**Revisitar se:** o volume de pedidos justificar automação/bot de atendimento.

## 2026-07-25 — Cardápio em PDF, separado do código

**Decisão:** Cardápio é um arquivo PDF em `assets/cardapio/`, não uma lista de produtos codificada no HTML.
**Motivo:** O dono do negócio pode atualizar preços/produtos trocando o PDF, sem precisar mexer em código ou pedir ajuda técnica toda vez.

## 2026-07-25 — Hospedagem no GitHub Pages

**Decisão:** Deploy via GitHub Pages.
**Motivo:** Gratuito, integrado ao Git/VS Code, deploy automático a cada push, fácil de conectar domínio próprio depois.

## 2026-07-25 — Time hierárquico de subagentes (Claude Code)

**Decisão:** Criar 9 subagentes em `.claude/agents/` (CEO AI, Product Manager, Solution Architect, Backend & Database Guardian, Frontend Engineer, QA Engineer, Security Engineer, DevOps Engineer, Technical Writer), cada um com escopo fechado, revisando o trabalho do anterior na cadeia.
**Motivo:** Padronizar qualidade e evitar retrabalho/scope creep num projeto conduzido por alguém iniciante em programação — cada etapa tem um "gate" de revisão antes de seguir adiante.
**Detalhe:** Backend & Database Guardian tem escopo intencionalmente pequeno hoje (o projeto não usa backend/banco) — função principal é vetar complexidade desnecessária, não construir.
**Revisitar se:** o time de agentes ficar redundante para o tamanho do projeto, ou se o negócio crescer a ponto de precisar de backend/banco de dados de verdade.

## 2026-07-25 — Agentes ganharam nomes próprios

**Decisão:** Cada subagente passou a ter um nome próprio comum, além do cargo: Ricardo (CEO AI), Fernanda (Product Manager), Eduardo (Solution Architect), Marcos (Backend & Database Guardian), Camila (Frontend Engineer), Rafael (QA Engineer), Beatriz (Security Engineer), Lucas (DevOps Engineer), Juliana (Technical Writer).
**Motivo:** Facilitar reconhecer qual agente está atuando durante uma conversa no VS Code (mais natural que lembrar slugs técnicos). Os arquivos em `.claude/agents/` mantêm o nome do cargo (ex: `product-manager.md`); só o campo `name` interno e as referências cruzadas entre agentes mudaram.

## 2026-07-25 — Um único botão no site; link de WhatsApp passa a viver no PDF do cardápio

**Contexto:** O site tinha 3 pontos de CTA de WhatsApp (header, hero e seção final), mais um botão separado "Ver Cardápio". Eram vários botões repetindo a mesma ação, e o cardápio em PDF não tinha nenhum link de contato.
**Decisão:** Remover os 3 botões de WhatsApp do site (header, hero, CTA final) e deixar só um botão no site inteiro: "Ver Cardápio", na seção do cardápio, perto do rodapé. O link de WhatsApp passou a ficar no rodapé do PDF do cardápio (`assets/cardapio/gerar_cardapio.py`), não mais no `index.html`.
**Motivo:** Simplificar o caminho do visitante: site abre o cardápio, a pessoa decide o que quer e pede pelo WhatsApp direto do PDF. Menos botões repetidos para manter, `js/script.js` ficou vazio (nenhum botão no site precisa mais de JavaScript).
**Revisitar se:** o dono do projeto perceber queda em pedidos pelo WhatsApp (por exemplo, se muita gente não abrir o PDF até o fim) — nesse caso, pode fazer sentido voltar a ter um botão de WhatsApp direto no site.

## 2026-07-26 — Reversão parcial: ícone de WhatsApp de volta no rodapé do site

**Contexto:** O dono do projeto revisou o site ao vivo depois da decisão anterior ("Um único botão no site; link de WhatsApp passa a viver no PDF do cardápio") e percebeu que a fricção para contatar via WhatsApp ficou grande demais: o cliente precisava abrir o PDF do cardápio e rolar até o rodapé para encontrar o link.
**Decisão:** O botão único "Ver Cardápio" continua exatamente igual, como o CTA principal da seção de cardápio. O que muda é o rodapé (`footer`) do site, que ganhou de volta um ícone de WhatsApp com acesso direto (mesmo link `wa.me` e mensagem da seção 6.6 do `SPEC.md`), ao lado de um ícone de Instagram (antes era só um link de texto). Não são os 3 botões de WhatsApp removidos anteriormente (header, hero, CTA final) — é uma posição mais discreta, de contato/rede social no rodapé, não um CTA duplicado no topo do site.
**Motivo:** Equilíbrio entre a simplicidade visual que motivou a decisão original (evitar vários botões repetindo a mesma ação) e a necessidade prática de não esconder demais o canal principal de conversão do negócio.
**Revisitar se:** depois de publicado, ainda parecer que poucas pessoas usam o ícone do rodapé — nesse caso, considerar um CTA adicional mais visível.

## 2026-07-26 — Segunda reversão parcial: botão "Fazer Pedido" de volta na seção Cardápio + Instagram com gradiente oficial

**Contexto:** Mesmo depois do ícone de WhatsApp voltar ao rodapé (decisão de 2026-07-26 acima), o dono do projeto avaliou o site ao vivo de novo e achou que o acesso ao WhatsApp ainda estava pouco visível: o ícone do rodapé é pequeno e fica só no fim da página, longe de onde a pessoa decide pedir (a seção do cardápio).
**Decisão:** A seção "Cardápio" ganhou um segundo botão, "Fazer Pedido", posicionado ao lado do botão "Ver Cardápio" (não substitui, os dois coexistem lado a lado num painel visual novo). "Fazer Pedido" abre o WhatsApp direto, com a mesma mensagem da seção 6.6 do `SPEC.md`. Além disso, o ícone de Instagram do rodapé deixou de ser contornado na cor verde da Belorae (recomendação anterior da Sofia) e passou a usar o gradiente oficial da marca Instagram (amarelo, laranja, rosa, roxo), por preferência explícita do dono do projeto.
**Motivo:** O dono do projeto decidiu que o WhatsApp precisa de um acesso mais direto e visível do que só o ícone discreto do rodapé, já que é o único caminho de conversão em pedido do site. Sobre o Instagram, a preferência foi estética: o dono quis o ícone reconhecível no padrão visual que todo mundo já associa ao Instagram, em vez de uma versão customizada na cor da marca.
**Detalhe:** Desenhado por Sofia, implementado por Camila, aprovado por Rafael (QA, só com ressalva de desalinhamento do `SPEC.md`, já corrigida nesta rodada) e por Beatriz (Security, sem ressalvas). Decisão de produto tomada diretamente pelo dono do projeto, sem necessidade de nova aprovação de conteúdo.
**Revisitar se:** o dono do projeto perceber que os 2 botões lado a lado ficam confusos ou redundantes na prática (por exemplo, se a maioria clicar direto em "Fazer Pedido" sem nunca abrir o cardápio) — nesse caso, vale reavaliar se o "Ver Cardápio" ainda é necessário nessa posição.

## 2026-07-26 — Ícones de WhatsApp e Instagram viram botões flutuantes fixos (saem do rodapé)

**Contexto:** Os ícones de WhatsApp e Instagram ficavam dentro do rodapé (`footer`) do site, junto com o texto da marca e a localização. Isso significava que só apareciam para quem rolava a página até o fim.
**Decisão:** Os ícones saíram do rodapé e passaram a ser botões flutuantes fixos no canto inferior direito da tela (`.social-float`), visíveis durante toda a rolagem da página, com uma animação sutil de entrada ao carregar. O rodapé continua existindo, mas agora só com logo, nome da marca e localização.
**Motivo:** O dono do projeto pediu acesso mais rápido ao contato, sem precisar rolar até o fim da página. Botões flutuantes sempre visíveis reduzem a fricção de quem quer chamar no WhatsApp ou ver o Instagram a qualquer momento da visita.
**Detalhe:** Projetado por Sofia, implementado por Camila, aprovado por Rafael (QA) e Beatriz (Security), sem bloqueadores. Inclui suporte a `prefers-reduced-motion`, respeito à área segura de iPhones (`safe-area-inset`), ocultação na impressão (`@media print`) e espaço reservado no rodapé mobile para não sobrepor conteúdo.
**Revisitar se:** os botões flutuantes atrapalharem a leitura de algum conteúdo em telas muito pequenas, ou se o dono do projeto preferir voltar a ter os ícones só no rodapé.

## 2026-07-25 — Imagens placeholder do Pexels, baixadas localmente

**Decisão:** Enquanto o dono do projeto não envia fotos reais dos produtos, usar 4 fotos gratuitas do banco Pexels (licença livre de uso, sem necessidade de atribuição) baixadas como arquivos reais em `assets/images/` — não hotlinkadas por URL externa.
**Arquivos:** `bolo-cenoura-placeholder.jpg`, `cookies-placeholder.jpg`, `brownie-placeholder.jpg`, `cheesecake-placeholder.jpg` — nome já indica que são temporários.
**Motivo:** Hotlink direto no domínio do Pexels criaria dependência de terceiro em runtime (site pode mudar/sumir a URL), quebrando a filosofia de site 100% estático e autossuficiente do projeto. Baixar o arquivo mantém o site funcionando independente do Pexels.
**Revisitar se:** o dono do projeto enviar fotos reais dos produtos — aí esses 4 arquivos devem ser substituídos e removidos.
