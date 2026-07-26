# DECISIONS.md

Registro de decisões técnicas importantes — para lembrar o "porquê" no futuro.

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

## 2026-07-25 — Imagens placeholder do Pexels, baixadas localmente

**Decisão:** Enquanto o dono do projeto não envia fotos reais dos produtos, usar 4 fotos gratuitas do banco Pexels (licença livre de uso, sem necessidade de atribuição) baixadas como arquivos reais em `assets/images/` — não hotlinkadas por URL externa.
**Arquivos:** `bolo-cenoura-placeholder.jpg`, `cookies-placeholder.jpg`, `brownie-placeholder.jpg`, `cheesecake-placeholder.jpg` — nome já indica que são temporários.
**Motivo:** Hotlink direto no domínio do Pexels criaria dependência de terceiro em runtime (site pode mudar/sumir a URL), quebrando a filosofia de site 100% estático e autossuficiente do projeto. Baixar o arquivo mantém o site funcionando independente do Pexels.
**Revisitar se:** o dono do projeto enviar fotos reais dos produtos — aí esses 4 arquivos devem ser substituídos e removidos.
