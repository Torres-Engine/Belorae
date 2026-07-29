# Planilha de Precificação por Produto

**Setor:** Financeiro
**Responsável:** Renato (Controller Financeiro)
**Data:** 26/07/2026
**Status:** rascunho v0.1, estrutura pronta, valores pendentes

---

## O que é este documento

Este documento é a "planilha" (em formato de tabela de texto, para poder ser copiada depois para
Google Sheets ou Excel) onde cada linha da fórmula de precificação, explicada em
`METODO-DE-PRECIFICACAO.md`, ganha um lugar certo para receber valor, produto por produto.

Hoje **nenhum valor está preenchido**. Todo campo está marcado como `[a confirmar]`, porque
depende de informação que ainda não existe em nenhum lugar (custo de insumo real da Patrícia,
rendimento real medido pelo Vitor, rateio de custo fixo do `MAPA-CUSTOS-FIXOS.md`, e as decisões
do dono sobre valor da própria hora e margem alvo). A estrutura existe para que, assim que cada
número chegar, baste substituir o `[a confirmar]` pelo valor real, sem precisar redesenhar a
planilha.

Os três produtos abaixo são os do trio de lançamento proposto na Onda 1 (ver
`docs/negocio/PLANO-DE-ONDAS.md`): Bolo Integral de Cenoura, Brownie Fit de Amêndoas e Cookies
Sem Glúten. Essa escolha de trio ainda depende de confirmação do dono (ver Achado Crítico 1 em
`docs/negocio/README.md`), mas a estrutura de preço serve para qualquer produto, muda só o nome.

---

## Como preencher cada linha (resumo, ver `METODO-DE-PRECIFICACAO.md` para a explicação completa)

| Linha da fórmula | De onde vem o número |
|---|---|
| Custo de insumo por unidade | Ficha técnica do Vitor (Produção) + cotação de fornecedor da Patrícia (Compras). Ver item 1.1 do `METODO-DE-PRECIFICACAO.md`. |
| Custo de embalagem por unidade | Cotação de embalagem da Patrícia. Ver item 1.2. |
| Custo de mão de obra por unidade | Valor da hora do dono (decisão do dono, ainda `[a confirmar]`) x tempo real do lote (ficha técnica do Vitor, depois do teste de bancada), dividido pelo rendimento. Ver item 1.3. |
| Rateio de custo fixo por unidade | Custo fixo total do mês (`MAPA-CUSTOS-FIXOS.md`, tabela da seção 1) dividido pela quantidade total estimada de vendas do mês (todos os produtos somados). Ver item 1.4. |
| Margem alvo | Decisão do dono, em porcentagem sobre o preço de venda (não markup sobre custo). Ver itens 1.5 e 2. |
| Preço de venda | Custo total por unidade dividido por (1 − margem alvo). Ver item 3. |

Lembrete importante: o rateio de custo fixo por unidade é o **mesmo número** para todos os
produtos vendidos naquele mês (ele não muda de produto para produto), porque ele depende da
quantidade total estimada de vendas do mês, somando todos os produtos, não só um. Por isso ele só
pode ser calculado depois que existir uma estimativa de volume mensal total.

---

## 1. Bolo Integral de Cenoura

Ficha técnica de referência: `docs/negocio/producao/FT-001-BOLO-INTEGRAL-CENOURA.md`.
Unidade de venda de referência para o cálculo abaixo: **1 fatia** (bolo inteiro rende
aproximadamente 12 fatias, conforme a ficha técnica; confirmar depois do teste de bancada).

| Item da fórmula | Valor |
|---|---|
| Custo de insumo por unidade (fatia) | `[a confirmar]` |
| Custo de embalagem por unidade | `[a confirmar]` |
| Custo de mão de obra por unidade | `[a confirmar]` |
| Rateio de custo fixo por unidade | `[a confirmar]` |
| **Custo total por unidade** | `[a confirmar]` (soma das quatro linhas acima) |
| Margem alvo (%) | `[a confirmar]` |
| **Preço de venda (por fatia)** | `[a confirmar]` (fórmula: custo total ÷ (1 − margem alvo)) |

Observação: o cardápio rascunho também prevê venda do bolo inteiro (aproximadamente 12 fatias). Se
o dono decidir vender também a unidade "bolo inteiro" como um item próprio, essa é uma segunda
linha de preço (custo total da fatia x 12, ou recálculo direto pela receita inteira), ainda não
criada aqui porque depende dessa decisão.

---

## 2. Brownie Fit de Amêndoas

Ficha técnica de referência: `docs/negocio/producao/FT-002-BROWNIE-FIT-AMENDOAS.md`.
Unidade de venda de referência para o cálculo abaixo: **1 unidade** (a receita rende 12 unidades,
equivalente a 2 caixas com 6, conforme a ficha técnica; confirmar depois do teste de bancada).

| Item da fórmula | Valor |
|---|---|
| Custo de insumo por unidade | `[a confirmar]` |
| Custo de embalagem por unidade | `[a confirmar]` |
| Custo de mão de obra por unidade | `[a confirmar]` |
| Rateio de custo fixo por unidade | `[a confirmar]` |
| **Custo total por unidade** | `[a confirmar]` (soma das quatro linhas acima) |
| Margem alvo (%) | `[a confirmar]` |
| **Preço de venda (por unidade)** | `[a confirmar]` (fórmula: custo total ÷ (1 − margem alvo)) |

Observação: o cardápio também prevê venda em caixa com 6 unidades. Se o dono mantiver esse
formato, essa é uma segunda linha de preço (preço da unidade x 6, com possível ajuste de desconto
de volume, desde que respeite a margem mínima de veto do Renato, ver item 5 do
`METODO-DE-PRECIFICACAO.md`), ainda não calculada aqui.

Atenção de custo já registrada na ficha técnica do Vitor: a farinha de amêndoas costuma ser um dos
insumos mais caros do cardápio inteiro, o que pode apertar a margem deste produto mais do que a
dos outros dois. Vale conferir com atenção assim que a Patrícia trouxer a cotação.

---

## 3. Cookies Sem Glúten

Ficha técnica de referência: **ainda não existe** (prevista como `FT-003-COOKIES-SEM-GLUTEN.md`,
entregável do Vitor na Onda 2, conforme `docs/negocio/PLANO-DE-ONDAS.md`). A estrutura abaixo já
está pronta para receber os valores assim que essa ficha técnica for criada.

Unidade de venda de referência para o cálculo abaixo: **1 unidade** (formato de venda exato, se
avulso ou em pacote, ainda depende da ficha técnica a ser criada).

| Item da fórmula | Valor |
|---|---|
| Custo de insumo por unidade | `[a confirmar]` |
| Custo de embalagem por unidade | `[a confirmar]` |
| Custo de mão de obra por unidade | `[a confirmar]` |
| Rateio de custo fixo por unidade | `[a confirmar]` |
| **Custo total por unidade** | `[a confirmar]` (soma das quatro linhas acima) |
| Margem alvo (%) | `[a confirmar]` |
| **Preço de venda (por unidade)** | `[a confirmar]` (fórmula: custo total ÷ (1 − margem alvo)) |

Observação: a Helena já sinalizou risco alto sobre a alegação "sem glúten" deste produto, por
causa da aveia usada na receita e da possível contaminação cruzada de bancada (ver
`docs/negocio/qualidade/MATRIZ-ALERGENOS-E-VALIDADE.md`). Isso não muda a estrutura de preço, mas
pode mudar o custo de insumo (se for preciso comprar aveia certificada, mais cara) e deve ser
conferido antes de fechar o preço final deste produto.

---

## Quadro-resumo dos três produtos (para preencher depois que os valores acima existirem)

| Produto | Custo total por unidade | Margem alvo | Preço de venda |
|---|---|---|---|
| Bolo Integral de Cenoura (fatia) | `[a confirmar]` | `[a confirmar]` | `[a confirmar]` |
| Brownie Fit de Amêndoas (unidade) | `[a confirmar]` | `[a confirmar]` | `[a confirmar]` |
| Cookies Sem Glúten (unidade) | `[a confirmar]` | `[a confirmar]` | `[a confirmar]` |

---

## Premissas assumidas

1. Assumi como unidade de referência de cálculo a menor unidade de venda de cada produto (fatia
   para o bolo, unidade avulsa para o brownie e para o cookie), porque é a unidade mais comum de
   comparação de preço e a que a ficha técnica já usa para calcular rendimento. Formatos maiores
   (bolo inteiro, caixa com 6) ficam registrados como observação, para cálculo futuro.
2. Assumi que o rateio de custo fixo por unidade é o mesmo valor para os três produtos neste
   quadro, porque a fórmula do `MAPA-CUSTOS-FIXOS.md` divide o custo fixo total do mês pela
   quantidade total estimada de vendas (somando todos os produtos), não por produto individual.
3. Não inventei nenhum valor de custo, tempo, margem ou preço. Todo campo permanece `[a confirmar]`
   até existir dado real vindo do Vitor, da Patrícia, do próprio `MAPA-CUSTOS-FIXOS.md` preenchido,
   e da decisão do dono sobre valor da hora e margem alvo.
4. Para os Cookies Sem Glúten, assumi que a estrutura de preço pode ser criada mesmo sem a ficha
   técnica existir ainda, porque o objetivo desta tarefa é deixar a planilha pronta para receber
   valor assim que a ficha técnica (FT-003) e os demais dados existirem, não calcular o preço agora.

## Perguntas para o dono responder

Estas perguntas já estão registradas em `METODO-DE-PRECIFICACAO.md` e em `PERGUNTAS-AO-DONO.md`, e
são pré-requisito para esta planilha sair do `[a confirmar]`:

1. Qual valor por hora você quer usar para o seu próprio tempo de trabalho na cozinha?
2. Qual margem alvo (em %) você quer ter em cada produto, ou pelo menos em média no cardápio?
3. Existe uma estimativa de quantas unidades, somando todos os produtos, você espera vender por
   mês? Sem isso, o rateio de custo fixo por unidade não pode ser calculado.
