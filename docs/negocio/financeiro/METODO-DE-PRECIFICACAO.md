# Método de Precificação da Belorae

**Setor:** Financeiro
**Responsável:** Renato (Controller Financeiro)
**Data:** 26/07/2026
**Status:** rascunho v0.1

---

## Por que este documento existe

Hoje a Belorae não tem nenhum preço calculado formalmente, nenhum custo registrado em lugar nenhum. Este documento ensina, passo a passo, como transformar "quanto custou fazer" em "quanto cobrar", de um jeito que qualquer pessoa (mesmo sem formação em gestão) consegue refazer sozinha, com papel e caneta ou uma planilha simples.

Tudo aqui é **método**. Os números usados como exemplo são **fictícios**, só para mostrar a conta funcionando. Nenhum valor abaixo é preço real da Belorae.

---

## 1. A fórmula completa

```
Preço de venda = Custo de insumo
                + Custo de embalagem
                + Custo de mão de obra (tempo do dono)
                + Rateio de custo fixo
                + Margem alvo
```

Cada peça está explicada abaixo. No fim, um exemplo numérico completo.

### 1.1 Custo de insumo por unidade

É quanto custam os ingredientes que entram em UMA unidade do produto (uma fatia, um brownie, uma caixa de 6 trufas etc.), não a receita inteira.

Como calcular: pegue o custo de cada ingrediente na quantidade que a receita usa, some tudo, e divida pelo número de unidades que a receita rende.

Exemplo: se uma receita de brownie gasta R$ 30,00 de ingredientes (farinha de amêndoas, adoçante, ovos, chocolate) e rende 10 unidades, o custo de insumo por unidade é R$ 30,00 ÷ 10 = **R$ 3,00**.

Este número depende diretamente da ficha técnica que o Vitor (Produção) monta e da cotação de fornecedor que a Patrícia (Compras) levanta. O Renato não inventa esse valor, ele recebe pronto e usa na conta.

### 1.2 Custo de embalagem

Caixa, saquinho, etiqueta, fita, papel de forminha. Some o custo de cada item de embalagem usado por unidade vendida.

Termo importante: **custo unitário de embalagem**. Não é o preço da caixa de 100 sacos, é quanto desse pacote foi gasto em UMA venda (preço da caixa de 100 sacos dividido por 100, por exemplo).

### 1.3 Custo de mão de obra (o item que todo iniciante esquece)

Este é o erro mais comum de quem começa um negócio caseiro: **não colocar um valor para a própria hora de trabalho**, porque "eu não me pago mesmo, é meu negócio". Isso faz o preço mentir: parece que o produto dá lucro, mas na verdade só está pagando o material, e o dono está trabalhando de graça (ou pior, no prejuízo, se contar o desgaste do tempo e do equipamento).

Como calcular:
1. Defina um valor por hora que o seu tempo vale (mesmo que hoje você não retire esse dinheiro de fato). Pode ser baseado no que você ganharia em um emprego equivalente, ou um valor mínimo que faça sentido para o seu padrão de vida. Este valor é uma decisão do dono, não um cálculo financeiro. **[a confirmar]**
2. Cronometre (ou estime) quanto tempo leva para produzir um lote do produto, do preparo até a embalagem pronta.
3. Divida (valor por hora x horas gastas) pelo número de unidades do lote.

Exemplo: se o dono define seu tempo em R$ 20,00/hora, e um lote de 10 brownies leva 1 hora e 30 minutos (1,5 hora) do preparo até embalar, o custo de mão de obra do lote é R$ 20,00 x 1,5 = R$ 30,00. Dividido por 10 unidades = **R$ 3,00 por unidade**.

Importante: colocar esse valor no preço não significa que o dinheiro vai sair do caixa hoje. Significa que o preço reflete a realidade, e o dono sabe, com clareza, quanto do "lucro" aparente é na verdade salário dele mesmo.

### 1.4 Rateio de custo fixo

**Custo fixo** é todo gasto que existe independente de quanto você vende (aluguel ou parte da conta de casa, internet, energia, gás, taxa de maquininha fixa, contador, MEI). O detalhamento completo desses custos está no documento `MAPA-CUSTOS-FIXOS.md`, que também está nesta pasta.

**Rateio** é a palavra técnica para "dividir um custo entre várias coisas de forma proporcional". Aqui, significa pegar o total de custo fixo do mês e dividir pela quantidade de produtos que você espera vender naquele mês, para descobrir quanto cada unidade vendida precisa "carregar" desse custo fixo.

Fórmula do rateio:
```
Rateio de custo fixo por unidade = Custo fixo total do mês ÷ Quantidade total de unidades vendidas no mês
```

Exemplo: se o custo fixo total do mês é R$ 800,00 (exemplo fictício) e a expectativa é vender 200 unidades no mês (somando todos os produtos), o rateio é R$ 800,00 ÷ 200 = **R$ 4,00 por unidade**.

Este número é sensível: se você vender menos do que o esperado, cada unidade carrega mais custo fixo do que o previsto, e a margem real cai. Por isso o ponto de equilíbrio (quanto vender por mês para cobrir os custos fixos) é calculado à parte, em relatório específico do Renato.

### 1.5 Margem alvo

**Margem** é a fatia do preço de venda que sobra como lucro depois de pagar todos os custos (insumo, embalagem, mão de obra, rateio de fixo). Ela é sempre calculada em cima do **preço de venda**, não em cima do custo.

**Margem alvo** é a margem que o dono decide que quer ter, em porcentagem, antes de calcular o preço final. Este número é uma decisão de negócio, não um dado técnico. Um ponto de partida comum para confeitaria artesanal é entre 30% e 50% de margem, mas o valor certo para a Belorae depende de quanto o dono precisa tirar do negócio e do que o mercado local aceita pagar. **[a confirmar]**

---

## 2. Markup x Margem: o erro número 1 de quem começa

Estes dois termos parecem a mesma coisa e não são. Confundir os dois é a causa mais comum de negócio pequeno que "vende bastante" e mesmo assim não sobra dinheiro no fim do mês.

- **Margem**: porcentagem do PREÇO DE VENDA que é lucro. Fórmula: Margem = (Preço de venda − Custo total) ÷ Preço de venda.
- **Markup**: multiplicador aplicado sobre o CUSTO para chegar ao preço de venda. Fórmula: Preço de venda = Custo total x Markup.

Por que isso importa: um markup de 2x (dobrar o custo) parece gerar 100% de lucro, mas na verdade gera 50% de margem, não 100%. Isso acontece porque o markup é calculado sobre o custo (que é o número menor) e a margem é calculada sobre o preço de venda (que é o número maior).

Exemplo numérico fictício:
- Custo total do produto: R$ 10,00
- Markup de 2x: Preço de venda = R$ 10,00 x 2 = R$ 20,00
- Margem real desse preço: (R$ 20,00 − R$ 10,00) ÷ R$ 20,00 = 0,50 = **50% de margem**, não 100%.

Neste documento, sempre que falarmos em "margem alvo de X%", estamos falando de margem sobre o preço de venda, não markup sobre o custo. Isso evita o erro de achar que está ganhando o dobro quando na verdade está ganhando a metade.

---

## 3. Fórmula do preço com margem (não confundir com markup)

Para embutir corretamente uma margem alvo sobre o preço de venda (e não um markup sobre o custo), a conta é:

```
Preço de venda = Custo total ÷ (1 − Margem alvo)
```

Onde "Custo total" é a soma de insumo + embalagem + mão de obra + rateio de custo fixo, e "Margem alvo" é a porcentagem em decimal (30% = 0,30).

---

## 4. Exemplo numérico completo (FICTÍCIO, não é dado real da Belorae)

Suponha um produto fictício chamado "Doce Exemplo X", só para ilustrar a conta:

| Item | Valor |
|---|---|
| Custo de insumo por unidade | R$ 3,00 |
| Custo de embalagem por unidade | R$ 1,00 |
| Custo de mão de obra por unidade | R$ 3,00 |
| Rateio de custo fixo por unidade | R$ 4,00 |
| **Custo total por unidade** | **R$ 11,00** |
| Margem alvo definida pelo dono | 35% (0,35) |

Cálculo do preço:
```
Preço de venda = R$ 11,00 ÷ (1 − 0,35)
Preço de venda = R$ 11,00 ÷ 0,65
Preço de venda = R$ 16,92
```

Conferindo a margem: (R$ 16,92 − R$ 11,00) ÷ R$ 16,92 = R$ 5,92 ÷ R$ 16,92 = 0,35 = 35%. A conta bate.

Na prática, o dono provavelmente arredondaria esse preço para R$ 17,00 ou R$ 16,90, por facilidade de cobrar e de dar troco. Arredondar para cima é seguro (mantém ou aumenta a margem); arredondar para baixo reduz a margem e deve ser evitado sem recalcular.

---

## 5. Margem mínima e poder de veto

Este é um limite de proteção do negócio: **margem mínima é o piso abaixo do qual um produto não pode ser vendido, nem em promoção**, porque abaixo dele o negócio está, na prática, pagando para vender (mesmo que o preço pareça positivo, ele não cobre o custo real quando conta mão de obra e rateio de fixo).

Enquanto o dono não define esse número, a regra de trabalho do Renato é: **nenhuma promoção pode reduzir a margem de um produto para abaixo de 15%** (valor de segurança provisório, sujeito a confirmação do dono). Qualquer promoção da Bianca (Marketing) que empurre um produto para margem menor que isso deve ser vetada pelo Renato antes de ir ao ar, com uma alternativa proposta (por exemplo, desconto menor, ou desconto só a partir de um volume mínimo de compra).

Valor definitivo da margem mínima da Belorae: **[a confirmar]**.

---

## 6. Limitação conhecida: o que muda se a Belorae deixar de ser MEI

Isto não é um erro a corrigir agora. É um aviso registrado com antecedência, para o dia em que a pergunta aparecer de verdade.

Hoje, no item 1.4 (Rateio de custo fixo), o método trata o imposto do negócio (a guia DAS do MEI) como parte do custo fixo mensal, dentro do `MAPA-CUSTOS-FIXOS.md` (linha "Anuidade / taxa MEI"). Isso está correto **enquanto a Belorae for MEI**, porque no MEI o imposto é, de fato, um valor fixo por mês, igual chova ou faça sol de vendas.

O problema é que isso deixa de ser verdade se a Belorae crescer e precisar virar Microempresa (ME) dentro do Simples Nacional, conforme explicado pelo Otávio em `docs/negocio/juridico/DIAGNOSTICO-FORMALIZACAO.md`. No regime do Simples Nacional para ME, o imposto passa a ser calculado como um **percentual sobre o faturamento** (quanto mais vende, mais imposto paga em valor absoluto, e a alíquota também pode mudar por faixa de faturamento). Ou seja, o imposto vira **variável**, não fixo.

A fórmula deste documento, do jeito que está hoje, **não tem onde encaixar um custo variável por venda**. Ela soma custo fixo rateado (uma vez por unidade, calculado antes da venda acontecer) com custo de insumo, embalagem e mão de obra (também por unidade). Um percentual sobre o faturamento não é rateável da mesma forma, porque ele muda conforme o preço final e conforme a faixa de faturamento do mês, não conforme uma divisão simples de custo fixo por quantidade estimada.

Mesma lógica se aplica a qualquer tributação adicional sobre venda interestadual (Rio Negro/PR para Mafra/SC), apontada pelo Otávio no mesmo diagnóstico como uma questão real, ainda sem resposta confirmada de alíquota ou mecanismo. Se essa tributação existir e for cobrada por venda (por exemplo, um percentual de ICMS interestadual embutido na nota fiscal de cada pedido entregue em Mafra), ela também é variável por venda, e também não tem onde encaixar na fórmula atual.

**O que fica registrado como limitação conhecida, não como correção imediata:**

1. Enquanto a Belorae for MEI, a fórmula atual (custo fixo rateado incluindo a guia DAS) continua válida e não precisa mudar.
2. No dia em que a Belorae deixar de ser MEI e virar ME no Simples Nacional, este método precisa ser revisado para separar dois tipos de custo: custo fixo rateado por unidade (o que continua nesta fórmula) e um percentual variável sobre o preço de venda (que precisa entrar como uma nova etapa da fórmula, aplicada depois de definido o preço, não rateado por unidade estimada).
3. Se e quando existir clareza sobre uma tributação específica de venda interestadual para Mafra, SC (hoje sem alíquota nem mecanismo confirmado, conforme o Otávio), essa mesma lógica de "percentual variável por venda" se aplica, e o método também precisa ser revisado naquele momento.
4. Até lá, este documento não deve ser tratado como pronto para o cenário de ME ou de tributação interestadual confirmada. Ele está pronto apenas para o cenário atual (MEI, sem tributação interestadual confirmada).

---

## Premissas assumidas

**Sobre o método:**
1. Assumi que a fórmula de precificação da Belorae segue o modelo "custo total dividido por (1 menos margem alvo)", que calcula margem sobre o preço de venda, e não markup sobre o custo. Isso porque é a forma que evita o erro de subestimar a margem real, que é o problema mais comum em negócios iniciantes.
2. Assumi que "custo de mão de obra" deve entrar no preço mesmo que o dono não retire esse valor do caixa hoje, porque sem isso o preço não reflete o custo real do produto e o dono não consegue saber se está de fato lucrando ou só cobrindo material.
3. Assumi um valor provisório de 15% como margem mínima de veto até o dono definir o número real, para que o processo de revisão de promoções já tenha um critério objetivo desde a primeira semana.

**Sobre os exemplos numéricos:**
4. Todos os valores de custo, tempo e margem usados nos exemplos ("Doce Exemplo X", R$ 30,00 de ingredientes, R$ 20,00/hora etc.) são fictícios, criados só para demonstrar a mecânica do cálculo. Nenhum é preço, custo ou tempo real medido na Belorae.

## Perguntas para o dono responder

**Sobre o valor da hora do dono:**
1. Qual valor por hora você quer usar para o seu próprio tempo de trabalho na cozinha? Sem esse número, todo cálculo de custo de mão de obra fica incompleto, porque é uma decisão pessoal (não existe fórmula que descubra isso sozinha).
2. Você já cronometrou quanto tempo leva para produzir um lote de cada um dos 8 produtos do cardápio, do preparo até a embalagem pronta? Sem esse dado, o Renato não consegue calcular o custo de mão de obra real de cada produto, só de exemplos fictícios.

**Sobre margem:**
3. Qual margem alvo (em %) você quer ter em cada produto, ou pelo menos em média no cardápio? Este número define o preço final de tudo, e hoje não existe nenhuma referência registrada.
4. Você concorda com 15% como margem mínima de veto (abaixo da qual nenhuma promoção pode reduzir o preço), ou prefere outro número? Esse é o gatilho que o Renato vai usar para barrar promoções que coloquem o negócio em risco.

**Sobre custo de insumo:**
5. A ficha técnica do Vitor (com custo de insumo por unidade de cada um dos 8 produtos) já existe em algum lugar, ou precisa ser criada do zero? Sem ela, o cálculo de preço de cada produto real não pode começar, só o método (que já está pronto neste documento).
