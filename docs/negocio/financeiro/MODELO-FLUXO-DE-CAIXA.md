# Modelo de Fluxo de Caixa da Belorae

**Setor:** Financeiro
**Responsável:** Renato (Controller Financeiro)
**Data:** 26/07/2026
**Status:** rascunho v0.1

---

## O que é fluxo de caixa (em uma frase)

**Fluxo de caixa** é o registro simples de todo dinheiro que entra e todo dinheiro que sai do negócio, mês a mês, para o dono saber, a qualquer momento, se está sobrando ou faltando dinheiro. Não é sobre lucro "no papel", é sobre dinheiro de verdade entrando e saindo da conta ou da carteira.

Este modelo foi pensado para rodar em caderno ou em uma planilha simples (Google Sheets, Excel), sem nenhuma fórmula complicada. O objetivo da primeira versão não é ser perfeito, é existir: hoje a Belorae não tem nenhum registro financeiro em lugar nenhum, e qualquer registro (mesmo manual) já é um salto grande de controle.

---

## 1. Regra número 1: separar dinheiro da empresa do dinheiro pessoal

Antes de explicar a planilha, uma regra que vem antes de qualquer coluna ou fórmula: **o dinheiro que entra da venda de doces não é a mesma coisa que o dinheiro pessoal do dono**, mesmo que hoje tudo caia na mesma conta ou na mesma carteira.

Por que isso quebra negócio pequeno: se o dinheiro da venda e o dinheiro pessoal se misturam, o dono não consegue responder perguntas básicas como "o negócio está dando lucro de verdade?" ou "eu posso tirar dinheiro esse mês ou não?". É comum acontecer o seguinte ciclo, que derruba muitos negócios pequenos: o dinheiro da venda de hoje é usado para comprar insumo de amanhã, misturado com gasto pessoal, e quando chega um mês de venda mais fraca, não sobra dinheiro nem para comprar o insumo do próximo lote, porque o "caixa" nunca existiu separado, era só a carteira do dono mesmo.

Recomendação prática, mesmo sem abrir uma conta bancária de empresa ainda:
- Se possível, ter uma conta digital gratuita separada (só para a Belorae), ou pelo menos um envelope/caixinha física separada para o dinheiro das vendas.
- Definir um valor fixo de "retirada" (o quanto o dono tira do negócio para uso pessoal por mês) e registrar essa retirada como uma saída no fluxo de caixa, não como "sobrou, então uso". Isso conecta diretamente com o valor de mão de obra por hora definido em `METODO-DE-PRECIFICACAO.md`.
- Nunca pagar uma conta pessoal direto do dinheiro que entrou de um pedido, sem antes esse dinheiro "passar" pelo registro do fluxo de caixa.

---

## 2. Estrutura da planilha mensal

Uma aba por mês (ou uma tabela por mês, se for em caderno). Dentro de cada mês, uma linha por movimentação (cada entrada e cada saída), com estas colunas:

| Coluna | O que colocar |
|---|---|
| Data | Dia em que o dinheiro entrou ou saiu de fato (não a data do pedido, se forem diferentes). |
| Tipo | "Entrada" ou "Saída". |
| Categoria | Ver lista de categorias na seção 3. |
| Descrição | Um texto curto, ex: "Bolo de cenoura inteiro, cliente Maria" ou "Compra de farinha de amêndoas". |
| Valor | Valor em reais, sempre número positivo (o "Tipo" já diz se é entrada ou saída). |
| Forma de pagamento | Pix, dinheiro, cartão, outro. Ajuda a conferir depois com o extrato do banco. |
| Observação | Espaço livre, ex: "pagamento parcelado", "cliente de Mafra", "promoção aplicada". |

No fim do mês, duas linhas de resumo:

```
Total de entradas do mês  = soma de todas as linhas "Entrada"
Total de saídas do mês    = soma de todas as linhas "Saída"
Resultado do mês          = Total de entradas − Total de saídas
```

Se o "Resultado do mês" for positivo, sobrou dinheiro naquele mês. Se for negativo, o negócio gastou mais do que recebeu naquele mês (o que pode ser normal em um mês de investimento, como comprar um equipamento novo, mas precisa ser entendido, não ignorado).

---

## 3. Categorias de entrada e saída

### Entradas (dinheiro que entra)

- Venda de produto (o grosso do fluxo, idealmente detalhado por produto ou ao menos por categoria do cardápio: bolos, doces individuais, sem açúcar, salgados fit).
- Encomenda antecipada (sinal ou pagamento adiantado de um pedido que ainda vai ser entregue).
- Outras entradas (ex: venda de algum item usado, reembolso, etc, o que for raro entra aqui para não sujar a categoria principal).

### Saídas (dinheiro que sai)

- Insumo (ingredientes: farinha, chocolate, frutas, castanhas etc.).
- Embalagem (caixa, saquinho, etiqueta, fita).
- Custo fixo (energia, gás, água, internet, aluguel/rateio, ver detalhamento completo em `MAPA-CUSTOS-FIXOS.md`).
- Equipamento (compra ou conserto de forno, batedeira, geladeira etc, gastos que não são mensais mas acontecem de vez em quando).
- Deslocamento/entrega (combustível, transporte).
- Taxas (maquininha, contador, MEI).
- Retirada do dono (o valor que o dono tira do negócio para uso pessoal, ver seção 1 acima).
- Outras saídas (qualquer gasto que não se encaixe nas categorias acima).

---

## 4. Como ler o resultado no fim do mês

Depois de fechar as duas somas (entradas e saídas), três perguntas simples ajudam a interpretar o número:

1. **O resultado do mês foi positivo ou negativo?** Se negativo, foi por causa de uma compra grande e pontual (equipamento, estoque de insumo maior), ou porque as vendas do mês foram baixas? A resposta muda completamente o que fazer a seguir.
2. **O total de entradas cobre todo o custo fixo do mês?** Se as entradas não cobrem nem o custo fixo (energia, gás, internet etc.), o negócio está abaixo do ponto de equilíbrio (o assunto de um relatório específico do Renato, que depende do mapa de custo fixo estar preenchido).
3. **A retirada do dono está registrada, e ela é sustentável?** Se o dono está tirando mais do negócio do que o resultado do mês permite, isso "come" o caixa aos poucos, mesmo que pareça que está tudo bem no dia a dia.

Este fluxo de caixa mensal, junto com a planilha de precificação (`METODO-DE-PRECIFICACAO.md`) e o mapa de custo fixo (`MAPA-CUSTOS-FIXOS.md`), formam a base para o relatório financeiro periódico que o Renato vai gerar assim que houver ao menos um mês completo de dados reais registrados.

---

## Premissas assumidas

**Sobre o formato:**
1. Assumi que o modelo precisa funcionar sem nenhuma ferramenta paga, rodando em caderno ou Google Sheets, porque o negócio está em estágio inicial, sem funcionários e sem sistema financeiro implantado.
2. Assumi que uma linha por movimentação (em vez de um resumo semanal, por exemplo) é o nível de detalhe certo para começar, porque permite depois cruzar cada venda com o produto e cada gasto com a categoria, sem precisar refazer o controle do zero quando o negócio crescer.

**Sobre a separação pessoal/empresa:**
3. Assumi que hoje o dinheiro da Belorae e o dinheiro pessoal do dono provavelmente se misturam na mesma conta ou carteira, porque não há indicação de conta empresarial separada nem de MEI confirmado. Se isso já estiver resolvido, a recomendação da seção 1 vira só uma confirmação, não uma mudança de hábito.

## Perguntas para o dono responder

**Sobre ferramenta e rotina:**
1. Você prefere registrar o fluxo de caixa em Google Sheets, em um aplicativo de celular, ou em caderno? A resposta muda o formato exato do arquivo que devo preparar (planilha pronta para importar, ou modelo para copiar à mão).
2. Você consegue reservar um momento fixo (ex: todo domingo à noite) para lançar as movimentações da semana? Sem uma rotina definida, o fluxo de caixa tende a ficar esquecido depois da primeira semana.

**Sobre conta e retirada:**
3. Você já tem ou pretende abrir uma conta separada (mesmo que uma conta digital gratuita) só para o dinheiro da Belorae? Essa é a mudança de hábito mais importante deste documento, e precisa ser uma decisão consciente do dono.
4. Existe algum valor que você já retira (ou pretende retirar) do negócio hoje para uso pessoal? Sem esse número, a categoria "Retirada do dono" fica sem referência para o primeiro mês de registro.

**Sobre histórico:**
5. Existe algum registro informal de vendas ou gastos dos últimos meses (mesmo que só na cabeça ou em conversas de WhatsApp) que ajude a reconstruir um ponto de partida, ou o fluxo de caixa vai começar do zero a partir de agora? Isso define se dá para estimar uma tendência inicial ou se o primeiro mês será a única referência disponível.
