# Modelo de Rotulagem por Produto: Belorae

Setor: Qualidade e Segurança Alimentar
Responsável: Helena (Especialista em Qualidade e Segurança Alimentar)
Data: 26/07/2026
Status: rascunho v0.1

## Ressalva importante sobre as normas citadas

Este documento cita normas da Anvisa (Agência Nacional de Vigilância Sanitária) como referência de
conteúdo geral de rotulagem, com base em conhecimento amplo sobre o tema. As normas mais associadas
a este assunto costumam ser:

- Regulamento técnico geral de rotulagem de alimentos embalados (associado historicamente à RDC
  259/2002).
- Regulamento técnico sobre declaração obrigatória de alérgenos (associado historicamente à RDC
  26/2015).
- Regulamentos sobre rotulagem nutricional obrigatória (associados historicamente às RDC 359/2003,
  RDC 360/2003 e atualizações posteriores sobre rotulagem nutricional frontal).

Este documento **não tem acesso à internet** e regras de rotulagem mudam com alguma frequência.
Portanto, os números de RDC acima são citados apenas como ponto de partida de pesquisa, não como
confirmação de vigência atual. Antes de imprimir qualquer rótulo final, confirmar a redação vigente
com um profissional habilitado (nutricionista responsável técnico ou consultoria especializada em
rotulagem) e/ou com a vigilância sanitária local (Otávio deve revisar o aspecto regulatório formal
deste documento).

## O que precisa constar no rótulo (visão geral)

Todo produto vendido de forma embalada, mesmo artesanal, deve ter no rótulo, no mínimo:

1. **Denominação de venda**: o nome que identifica claramente o que é o produto (não pode ser só
   um nome comercial fantasioso sem explicar o que é; por exemplo, "Bolo Integral de Cenoura com
   Cobertura de Chocolate" identifica melhor o produto do que apenas um nome criativo sozinho).
2. **Lista de ingredientes em ordem decrescente**: todos os ingredientes usados, listados do que
   tem mais quantidade (em peso) para o que tem menos.
3. **Declaração de alérgenos**: frase destacada informando os alérgenos de declaração obrigatória
   presentes (ver `MATRIZ-ALERGENOS-E-VALIDADE.md` para o levantamento por produto).
4. **Peso líquido (conteúdo)**: quanto o produto pesa (em gramas) ou quantas unidades contém,
   dependendo do tipo de venda (fatia, unidade, caixa).
5. **Data de fabricação e prazo de validade**: quando foi feito e até quando pode ser consumido com
   segurança.
6. **Lote**: um código simples que identifica o dia/produção daquele item, para permitir
   rastreabilidade caso algo precise ser investigado depois (não precisa ser complexo: pode ser a
   própria data de fabricação, por exemplo).
7. **Identificação do produtor/fabricante**: nome do responsável (e, quando formalizado, razão
   social e CNPJ) e forma de contato.
8. **Condição de conservação**: instrução de como guardar (ambiente, refrigerado, congelado) e, se
   aplicável, instrução de consumo (por exemplo, "reaquecer antes de consumir").
9. **Informação nutricional básica**: tabela com valores aproximados de energia (calorias),
   carboidratos, proteínas, gorduras, entre outros, por porção. Existem situações em que produtos
   vendidos artesanalmente, sem embalagem industrial e diretamente ao consumidor final, podem ter
   regras simplificadas ou dispensas de tabela nutricional completa; essa exceção específica precisa
   ser confirmada, porque varia conforme o tipo de venda e não foi possível confirmar a regra atual
   sem acesso à internet [a confirmar].

## Modelo visual em texto: exemplo com o Brownie Fit de Amêndoas

O exemplo abaixo é fictício, apenas para mostrar como as informações ficariam organizadas em um
rótulo impresso ou etiqueta colada na embalagem. Os valores nutricionais e o peso são placeholders
e precisam ser substituídos por valores reais calculados a partir da ficha técnica.

```
====================================================
BROWNIE FIT DE AMÊNDOAS
Belorae Confeitaria Saudável
====================================================

INGREDIENTES: farinha de amêndoas, ovos, [adoçante
natural - especificar qual], manteiga [ou óleo -
confirmar], cacau em pó, fermento químico.
[completar lista real em ordem decrescente de peso]

ALÉRGENOS: CONTÉM AMÊNDOA E OVO.
Pode conter traços de glúten (produzido em ambiente
que também manipula farinha de trigo) [confirmar se
esta frase se aplica após revisão de processo, ver
achado em MATRIZ-ALERGENOS-E-VALIDADE.md].

PESO LÍQUIDO: [xx] g (1 unidade)

DATA DE FABRICAÇÃO: 26/07/2026
VALIDADE: consumir até 30/07/2026
(4 dias, sob refrigeração constante entre 1°C e 5°C)

LOTE: 260726-A

CONSERVAÇÃO: Manter refrigerado. Não deixar fora da
geladeira por mais de 2 horas.

FABRICADO POR: [nome do responsável / Belorae]
Rio Negro, PR
Contato: [telefone/WhatsApp de contato comercial,
não pessoal]

INFORMAÇÃO NUTRICIONAL (valores aproximados por
unidade de [xx] g):
Valor energético: [xx] kcal
Carboidratos: [xx] g
Proteínas: [xx] g
Gorduras totais: [xx] g
Fibra alimentar: [xx] g
Sódio: [xx] mg
[valores a calcular com base na ficha técnica real;
não inventar número antes disso]
====================================================
```

Este mesmo modelo de estrutura (ingredientes, alérgenos, peso, data de fabricação/validade, lote,
conservação, fabricante, informação nutricional) deve ser repetido para os outros 7 produtos,
ajustando o conteúdo específico de cada um com base na ficha técnica real e na
`MATRIZ-ALERGENOS-E-VALIDADE.md`.

## Frase padrão sugerida para declaração de alérgenos

- Quando o alérgeno está na receita: "CONTÉM [nome do alérgeno]."
- Quando existe risco de contaminação cruzada por ambiente compartilhado: "Pode conter traços de
  [nome do alérgeno]."
- Nunca usar a frase "sem [alérgeno]" em um produto sem ter certeza real do processo de produção
  (ver achado detalhado em `MATRIZ-ALERGENOS-E-VALIDADE.md` sobre os produtos "sem glúten" do
  cardápio atual).

## O que muda quando o negócio for formalizado

- **Identificação do fabricante**: hoje pode constar apenas nome do responsável e contato; após
  formalização (por exemplo, como Microempreendedor Individual, MEI, ou outro tipo de registro),
  passa a ser exigido também razão social, CNPJ e endereço do estabelecimento no rótulo.
- **Registro do produto**: dependendo do tipo de produto e do porte da operação, pode ser exigido
  registro ou notificação em algum órgão sanitário antes da venda em maior escala; essa exigência
  específica para confeitaria artesanal precisa ser confirmada com a vigilância sanitária local ou
  com Otávio [a confirmar].
- **Informação nutricional**: uma vez formalizado e com maior volume de venda, é mais provável que
  seja exigida tabela nutricional completa e calculada com precisão (não apenas aproximada), o que
  normalmente exige apoio de nutricionista ou laboratório para os cálculos.
- **Legislação estadual/municipal específica para produção artesanal em cozinha residencial**: em
  alguns estados existe legislação específica que permite produção e venda de alimentos artesanais
  feitos em cozinha residencial, com regras próprias (às vezes chamada informalmente de "lei da
  cozinha artesanal" ou nome parecido, variando por estado). Não foi possível confirmar se Paraná
  e/ou Santa Catarina têm uma legislação desse tipo vigente, nem suas exigências específicas
  [a confirmar com a vigilância sanitária local ou com Otávio].

---

## Premissas assumidas

1. Considerou-se que, hoje, os produtos são vendidos diretamente ao cliente final via WhatsApp e
   Instagram, sem revenda por terceiros, conforme contexto informado do negócio.
2. Considerou-se que a produção acontece em cozinha residencial, sem CNPJ formalizado até o momento
   deste documento, conforme contexto informado do negócio.
3. Os números de RDC citados são referência de ponto de partida de pesquisa, não confirmação de
   texto vigente, pela ausência de acesso à internet neste documento.
4. O peso líquido, valores nutricionais e lote do exemplo visual são placeholders fictícios,
   marcados entre colchetes, para mostrar apenas o formato, não o conteúdo real.

## Perguntas para o dono responder

### Sobre formalização e responsabilidade legal

1. O negócio já tem ou pretende abrir CNPJ (por exemplo, como MEI) no curto prazo? Isso importa
   porque muda o que precisa constar no campo "fabricado por" do rótulo e pode habilitar ou exigir
   outros registros.
2. Existe intenção de contratar ou consultar um nutricionista responsável técnico para validar a
   tabela de informação nutricional e o rótulo como um todo antes de uma venda em maior escala?
   Isso importa porque os valores nutricionais deste documento são apenas placeholders e precisam
   de cálculo técnico real.

### Sobre legislação local

3. Existe alguma informação já levantada sobre legislação estadual (Paraná e/ou Santa Catarina)
   específica para produção artesanal de alimentos em cozinha residencial? Isso importa porque pode
   simplificar (ou, ao contrário, tornar mais rígidas) as exigências de rótulo e registro citadas
   neste documento como "a confirmar".
4. O dono já teve algum contato com a vigilância sanitária de Rio Negro, PR, sobre os requisitos de
   rótulo para venda atual (mesmo antes de CNPJ)? Isso importa porque pode já existir uma orientação
   local que substitui ou complementa este modelo genérico.

### Sobre operação do rótulo no dia a dia

5. Existe hoje alguma forma prática de imprimir etiquetas (impressora própria, etiquetas
   adesivas compradas prontas, aplicativo de etiquetas) ou isso ainda precisa ser resolvido? Isso
   importa porque o modelo deste documento só funciona na prática se puder ser aplicado fisicamente
   em cada produto antes da entrega.
