# Programa de Gestão da Belorae

**Responsável pelo programa:** Marina (Diretora Geral / CEO do Negócio)
**Última atualização:** 26/07/2026
**Status:** Onda 1 concluída e revisada

## O que é esta pasta

Aqui mora a documentação da **empresa**, não do site.

A Belorae tem dois times de trabalho, que não se misturam:

- O **time técnico** (Ricardo e equipe) cuida do site. A documentação dele fica em `docs/`, fora desta pasta, e está descrita em `docs/AGENTS.md`.
- O **time de negócio** (Marina e equipe) cuida da empresa: o que produzir, quanto custa, por quanto vender, o que a lei exige, como vender e como não errar. É esta pasta, e o time está descrito em `docs/EQUIPE_NEGOCIO.md`.

Se a sua dúvida é sobre botão, cor, WhatsApp do site ou hospedagem, não é aqui. Se a sua dúvida é sobre receita, fornecedor, preço, rótulo, alvará ou cliente, é aqui.

## ATENÇÃO: dois achados críticos antes de qualquer coisa avançar

Esta seção vem antes do índice de propósito. São os dois pontos que precisam da decisão do dono antes de o negócio crescer, e nenhum dos dois se resolve sozinho com o tempo.

### Achado crítico 1: a promessa "sem glúten" hoje não é segura de manter

**O que foi encontrado.** Três produtos do cardápio prometem ausência de glúten: Brownie Fit de Amêndoas, Cookies Sem Glúten e Mini Quiche de Legumes. A Helena (Qualidade) verificou que essa promessa depende de duas condições, e hoje nenhuma das duas está garantida:

1. Nenhum ingrediente com glúten na receita. Nos cookies isso está em dúvida, porque a receita leva aveia, e aveia comum é frequentemente contaminada com trigo na lavoura e no processamento. Só aveia com selo de certificação "sem glúten" resolve.
2. Nenhum contato com farinha de trigo em bancada, tigela, utensílio, forma, batedeira ou até poeira suspensa. Como a produção acontece em cozinha única, e o Bolo Integral de Cenoura leva 280 g de farinha de trigo integral por receita, esse contato hoje é provável.

**Por que isso é grave em dois sentidos ao mesmo tempo.** Do lado da saúde, uma pessoa com doença celíaca pode ter reação séria com traços mínimos de glúten. Do lado do negócio, escrever "sem glúten" em um produto que não é comprovadamente sem glúten é infração sanitária, e não é defensável se acontecer um problema com um cliente.

**O agravante que a revisão da Onda 1 encontrou.** O portfólio de lançamento proposto (Bolo Integral de Cenoura, Brownie Fit de Amêndoas, Cookies Sem Glúten) é justamente a combinação de maior atrito possível: um produto que é a fonte do glúten mais dois produtos que prometem não ter glúten. Reduzir o cardápio de 8 para 3 itens resolveu o problema de sobrecarga de produção, mas não resolveu este, e concentrou ele.

**Existe ainda o caminho inverso, que precisa entrar no rótulo do bolo.** Brownie leva amêndoa e cookie leva castanhas. Se forem produzidos no mesmo ambiente, o Bolo Integral de Cenoura passa a precisar declarar "pode conter amêndoa e castanhas". Castanha e amêndoa causam reações graves, às vezes mais graves que o glúten.

**O que o dono precisa decidir.** Existem dois caminhos, e os dois são aceitáveis. O que não é aceitável é continuar como está.

- **Caminho A, manter a promessa.** Exige comprar aveia com certificação sem glúten, reservar um dia ou turno de produção só para os itens sem glúten, higienizar tudo antes, e guardar os produtos em embalagem fechada e separada, inclusive no freezer. Custa mais dinheiro e mais organização, e vira um diferencial real de marca.
- **Caminho B, ajustar a comunicação.** Trocar "sem glúten" por "pode conter traços de glúten, produzido em ambiente compartilhado", e renomear o produto "Cookies Sem Glúten". Custa quase nada, é honesto, e mantém a segurança do cliente e do negócio.

Enquanto essa decisão não existir, **nenhum rótulo pode ser impresso e o cardápio final não pode ser publicado.**

Detalhes em `qualidade/MATRIZ-ALERGENOS-E-VALIDADE.md` e em `qualidade/ROTULAGEM-MODELO.md`.

### Achado crítico 2: vender para Mafra/SC exige confirmação tributária e sanitária

**O que foi encontrado.** Rio Negro (PR) e Mafra (SC) são cidades coladas, mas em estados diferentes. Vender de um lado para o outro é, juridicamente, uma operação entre estados. O Otávio (Jurídico) identificou dois efeitos:

1. **Tributário.** O ICMS (imposto estadual sobre circulação de mercadoria) tem regras próprias para venda entre estados diferentes, que podem não ser as mesmas da venda dentro do Paraná.
2. **Sanitário.** A licença sanitária e o alvará são emitidos pelo município onde a produção acontece (Rio Negro). Isso normalmente não impede a venda para Mafra, mas é preciso confirmar se Santa Catarina tem alguma exigência adicional para alimento vindo de fora do estado.

**O que isso NÃO significa.** Não significa que a Belorae está proibida de vender para Mafra, nem que precisa parar. O Otávio foi claro nisso: não bloqueia o negócio.

**O que isso significa.** Significa que existe uma pergunta em aberto que fica mais cara de responder quanto mais tarde for feita. Se a venda para Mafra virar uma fatia relevante do faturamento antes de a situação estar confirmada, o risco é de cobrança retroativa de imposto, que é o tipo de problema que aparece de uma vez e já grande.

**O que o dono precisa fazer.** Uma conversa com um contador que já atenda negócios na fronteira PR/SC. Não um contador qualquer: um que já lide com essa situação, que é comum na região. As perguntas exatas a levar já estão prontas no checklist de `juridico/DIAGNOSTICO-FORMALIZACAO.md`.

**Consequência para o financeiro, registrada aqui porque atravessa dois setores.** Se em algum momento a Belorae deixar de ser MEI e virar Microempresa no Simples Nacional, o imposto deixa de ser um valor fixo mensal e vira um percentual sobre o faturamento. A fórmula de preço atual do Renato não tem espaço para imposto variável, porque foi construída para o cenário MEI. Isso está correto para hoje e precisa ser revisto no dia da mudança de regime. Registrado para não ser esquecido.

## Onde fica cada coisa

```
docs/negocio/
  README.md                   este arquivo, ponto de entrada
  PLANO-DE-ONDAS.md           o plano de 6 ondas do programa
  PERGUNTAS-AO-DONO.md        tudo que depende de resposta do dono, priorizado

  producao/                   Vitor, Chef Executivo
    PORTFOLIO-PRODUTOS.md          os 8 produtos avaliados, e quais lançar primeiro
    FICHA-TECNICA-MODELO.md        modelo em branco para toda receita futura
    FT-001-BOLO-INTEGRAL-CENOURA.md
    FT-002-BROWNIE-FIT-AMENDOAS.md
    FT-003-COOKIES-SEM-GLUTEN.md   ficha do terceiro produto do lançamento, com o ponto do glúten em aberto
    GLUTEN-DOIS-CAMINHOS.md        os dois caminhos possíveis para o Achado Crítico 1, para o dono escolher

  insumos/                    Patrícia, Compras e Insumos
    MAPA-DE-INSUMOS.md             tudo que precisa comprar, por categoria
    ROTEIRO-COTACAO-FORNECEDORES.md  como cotar, o que perguntar, script de WhatsApp
    POLITICA-ESTOQUE-MINIMO.md     quando comprar, quanto guardar, o que não estocar

  financeiro/                 Renato, Controller
    METODO-DE-PRECIFICACAO.md      como transformar custo em preço
    MAPA-CUSTOS-FIXOS.md           o que se paga mesmo sem vender nada
    MODELO-FLUXO-DE-CAIXA.md       como registrar dinheiro que entra e sai

  qualidade/                  Helena, Qualidade e Segurança Alimentar
    BOAS-PRATICAS-MANIPULACAO.md   checklist de rotina, para imprimir e usar
    MATRIZ-ALERGENOS-E-VALIDADE.md alérgenos e prazo de validade dos 8 produtos
    ROTULAGEM-MODELO.md            o que precisa estar escrito em cada etiqueta

  juridico/                   Otávio, Jurídico e Regulatório
    DIAGNOSTICO-FORMALIZACAO.md    MEI x Microempresa, e a questão de Mafra
    LICENCAS-E-ALVARAS.md          alvará, vigilância sanitária, curso obrigatório
    LGPD-DADOS-DE-CLIENTES.md      como tratar dado de cliente sem levar multa
```

Pastas que ainda não existem porque os setores ainda não foram acionados: `marketing/` (Bianca), `atendimento/` (Diego) e `pessoas/` (Fabiana). Entram nas Ondas 3 e 6, conforme o `PLANO-DE-ONDAS.md`.

## Por onde começar a ler, dependendo do que você quer

**Se você tem 10 minutos e quer entender a situação:** leia os dois achados críticos acima e depois o `PERGUNTAS-AO-DONO.md`, só o Bloco A.

**Se você vai para a cozinha:** `qualidade/BOAS-PRATICAS-MANIPULACAO.md` (imprima e cole na parede) e a ficha técnica do produto que vai fazer.

**Se você vai falar com fornecedor:** `insumos/ROTEIRO-COTACAO-FORNECEDORES.md`, que tem o script de mensagem pronto para copiar.

**Se você quer saber por quanto vender:** `financeiro/METODO-DE-PRECIFICACAO.md`. Leia a seção 2 mesmo que pule o resto, ela sozinha evita o erro mais caro de negócio pequeno.

**Se você vai abrir CNPJ ou falar com contador:** `juridico/DIAGNOSTICO-FORMALIZACAO.md`, e leve o checklist do fim do arquivo impresso.

**Se você vai imprimir etiqueta:** `qualidade/ROTULAGEM-MODELO.md`, mas só depois de decidir o Achado Crítico 1.

## Como ler o status de cada documento

Todo documento tem um cabeçalho com **Setor**, **Responsável**, **Data** e **Status**. Hoje todos estão como `rascunho v0.1`, o que significa: a estrutura está pronta e revisada, mas os números reais ainda não foram preenchidos.

Dentro dos documentos, `[a confirmar]` marca um campo que depende de informação que ainda não existe (uma cotação, uma conta de luz, uma decisão do dono). Isso é proposital. Nenhum agente inventou preço, fornecedor, telefone ou número de norma. Onde não havia dado real, ficou em branco marcado, e não um chute com cara de fato.

## Regras de escrita deste programa

Para manter tudo com a mesma cara e legível para quem é iniciante em gestão:

- Português do Brasil, direto, sem enrolação.
- Todo termo técnico de negócio é explicado na primeira vez que aparece.
- Sem travessão e sem emoji nos documentos.
- Quem propõe, assume: cada documento termina com as premissas assumidas e as perguntas em aberto.
- Nenhum número inventado. Sem dado real, escrever `[a confirmar]`.
