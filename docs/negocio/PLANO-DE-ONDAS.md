# Plano de Ondas do Programa de Gestão

**Responsável:** Marina (Diretora Geral / CEO do Negócio)
**Data:** 26/07/2026
**Status:** v1.1, com a Onda 1 concluída e a Onda 2 parcialmente concluída

## O que é uma "onda"

Onda é um bloco de trabalho em que alguns setores trabalham ao mesmo tempo, cada um no que é dele, e no fim eu junto tudo e verifico se as respostas conversam entre si.

A ideia é simples, e é a mesma lógica que o time técnico do site já usa: em vez de fazer setor por setor em fila (o que demora demais) ou fazer tudo de uma vez (o que vira bagunça), agrupa-se por dependência. **Setores que não precisam da resposta um do outro rodam em paralelo. Setores que precisam esperam a onda anterior.**

Exemplo prático: a Bianca (Marketing) não pode escrever "nosso brownie sem glúten custa R$ 9,00" antes de o Vitor confirmar se ele pode mesmo ser chamado de sem glúten e antes de o Renato calcular se R$ 9,00 cobre o custo. Por isso Marketing não entra na Onda 1 nem na 2.

## Visão geral das 6 ondas

| Onda | Nome | Setores | Pergunta que responde | Status |
|---|---|---|---|---|
| 1 | Fundação | Vitor, Patrícia, Renato, Helena, Otávio | O que vendemos, como se faz, o que custa, o que a lei exige | **Concluída** |
| 2 | Números reais e correção de rota | Vitor, Patrícia, Renato, Helena | Quanto custa de verdade e por quanto vender | **Parcialmente concluída** |
| 3 | Ir ao mercado | Bianca, Diego | Como contar isso e como atender quem pedir | Aguarda Onda 2 |
| 4 | Formalização executada | Otávio, Renato | Como operar dentro da lei sem quebrar o caixa | Aguarda decisão do dono |
| 5 | Estabilizar e medir | Renato, Diego, Helena, Vitor | Está dando certo? Como sabemos? | Aguarda Onda 3 |
| 6 | Crescer com estrutura | Fabiana, Vitor, Bianca, Renato | Como crescer sem perder qualidade | Aguarda Onda 5 |

---

## Onda 1: Fundação (CONCLUÍDA)

**Objetivo.** Sair do zero absoluto. Antes desta onda não existia nenhuma ficha de receita, nenhuma lista de compras, nenhum custo registrado, nenhuma regra de higiene escrita e nenhum diagnóstico legal. Existia um cardápio rascunho fictício e nada mais.

**Setores acionados, todos em paralelo:** Vitor (Produção), Patrícia (Compras e Insumos), Renato (Financeiro), Helena (Qualidade e Segurança Alimentar), Otávio (Jurídico e Regulatório).

**Por que esses cinco em paralelo.** Nenhum deles precisava da entrega do outro para começar. O Vitor podia escrever receita sem saber o preço. A Patrícia podia listar o que comprar sem saber a margem. O Renato podia montar o método de cálculo sem ter os números. A Helena podia escrever regra de higiene sem CNPJ. O Otávio podia diagnosticar formalização sem saber o custo do bolo. Rodar em sequência teria custado cinco vezes mais tempo pelo mesmo resultado.

**Entregue:** 16 documentos.

- Produção: `PORTFOLIO-PRODUTOS.md`, `FICHA-TECNICA-MODELO.md`, `FT-001-BOLO-INTEGRAL-CENOURA.md`, `FT-002-BROWNIE-FIT-AMENDOAS.md`
- Insumos: `MAPA-DE-INSUMOS.md`, `ROTEIRO-COTACAO-FORNECEDORES.md`, `POLITICA-ESTOQUE-MINIMO.md`
- Financeiro: `METODO-DE-PRECIFICACAO.md`, `MAPA-CUSTOS-FIXOS.md`, `MODELO-FLUXO-DE-CAIXA.md`
- Qualidade: `BOAS-PRATICAS-MANIPULACAO.md`, `MATRIZ-ALERGENOS-E-VALIDADE.md`, `ROTULAGEM-MODELO.md`
- Jurídico: `DIAGNOSTICO-FORMALIZACAO.md`, `LICENCAS-E-ALVARAS.md`, `LGPD-DADOS-DE-CLIENTES.md`

**Decisões tomadas nesta onda:**

1. Proposta de lançar com 3 produtos em vez de 8 (Bolo Integral de Cenoura, Brownie Fit de Amêndoas, Cookies Sem Glúten), adiando Cheesecake, Pavê e Mini Quiche por risco e complexidade, e escalonando Trufa e Bolo Vegano para uma segunda etapa. Pendente de confirmação do dono.
2. Método de preço adotado: margem sobre o preço de venda, não markup sobre o custo. Isso evita o erro mais comum de negócio iniciante, que é achar que ganha o dobro quando ganha a metade.
3. Custo da própria hora de trabalho do dono entra no preço, mesmo que ele não retire esse dinheiro hoje.
4. Toda ficha técnica em gramas e mililitros, nunca em medida caseira sozinha, porque medida caseira quebra a padronização.
5. Insumo fresco só se compra depois de pedido confirmado do cliente.

**O que a revisão de coerência encontrou (feita pela Marina ao fim da onda):**

- Os produtos "sem glúten" não podem manter essa promessa hoje, e o trio de lançamento proposto concentra esse risco em vez de reduzir. Ver Achado Crítico 1 no `README.md`.
- O mapa de insumos não cobre 5 itens que as fichas técnicas pedem (açúcar demerara, óleo de coco, fermento, sal, papel manteiga) e tem 4 contagens de uso desatualizadas.
- Falta embalagem para venda de unidade avulsa e falta embalagem para congelamento, que nesta operação também é barreira de alérgeno.
- Os custos fixos não incluem taxa de licença sanitária, taxa de alvará, curso de manipulação, abertura de CNPJ nem eventual responsável técnico. Falta uma tabela de investimento inicial, separada da de custo mensal.
- A validade do brownie definida pela Qualidade (3 a 4 dias refrigerado) contradiz a proposta da Produção (estoque em temperatura ambiente). Dos 3 produtos do lançamento, só o cookie sustenta estoque de verdade.
- Ninguém definiu validade de produto congelado, e a estratégia de estoque inteira depende disso.
- Ninguém definiu o prazo mínimo de encomenda que o cliente precisa dar, e esse número trava compras, produção e atendimento ao mesmo tempo.

**Perguntas geradas:** 78, no total dos cinco setores. Consolidadas para cerca de 42 em `PERGUNTAS-AO-DONO.md`, sendo 5 já respondidas pela própria Onda 1 e 5 suspensas por tratarem de produtos adiados.

---

## Onda 2: Números reais e correção de rota (PARCIALMENTE CONCLUÍDA)

**Objetivo.** Trocar todo `[a confirmar]` que der por número real, e corrigir o que a revisão da Onda 1 encontrou. É a onda que transforma método em preço.

**Setores:** Vitor, Patrícia, Renato (o trio que fecha o custo) mais Helena, revisando o que precisa mudar no produto.

**Por que esses quatro juntos.** Aqui existe dependência de verdade, e ela é encadeada: a Patrícia entrega o preço do insumo, o Vitor entrega o rendimento real da receita, e só então o Renato consegue calcular o custo por unidade. A Helena entra em paralelo porque o resultado dela (validade de congelado, rotina anti-contaminação, rótulo real) muda o que o Vitor pode prometer e o que a Patrícia precisa comprar.

**Como esta onda foi dividida.** A Onda 2 foi executada em duas partes. A **parte 1** reúne tudo que dava para fazer sem nenhuma resposta do dono, e foi concluída em 26/07/2026. A **parte 2** é o que só existe depois das respostas do Bloco A do `PERGUNTAS-AO-DONO.md` e das duas tarefas físicas do dono (teste de bancada e cotação). Essa divisão não estava prevista no plano original: ela apareceu porque a parte 1 se mostrou grande o bastante para render sozinha, e segurar tudo esperando o dono teria parado o programa inteiro à toa.

### Parte 1: entregue, sem depender do dono

Vitor
- [CONCLUÍDO] Correção da FT-002, removendo a afirmação de que a farinha de amêndoas garante o "sem glúten" e incluindo a declaração de traços. Ficha passou para v0.2.
- [CONCLUÍDO] FT-003 (Cookies Sem Glúten), completando o trio de lançamento, com o ponto do glúten deixado em aberto e as duas variações de aveia (comum e certificada) lado a lado.
- [CONCLUÍDO] `GLUTEN-DOIS-CAMINHOS.md`, com os dois cenários do Achado Crítico 1 e recomendação técnica pelo Caminho B.
- [CONCLUÍDO] Bloco de custo de embalagem por unidade nas três fichas técnicas.

Patrícia
- [CONCLUÍDO] Correção do `MAPA-DE-INSUMOS.md`: divergência do açúcar demerara versus adoçante resolvida, itens faltantes incluídos, contagens de uso atualizadas, insumos da FT-003 incorporados. Mapa passou para v0.2.
- [CONCLUÍDO] Três linhas novas de embalagem: unidade avulsa, embalagem hermética para congelamento e papel manteiga.

Renato
- [CONCLUÍDO] Segunda tabela no `MAPA-CUSTOS-FIXOS.md`, de investimento inicial, com a origem de cada linha nos documentos do Otávio e da Helena.
- [CONCLUÍDO] Nota de limitação no `METODO-DE-PRECIFICACAO.md` sobre o método não suportar imposto variável se a empresa deixar de ser MEI.
- [CONCLUÍDO] `PLANILHA-PRECIFICACAO.md`, estrutura pronta para os 3 produtos, com todos os campos marcados como `[a confirmar]`.

Helena
- [CONCLUÍDO] Seção de validade de produto congelado no `MATRIZ-ALERGENOS-E-VALIDADE.md`, cobrindo os 3 produtos do lançamento.
- [CONCLUÍDO] `PROCEDIMENTO-SEPARACAO-ALERGENOS.md`, com a rotina que o Vitor vai executar.
- [CONCLUÍDO] Revisão do risco do freezer como vetor de contaminação cruzada, dentro dos dois documentos acima.
- [CONCLUÍDO] `ROTULOS-LANCAMENTO.md`, com os 3 rótulos, faltando só dado nutricional e CNPJ, conforme previsto.
- [PARCIAL] Correção do travessão. Os títulos principais foram corrigidos, mas restam travessões no corpo e nos títulos de seção de `BOAS-PRATICAS-MANIPULACAO.md`, `ROTULAGEM-MODELO.md`, `MATRIZ-ALERGENOS-E-VALIDADE.md` e `ROTEIRO-COTACAO-FORNECEDORES.md`.

### O que a revisão de coerência da parte 1 encontrou (feita pela Marina)

Nove pontos, nenhum deles bloqueante, todos com correção definida:

1. O Caminho A do Vitor e o procedimento da Helena dão instruções opostas sobre produzir com e sem glúten no mesmo dia. Regra unificada decidida: a rotina da Helena (sem glúten primeiro, higienização entre, produto com glúten por último) é o piso mínimo de hoje e do Caminho B, e vale como redução de risco, não como garantia. A regra mais rígida do Vitor (dias ou turnos separados) só passa a valer se o dono escolher o Caminho A e voltar a escrever "sem glúten" no rótulo. Os dois documentos precisam registrar essa distinção.
2. O Rótulo 3 do `ROTULOS-LANCAMENTO.md` afirma que a FT-003 não existe. Ela existe. O rótulo precisa ser refeito com a lista real de ingredientes em ordem decrescente de peso e peso líquido de referência de 30 g por unidade.
3. A FT-002 ainda propõe estoque do brownie em temperatura ambiente, enquanto a Helena determinou refrigerado de 3 a 4 dias e o rótulo já foi escrito assim. Essa contradição vinha da Onda 1 e não foi corrigida.
4. As três fichas ainda marcam a validade como `[a confirmar com Helena]`, sendo que a Helena já respondeu. É um `[a confirmar]` falso.
5. O `MAPA-DE-INSUMOS.md` ainda manda cotar "mix de farinha sem glúten" para os Cookies, mas a FT-003 usa só aveia como base seca. Mesma linha sobra no Grupo 1 da `POLITICA-ESTOQUE-MINIMO.md`.
6. A embalagem hermética de congelamento está atribuída a 2 produtos no mapa, mas a Helena cobre 3, incluindo massa crua de cookie.
7. O bloco de custo de embalagem das fichas mistura embalagem de venda (por unidade) com consumível de lote (papel manteiga) e com embalagem de estoque (hermética), que não se comportam igual. Precisa virar duas linhas.
8. A tabela de investimento inicial não tem o jogo de utensílios exclusivo nem a marcação visual de zonas, que são o custo de entrada do Caminho A. Sem essas linhas, o dono compara os dois caminhos sem ver o preço de um deles.
9. A Patrícia registrou que não teve escopo para atualizar o `ROTEIRO-COTACAO-FORNECEDORES.md` e a `POLITICA-ESTOQUE-MINIMO.md`. Decisão da Marina: a lista de priorização de cotação do roteiro é corrigida agora, porque hoje ela mandaria o dono cotar insumos de produtos adiados e deixaria de fora quase todos os insumos do trio de lançamento. Os números de estoque mínimo esperam o Bloco A, porque dependem da A9 e da A12.

### Parte 2: o que falta para a Onda 2 fechar de vez

Nada aqui anda sem o dono. Cada item indica a pergunta que o destrava.

Vitor
- [PENDENTE] Rendimento e tempo reais das três fichas, depois do teste de bancada. Depende da **A14**.
- [PENDENTE] Fechar a variação de aveia da FT-003 e o nome comercial do produto. Depende da **A1**.
- [PENDENTE] Fechar o tipo exato de castanha da FT-003. Depende da **A15**.
- [PENDENTE] Correções de coerência 1, 3, 4 e 7 da lista acima (independem do dono, mas são retrabalho de documento, não entrega nova).

Patrícia
- [PENDENTE] Cotação real de pelo menos 3 fornecedores por insumo do trio. Depende da **A3** (para saber o que cotar), da **A1** e da **A4** (para saber qual variação cotar) e da ação física do dono de fazer as ligações.
- [PENDENTE] Números concretos de estoque mínimo. Depende da **A9** e da **A12**.
- [PENDENTE] Correções de coerência 5 e 6 da lista acima.

Renato
- [PENDENTE] Preencher a `PLANILHA-PRECIFICACAO.md`. Depende da cotação da Patrícia, do teste de bancada do Vitor, e das respostas **A7**, **A8**, **A9** e **A10**.
- [PENDENTE] Cálculo do ponto de equilíbrio. Depende das mesmas respostas.
- [PENDENTE] Preço de venda proposto dos 3 produtos. É a última peça da onda: só existe depois de tudo acima.
- [PENDENTE] Correção de coerência 8 da lista acima.

Helena
- [PENDENTE] Refazer o Rótulo 3 com base na FT-003 (correção 2 da lista acima).
- [PENDENTE] Fechar a redação de glúten dos três rótulos. Depende da **A1**.
- [PENDENTE] Concluir a limpeza de travessão nos quatro arquivos.
- [PENDENTE] Dado nutricional dos rótulos, que depende de nutricionista (**C4**), e razão social e CNPJ, que dependem da Onda 4.

**O que trava:** o Bloco A do `PERGUNTAS-AO-DONO.md`, que passou de 14 para 16 perguntas nesta rodada. Sem ele, a Onda 2 não fecha e a Onda 3 não começa.

---

## Onda 3: Ir ao mercado

**Objetivo.** Com produto definido, preço calculado e rótulo pronto, começar a vender de forma organizada.

**Setores:** Bianca (Marketing e Vendas) e Diego (Atendimento e Operações de Pedido), em paralelo entre si.

**Por que só agora.** Marketing e atendimento comunicam o que já está decidido. Se entrarem antes, a Bianca constrói posicionamento em cima de um produto que pode mudar de nome (ver Achado Crítico 1) e de um preço que ainda não existe, e o Diego escreve script de pedido sem saber o prazo de encomenda. Seria retrabalho garantido.

**Entregáveis previstos:**

Bianca
- Posicionamento da marca, coerente com o preço que o Renato fechou
- Calendário de conteúdo para Instagram
- Regra de promoção que respeite a margem mínima de veto do Renato
- Como comunicar honestamente o que a Belorae é, especialmente se o Caminho B do Achado Crítico 1 for escolhido

Diego
- Script de atendimento por WhatsApp, do primeiro contato ao pós-venda
- Fluxo de pedido, com o prazo mínimo de encomenda definido
- Política de entrega, incluindo Mafra e incluindo cadeia de frio quando fizer calor
- O que fazer quando um cliente reclama

**Ponto de contato com o time técnico.** É aqui que os dois times se encostam pela primeira vez: o cardápio real e os preços saem desta pasta e vão para o PDF do site, e o posicionamento da Bianca precisa combinar com a identidade visual que o time do Ricardo aplicou. O combinado continua: a Marina não decide nada de site, só entrega o conteúdo pronto.

---

## Onda 4: Formalização executada

**Objetivo.** Sair do diagnóstico e executar. Esta onda depende mais de agenda do dono com terceiros (contador, prefeitura, vigilância sanitária) do que de trabalho dos setores.

**Setores:** Otávio e Renato.

**Por que separada.** O ritmo aqui não é nosso. Depende de horário de atendimento de prefeitura e de resposta de contador. Misturar isso com a Onda 2 travaria a Onda 2 inteira à toa.

**Entregáveis previstos:**
- CNPJ aberto, com o regime escolhido (MEI ou ME) baseado em faturamento real
- Resposta definitiva sobre a questão tributária e sanitária de Mafra/SC (Achado Crítico 2)
- Licença sanitária e alvará encaminhados, com prazos e taxas conhecidos
- Curso de Boas Práticas de Manipulação concluído
- Atualização dos rótulos com razão social e CNPJ
- Revisão do método de precificação para o regime tributário escolhido
- Custo fixo mensal atualizado com os valores reais de contador, DAS e taxas

---

## Onda 5: Estabilizar e medir

**Objetivo.** Depois de um a três meses vendendo, olhar o que aconteceu de verdade e corrigir. É a primeira onda que trabalha com dado real em vez de estimativa.

**Setores:** Renato, Diego, Helena e Vitor.

**Entregáveis previstos:**
- Primeiro relatório financeiro com dado real, e ponto de equilíbrio recalculado
- Comparação entre o custo estimado na Onda 2 e o custo que aconteceu
- Revisão de preço onde a margem real ficou abaixo da planejada
- Indicadores simples de atendimento (quanto tempo para responder, quantos pedidos por semana, o que mais se vende)
- Auditoria da rotina de higiene e alérgenos: está sendo seguida na prática ou só no papel
- Revisão das fichas técnicas com o tempo e o rendimento que a produção real mostrou

**Critério de decisão desta onda.** Se o negócio estiver estável, com margem saudável e rotina que se sustenta sozinha, segue para a Onda 6. Se não estiver, repete a Onda 5 com ajustes antes de pensar em crescer. Crescer com processo instável é a forma mais rápida de perder qualidade.

---

## Onda 6: Crescer com estrutura

**Objetivo.** Aumentar capacidade sem que a qualidade caia junto.

**Setores:** Fabiana (Pessoas), Vitor, Bianca e Renato.

**Por que a Fabiana só entra agora.** Contratar antes de ter caixa previsível e processo escrito é um dos erros mais caros de negócio pequeno. Sem ficha técnica, sem rotina de higiene documentada e sem preço que cubra o custo de mão de obra, uma pessoa nova não tem como aprender nem tem como ser paga com segurança. A Fabiana entra quando existir algo para ela ensinar e dinheiro para pagar.

**Entregáveis previstos:**
- Descrição do primeiro cargo a contratar, com base no gargalo que a Onda 5 mostrar
- Checklist de contratação e de treinamento, usando as fichas técnicas e o checklist de boas práticas como material de ensino
- Reintrodução avaliada dos produtos adiados: Trufa, Bolo Vegano, Cheesecake, Pavê e Mini Quiche
- Avaliação de espaço de produção próprio, se a cozinha residencial virar limite
- Avaliação de mudança de MEI para ME, com o impacto no preço já calculado
- Expansão de canal de venda

---

## Como este plano muda

Este plano não é fixo. Ele muda quando:

- O dono muda a prioridade do negócio.
- Uma onda descobre algo que muda a ordem das seguintes, que foi exatamente o que aconteceu na Onda 1 com o achado do "sem glúten".
- Um bloqueio externo trava uma onda inteira, e faz mais sentido antecipar outra.

Toda mudança de plano é registrada aqui, com a data e o motivo. O plano existe para dar clareza sobre a ordem das coisas, não para engessar o negócio.

### Histórico de versões

| Versão | Data | O que mudou |
|---|---|---|
| v1.0 | 26/07/2026 | Criação do plano, com a Onda 1 registrada como concluída e revisada |
| v1.1 | 26/07/2026 | Onda 2 dividida em duas partes. Parte 1 (o que não dependia do dono) registrada como concluída, com 9 achados de coerência e as pendências da parte 2 amarradas às perguntas do Bloco A que as destravam |
