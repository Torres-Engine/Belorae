# SPEC.md — Especificação Técnica e de Produto

> Metodologia: **Spec-Driven Development (SDD)** — este documento é a fonte única da verdade do projeto. Toda implementação (atual ou reconstrução do zero) deve seguir exatamente o que está aqui. Se o código e este arquivo divergirem, o código está errado.

| Campo | Valor |
|---|---|
| Projeto | Site institucional one-page — Belorae Confeitaria Saudável |
| Versão da spec | 1.0.0 |
| Data | 2026-07-26 |
| Dono do projeto | Torres |
| Status | Aprovada — pronta para rebuild do zero |

---

## 1. Visão Geral

Site one-page cujo único objetivo é converter visitantes em pedidos via WhatsApp para a Belorae, uma confeitaria saudável (sem açúcar refinado, sem glúten quando possível) sediada em Rio Negro, PR, atendendo Mafra e região. Não é loja virtual: não há carrinho, checkout ou pagamento no site.

**Métrica de sucesso:** visitante consegue, em até 2 cliques a partir do link do site, abrir uma conversa de WhatsApp com a Belorae já com intenção de pedido clara.

---

## 2. Objetivos e Não-Objetivos

### Objetivos
- Apresentar a marca de forma profissional e coerente com a identidade visual real (não genérica).
- Levar o visitante a um pedido via WhatsApp com o mínimo de fricção.
- Disponibilizar um cardápio (PDF) com produtos, descrições e preços.
- Ser mantido por uma pessoa iniciante em programação, sem build step.

### Não-Objetivos (explicitamente fora de escopo nesta fase)
- Carrinho de compras, checkout, pagamento online.
- Login, cadastro, área do cliente.
- Painel administrativo de pedidos.
- Automação via API paga do WhatsApp Business.
- Múltiplas páginas — o site é intencionalmente uma página só.

---

## 3. Requisitos Funcionais

| ID | Requisito | Critério de aceite |
|---|---|---|
| RF-01 | Link de WhatsApp com mensagem pré-escrita vive em 3 lugares: no botão "Fazer Pedido" da seção Cardápio, no botão flutuante fixo de WhatsApp (canto inferior direito da tela) e no rodapé do PDF do cardápio | `wa.me/5541996123682?text=...` abre com o texto exato definido na seção 6.6 nos 3 pontos: botão "Fazer Pedido" (`#cardapio`), botão flutuante de WhatsApp (`.social-float`) e link clicável no rodapé do PDF (gerado por `assets/cardapio/gerar_cardapio.py`) |
| RF-02 | Seção "Cardápio" tem 2 botões lado a lado: "Fazer Pedido" (abre o WhatsApp com a mensagem da seção 6.6) e "Ver Cardápio" (abre o PDF do cardápio) | Botão "Fazer Pedido" aponta para `wa.me/5541996123682` com o texto exato da seção 6.6; botão "Ver Cardápio" aponta para `assets/cardapio/cardapio-belorae.pdf` e o arquivo existe e abre corretamente |
| RF-03 | Header exibe o logo real da marca (imagem, não texto), sobre o fundo verde da cápsula do header (v2.0) | `<img>` referenciando `assets/logo/belorae-logo-horizontal-fundo-verde.jpg`, proporção original preservada |
| RF-04 | Seção "Sobre" exibe foto da fundadora (Jaque) com legenda | `assets/images/jaque-sobre-v2.jpg` + legenda "Jaque, fundadora da Belorae" |
| RF-05 | Footer exibe cidade de atuação | Texto "Rio Negro, PR. Atendemos Mafra e região." visível no footer |
| RF-06 | Ícone de Instagram, como botão flutuante fixo no canto inferior direito da tela, linkando ao perfil da marca, com o gradiente oficial da marca Instagram (não contornado) | Link para `https://www.instagram.com/belorae_confeitaria`, abre em nova aba, `rel="noopener"`, ícone com fundo em gradiente (amarelo, laranja, rosa, roxo) igual ao símbolo oficial do Instagram |
| RF-07 | Cardápio em PDF lista todos os produtos com nome, descrição, preço e foto | Ver seção 7 — 8 itens em 4 categorias, cada um com foto quadrada |
| RF-08 | Site 100% responsivo (mobile-first) | Layout íntegro em telas de 375px a 1440px, sem scroll horizontal |
| RF-09 | Favicon reflete a marca | `<link rel="icon">` aponta para um dos ícones em `assets/logo/` |
| RF-10 | Ícone de WhatsApp com acesso direto, como botão flutuante fixo no canto inferior direito da tela, ao lado do botão flutuante de Instagram | SVG inline em verde oficial `#25D366`, linkando para `wa.me/5541996123682?text=...` com a mensagem da seção 6.6, abre em nova aba, `rel="noopener"` |

## 4. Requisitos Não-Funcionais

| ID | Requisito |
|---|---|
| RNF-01 | Zero travessão ("—") ou hífen usado como conector entre palavras em qualquer texto visível do site ou do cardápio (regra permanente, verificada pelo Ricardo antes de qualquer publicação — ver seção 9) |
| RNF-02 | Zero emojis em qualquer texto ou elemento visual do site e do cardápio |
| RNF-03 | Sem framework, sem bundler, sem build step — HTML/CSS/JS puro |
| RNF-04 | Sem backend, sem banco de dados |
| RNF-05 | Peso do PDF do cardápio menor que 5MB |
| RNF-06 | Todo texto em português do Brasil (pt-BR), inclusive metadados e `lang="pt-BR"` |
| RNF-07 | Nenhum dado pessoal real de cliente commitado no repositório |

---

## 5. Arquitetura Técnica

| Camada | Decisão | Referência |
|---|---|---|
| Frontend | HTML5 + CSS3 + JavaScript vanilla | `docs/ARCHITECTURE.md` |
| Hospedagem | GitHub Pages | `docs/DEPLOY.md` |
| Cardápio | PDF gerado por script Python (`reportlab` + `Pillow`), não escrito manualmente | `assets/cardapio/gerar_cardapio.py` |
| Contato | Link `wa.me` com mensagem pré-escrita, sem API paga | `docs/DECISIONS.md` |
| Versionamento | Git + GitHub, editado via extensão Claude Code no VS Code | `docs/DEPLOY.md` |

Diagrama de fluxo, justificativas completas e histórico de decisões: ver `docs/ARCHITECTURE.md` e `docs/DECISIONS.md` (não duplicado aqui — este documento referencia, não substitui).

---

## 6. Design System

### 6.1 Paleta de cores (variáveis CSS em `:root`)

| Token | Hex | Uso |
|---|---|---|
| `--cor-fundo` | `#FAF6EE` | Fundo principal (creme) |
| `--cor-primaria` | `#6E8763` | Verde-sálvia — botões, destaques |
| `--cor-primaria-escura` | `#4F6647` | Verde escuro — hover, CTA final, títulos |
| `--cor-texto` | `#3E2F22` | Marrom-café — texto principal |
| `--cor-acento` | `#C98A63` | Terracota — preços, acentos secundários |
| `--cor-branco` | `#FFFFFF` | Cards, contraste |

**Adendo v2.0 ("Blocos e Cápsulas", ver seção 12 e `docs/CHANGELOG.md` 1.9.0):** o redesign visual implementado pela Camila (direção de Sofia) adicionou 4 tokens novos de cor, sem redefinir nenhum dos 6 tokens acima (eles continuam com o mesmo valor de sempre):

| Token novo | Hex | Uso |
|---|---|---|
| `--cor-verde-marca` | `#4A543C` | Verde da cápsula do header e do painel da seção Cardápio (medido por pixel do arquivo `assets/logo/belorae-logo-horizontal-fundo-verde.jpg`) |
| `--cor-fundo-suave` | `#EFF1E9` | Fundo do bloco da seção Sobre |
| `--cor-texto-forte` | `#2A1F16` | Texto do botão "Fazer Pedido" (correção de contraste, ver seção 11) |
| `--cor-ouro` | `#C9A227` | Só decorativo, no glifo "raminho" sobre fundo verde; nunca usado em texto ou botão |

Também foram adicionados tokens de raio de borda (`--raio-medio`, `--raio-grande`, `--raio-bloco`, `--raio-pilula`) e de sombra, usados nos blocos arredondados do redesign. Nenhum deles substitui ou redefine cor da paleta oficial.

### 6.2 Tipografia
- Títulos: `Georgia, 'Times New Roman', serif` (site) — coerente com o logo, que usa uma serifada elegante.
- Corpo: `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif` (site).
- Cardápio em PDF: `Liberation Serif` (Regular/Bold/Italic) — serifada, sem depender de fontes externas via rede.

### 6.3 Logo — arquivos e uso correto

Todos em `assets/logo/`, qualidade original preservada (nunca redimensionar de forma que distorça a proporção):

| Arquivo | Descrição | Uso |
|---|---|---|
| `belorae-logo-vertical.jpg` | Lockup completo, fundo creme | Materiais impressos, redes sociais |
| `belorae-logo-horizontal-fundo-creme.jpg` | Horizontal, fundo claro | Materiais sobre fundo claro (fora do header, desde o redesign v2.0) |
| `belorae-logo-horizontal-fundo-verde.jpg` | Horizontal, fundo escuro | Header do site (desde o redesign v2.0, a cápsula do header é verde) e outros fundos verdes/escuros |
| `belorae-selo-circular.jpg` | Selo com "BELORAE" | Cabeçalho do cardápio em PDF |
| `belorae-icone-fundo-creme.jpg` | Ícone isolado, fundo claro | Favicon, footer |
| `belorae-icone-fundo-verde.jpg` | Ícone isolado, fundo escuro | Uso alternativo em fundos escuros |

**Regra:** nunca usar texto simulando o logo (ex: `<a class="logo">Belorae</a>` em texto puro) — sempre a imagem real.

### 6.4 Regra de conteúdo — proibição de travessão

Nenhum texto do site ou do cardápio pode usar "—" (em dash) ou "-" (hífen com espaços) como conector entre palavras (padrão "palavra - palavra"). Reescrever com ponto, vírgula, ou reestruturar a frase. Checagem obrigatória antes de qualquer publicação (ver seção 9 e `.claude/agents/ceo-orquestrador.md`).

### 6.5 Regra de conteúdo — proibição de emoji

Nenhum emoji em nenhum texto, título, botão ou elemento do site ou do cardápio.

### 6.6 Mensagem do link de WhatsApp no rodapé do PDF do cardápio (texto exato)

```
Olá! Vi o site da Belorae e quero fazer um pedido.
```

Este texto é usado no link `wa.me` em 3 lugares: no botão "Fazer Pedido" da seção Cardápio (`index.html`), no botão flutuante fixo de WhatsApp no canto inferior direito da tela (`index.html`) e no rodapé do PDF do cardápio (gerado por `assets/cardapio/gerar_cardapio.py`). A seção Cardápio (seção 7) tem 2 botões lado a lado: "Fazer Pedido" (WhatsApp) e "Ver Cardápio" (PDF); o botão flutuante é um acesso direto de contato adicional, sempre visível durante a rolagem da página, não substitui o botão da seção Cardápio.

---

## 7. Especificação de Conteúdo por Seção

| Seção | Conteúdo obrigatório | Observações |
|---|---|---|
| Header | Logo (imagem) + nav (Produtos, Sobre, Cardápio) | Sticky no topo. Sem botão de pedido/WhatsApp |
| Hero | Título + subtítulo | Sem botões. Título e subtítulo em `docs/PROJECT_SCOPE.md` / `index.html` atual |
| Produtos (destaques) | 4 cards com foto, nome, descrição curta | Fotos de exemplo hoje (Pexels) — trocar por fotos reais antes do lançamento |
| Sobre | Foto da Jaque + legenda + texto institucional | Foto real já recebida (`assets/images/jaque-sobre.jpg`) |
| Cardápio (seção do site) | Texto curto + 2 botões lado a lado: "Fazer Pedido" (abre o WhatsApp com a mensagem da seção 6.6) e "Ver Cardápio" (abre o PDF) | Não listar produtos direto no HTML — sempre via PDF. O PDF também tem o link de WhatsApp no próprio rodapé (redundância proposital: quem abre o PDF direto, sem passar pelo botão desta seção, ainda encontra o link). Desde o redesign v2.0, essa seção é um painel de fundo sólido na cor `--cor-verde-marca` (antes era um gradiente), com um glifo SVG decorativo em formato de "raminho" (símbolo `#ico-raminho`, definido inline logo após a abertura do `<body>`) acima do título |
| Footer | Ícone/marca + texto institucional + cidade de atuação + coluna de navegação | Ver RF-05. Não existe mais seção "CTA final". Os ícones de WhatsApp e Instagram não ficam mais no rodapé: são botões flutuantes fixos no canto inferior direito da tela (ver RF-06 e RF-10), visíveis durante toda a rolagem da página; desde o redesign v2.0 ficam dentro de uma única cápsula creme, em vez de soltos lado a lado. O site tem hoje 3 pontos de acesso ao WhatsApp: botão "Fazer Pedido" na seção Cardápio, botão flutuante fixo, e link dentro do rodapé do PDF. Desde o redesign v2.0, o footer tem 2 colunas: marca (logo, nome, localização) e uma coluna nova "Navegação", com os mesmos 3 links do menu do header (Produtos, Sobre, Cardápio) |

## 8. Especificação do Cardápio (PDF)

Gerado por `assets/cardapio/gerar_cardapio.py`. Estrutura de dados (categoria → itens):

| Categoria | Item | Preço | Foto |
|---|---|---|---|
| Bolos | Bolo Integral de Cenoura | Fatia R$ 12 / Inteiro R$ 65 | `assets/images/bolo-cenoura-placeholder.jpg` |
| Bolos | Bolo Vegano de Banana com Canela | Fatia R$ 12 / Inteiro R$ 60 | `assets/images/cardapio/banana-canela-placeholder.jpg` |
| Doces individuais | Brownie Fit de Amêndoas | Unidade R$ 9 / Caixa 6 R$ 48 | `assets/images/brownie-placeholder.jpg` |
| Doces individuais | Cookies Sem Glúten | Unidade R$ 7 / Pacote 4 R$ 24 | `assets/images/cookies-placeholder.jpg` |
| Doces individuais | Trufa de Cacau 70% com Castanha-do-Pará | Unidade R$ 6 / Caixa 6 R$ 32 | `assets/images/cardapio/trufa-placeholder.png` |
| Sem açúcar / diet | Cheesecake Proteico de Frutas Vermelhas | Fatia R$ 14 | `assets/images/cheesecake-placeholder.jpg` |
| Sem açúcar / diet | Pavê Fit de Morango | Porção R$ 15 | `assets/images/cardapio/pave-morango-placeholder.jpg` |
| Salgados fit | Mini Quiche de Legumes | Unidade R$ 8 / Caixa 6 R$ 42 | `assets/images/cardapio/quiche-placeholder.jpg` |

**Todos os produtos e preços acima são RASCUNHO/exemplo** — substituir pelos reais antes do lançamento (bloqueador registrado em `docs/TASKS.md`). Layout do PDF: fundo creme com moldura verde, selo circular no topo, aviso de rascunho em badge, categorias com regra verde, item = foto quadrada + nome + descrição + preço alinhado à direita, tudo em `Liberation Serif`, sem travessão, sem emoji, cabendo em 1 página A4.

---

## 9. Time de Agentes (Claude Code)

Time hierárquico completo em `.claude/agents/`, detalhado em `docs/AGENTS.md`. Resumo:

| Nome | Papel | Gate que aplica |
|---|---|---|
| Ricardo | CEO AI / Orquestrador | Aprova/reprova publicação; checagem obrigatória de travessão em todo o site e cardápio |
| Fernanda | Product Manager | Define conteúdo/textos |
| Eduardo | Solution Architect | Aprova abordagem técnica mais simples |
| Marcos | Backend & Database Guardian | Veta backend/banco desnecessário |
| Sofia | UX/UI Designer | Define direção visual antes da implementação e revisa polimento depois; cobra padrão premium, nunca amador |
| Camila | Frontend Engineer | Implementa HTML/CSS/JS |
| Rafael | QA Engineer | Testa fluxo de conversão antes de liberar |
| Beatriz | Security Engineer | Revisa dados sensíveis e credenciais |
| Lucas | DevOps Engineer | Publica no GitHub Pages |
| Juliana | Technical Writer | Mantém documentação atualizada |

---

## 10. Estrutura de Arquivos (alvo)

```
index.html
css/style.css
js/script.js
assets/
  logo/            (6 arquivos, ver 6.3)
  images/          (fotos de produtos e da fundadora)
    cardapio/        (fotos de exemplo específicas do cardápio)
  cardapio/
    cardapio-belorae.pdf
    gerar_cardapio.py
    LEIA-ME.md
.claude/agents/    (9 arquivos de agente)
docs/
  PROJECT_SCOPE.md, ARCHITECTURE.md, ROADMAP.md, TASKS.md,
  DECISIONS.md, CHANGELOG.md, DEPLOY.md, AGENTS.md,
  CARDAPIO-RASCUNHO.md
CLAUDE.md
README.md
SPEC.md            (este arquivo)
```

---

## 11. Critérios de Aceite Globais (Definition of Done)

Publicação só é aprovada quando **todos** os itens abaixo forem verdadeiros:

- [ ] Zero travessão/hífen-conector em qualquer texto do site ou do cardápio (RNF-01)
- [ ] Zero emoji em qualquer lugar (RNF-02)
- [ ] Logo real aplicado no header, footer e favicon (RF-03, RF-09)
- [ ] Foto da Jaque na seção Sobre (RF-04)
- [ ] Footer com cidade de atuação (RF-05); botões flutuantes fixos de WhatsApp e Instagram no canto inferior direito da tela (RF-06, RF-10)
- [ ] Seção Cardápio com os 2 botões lado a lado, "Fazer Pedido" e "Ver Cardápio", ambos funcionando (RF-02)
- [ ] Cardápio em PDF abre corretamente, com fotos, sem travessão (RF-07)
- [ ] Mensagem do link de WhatsApp exatamente como a seção 6.6, nos 3 pontos: botão "Fazer Pedido", botão flutuante fixo do site e rodapé do PDF (RF-01)
- [ ] Responsivo sem quebra em mobile (RF-08)
- [ ] QA (Rafael) testou o fluxo completo
- [ ] Security (Beatriz) revisou dados sensíveis
- [ ] Nenhum bloqueador aberto em `docs/TASKS.md` que impeça lançamento

---

## 12. Plano de Execução — Rebuild do Zero (em ondas)

Execução organizada em **ondas**: dentro de uma onda, os agentes trabalham em paralelo (tarefas independentes entre si); uma onda só começa depois que **todos** os agentes da onda anterior aprovarem. O Ricardo é quem monta e anuncia as ondas — não precisa esperar um agente terminar pra começar outro se os dois não dependem um do outro.

| Onda | Agentes (em paralelo dentro da onda) | O que fazem | Depende de |
|---|---|---|---|
| 1 | **Eduardo** + **Fernanda** + **Marcos** | Eduardo confirma viabilidade técnica sem desvio de arquitetura · Fernanda confirma que o conteúdo das seções 6 e 7 está completo e sem ambiguidade · Marcos confirma que nada exige backend/banco de dados | Nada — os três avaliam o `SPEC.md` de forma independente |
| 2 | **Camila** (sozinha) | Reconstrói `index.html`, `css/style.css` e `js/script.js` do zero, seção por seção do `SPEC.md` — não reaproveitar código antigo sem revisar contra a spec | Onda 1 completa (os 3 aprovarem) |
| 3 | **Rafael** + **Beatriz** + **Ricardo** | Rafael testa contra o checklist da seção 11 · Beatriz revisa dados sensíveis e credenciais · Ricardo roda a checagem de travessão/emoji (seções 6.4, 6.5) em todo o site e cardápio | Onda 2 completa (Camila entregar) |
| 4 | **Lucas** (sozinho) | Publica no GitHub Pages | Onda 3 completa (os 3 aprovarem, zero pendência) |
| 5 | **Juliana** (sozinha) | Atualiza `docs/CHANGELOG.md` com a versão do rebuild e confirma que README/CLAUDE.md refletem o estado novo | Onda 4 completa (Lucas publicar) |

Regra geral pro Ricardo (vale pra esse rebuild e pra qualquer tarefa futura): antes de sequenciar um agente atrás do outro, perguntar "esse agente depende do resultado do anterior, ou só estou esperando por hábito?" — se não depender, roda junto, na mesma onda.

## 13. Pendências do dono do negócio (bloqueiam lançamento, não a spec)

- Número de WhatsApp real: já definido (`5541996123682`).
- Produtos, sabores e preços reais do cardápio (hoje é rascunho).
- Fotos reais dos produtos (hoje são fotos de exemplo do banco Pexels).

## 14. Rastreabilidade

Este documento resume decisões já registradas em detalhe em: `docs/DECISIONS.md` (histórico completo), `docs/CHANGELOG.md` (versões), `docs/ARCHITECTURE.md` (justificativas técnicas), `docs/AGENTS.md` (time de agentes). Em caso de dúvida sobre "por quê" uma decisão foi tomada, consultar `docs/DECISIONS.md` antes de alterar o que está aqui.
