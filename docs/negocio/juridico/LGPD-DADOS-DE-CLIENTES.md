# LGPD Básico: Como Tratar Dados de Clientes

**Setor:** Jurídico e Regulatório
**Responsável:** Otávio (Consultor Jurídico e Regulatório)
**Data:** 26/07/2026
**Status:** rascunho v0.1

> Aviso importante: eu não sou advogado. Este documento traduz, de forma simples, os cuidados
> básicos da LGPD (Lei Geral de Proteção de Dados) para um negócio pequeno como a Belorae, que
> ainda não tem sistema formal de cadastro. Não substitui orientação jurídica definitiva,
> especialmente se o negócio crescer e passar a lidar com um volume grande de dados de clientes.

## O que é a LGPD, em termos simples

LGPD é a Lei Geral de Proteção de Dados, uma lei brasileira que estabelece regras para como
empresas e pessoas podem coletar, guardar e usar dados pessoais (informações que identificam
alguém, como nome, telefone, endereço, e-mail). A ideia central é simples: só usar o dado da
pessoa para o que ela entendeu e aceitou, cuidar bem desse dado enquanto ele estiver guardado, e
apagar ou devolver quando não for mais necessário ou quando a pessoa pedir.

Para um negócio pequeno como a Belorae, que não tem sistema de cadastro formal e trabalha
principalmente pelo WhatsApp, a LGPD ainda se aplica, mas de um jeito proporcional ao tamanho do
negócio: não é preciso um departamento jurídico de proteção de dados, mas é preciso adotar
cuidados mínimos e consistentes.

## Quais dados a Belorae normalmente coleta

No fluxo de pedido por WhatsApp, os dados típicos são:

- Nome do cliente.
- Número de telefone (que já vem naturalmente do WhatsApp).
- Endereço de entrega (quando o pedido inclui entrega).
- Eventualmente, preferências de produto ou restrições alimentares mencionadas na conversa.

Todos esses são considerados dados pessoais pela LGPD, e o endereço de entrega, dependendo do
nível de detalhe, pode ser tratado com o mesmo cuidado dado a dado sensível relacionado à
localização da pessoa.

## O que pode e o que não pode fazer com a lista de contatos do WhatsApp

### Pode

- Guardar o contato do cliente para conseguir confirmar e entregar aquele pedido específico.
- Responder dúvidas e enviar atualizações sobre um pedido já feito (por exemplo, avisar que o
  bolo está pronto para retirada).
- Guardar o histórico de pedidos de um cliente para agilizar um próximo atendimento, se o cliente
  voltar a falar com a Belorae por iniciativa própria.

### Não pode (sem consentimento) e é o risco mais comum

- **Enviar mensagem de promoção, novidade de cardápio ou campanha para toda a lista de contatos
  do WhatsApp sem que a pessoa tenha concordado em receber esse tipo de mensagem.** Esse é
  disparo de comunicação de marketing sem consentimento, e é o erro mais comum e mais fácil de
  cometer sem perceber, porque parece só "avisar os clientes de algo bom". Juridicamente, usar o
  contato de alguém que só falou uma vez para comprar um bolo, para depois mandar propaganda sem
  perguntar antes, é um uso do dado além do que a pessoa autorizou.
- Compartilhar a lista de contatos de clientes com terceiros (outro negócio, por exemplo) sem
  autorização.
- Usar o endereço de entrega para qualquer finalidade que não seja a entrega combinada.

### Como pedir consentimento de forma simples, sem sistema formal

Uma forma simples e de baixo custo de resolver isso: ao final de uma conversa de pedido, perguntar
diretamente algo como "Posso te avisar por aqui quando tiver novidade no cardápio ou promoção?" e
só incluir quem responder que sim numa lista separada (pode ser uma lista simples de contatos
salvos, ou uma etiqueta/grupo de transmissão no próprio WhatsApp) para esse tipo de mensagem.
Quem não responder ou disser que não, fica de fora dessa lista, mas continua recebendo
normalmente as mensagens do próprio pedido que já fez.

## Como guardar os dados e por quanto tempo

Cuidados mínimos recomendados, mesmo sem sistema formal:

- Evitar espalhar a mesma informação de cliente em vários lugares (por exemplo, anotar o mesmo
  pedido em um caderno, numa planilha e numa conversa separada). Quanto mais lugares, maior o
  risco de perda ou exposição acidental.
- Se usar planilha ou agenda de pedidos, mantê-la em um local com alguma proteção mínima (por
  exemplo, um Google Sheets com acesso restrito, não um documento público ou compartilhado sem
  necessidade).
- Não é necessário guardar dados de cliente para sempre. Uma prática razoável é manter o
  histórico de pedidos por um tempo limitado (por exemplo, o tempo que fizer sentido para
  histórico de vendas e eventual reclamação, algo como um a dois anos), e depois apagar ou
  arquivar de forma que não fique acessível no dia a dia. **[a confirmar]** um prazo mais preciso,
  se o volume de dados crescer, com apoio jurídico, mas para o estágio atual do negócio, um
  prazo curto e simples já reduz bastante o risco.

## O que fazer se um cliente pedir para ser apagado

A LGPD garante à pessoa o direito de pedir a exclusão dos seus dados pessoais. Na prática, para a
Belorae hoje, isso significa: se um cliente disser algo como "pode apagar meus dados" ou "não
quero mais que vocês guardem meu contato", o caminho simples é:

1. Confirmar com o cliente o que ele quer (só sair da lista de promoções, ou apagar todo o
   histórico de pedidos).
2. Remover o contato da lista/etiqueta de promoções, se for o caso.
3. Apagar o registro do pedido salvo (planilha, caderno, conversa arquivada) que contenha os
   dados dele, quando não houver outra razão legítima para manter (por exemplo, controle fiscal
   de venda já feita, que pode ter prazo legal próprio de guarda).
4. Confirmar para o cliente que o pedido foi atendido, de forma simples, por mensagem mesmo.

## Conexão com a regra já existente no projeto do site

O `CLAUDE.md` do projeto do site já traz, na seção "O que NÃO fazer", a regra de "não commitar
números de telefone/e-mails reais de clientes" no repositório do código. Essa regra já está sendo
seguida tecnicamente pelo time do site, e a LGPD reforça exatamente esse cuidado: dado pessoal de
cliente não deve aparecer em nenhum lugar público ou de acesso amplo, incluindo código-fonte,
capturas de tela de exemplo, ou documentação compartilhada. Ou seja, o cuidado técnico que já
existe no projeto está alinhado com a exigência legal, e vale manter esse mesmo padrão de cuidado
também fora do código, na rotina de atendimento pelo WhatsApp.

## Checklist simples de LGPD para o dia a dia

- [ ] Perguntar antes de incluir alguém em lista de promoção/novidade.
- [ ] Manter os dados de clientes em um número reduzido de lugares (evitar espalhar).
- [ ] Revisar de tempos em tempos e apagar dados de pedidos muito antigos que não têm mais
      utilidade.
- [ ] Atender rapidamente qualquer pedido de exclusão de dados feito por um cliente.
- [ ] Nunca colocar telefone ou endereço real de cliente em qualquer material público (site,
      redes sociais, documentação).

## Premissas assumidas

- Assumi que a Belorae ainda não usa nenhum sistema formal de CRM (sistema de gestão de
  relacionamento com cliente) e trabalha com WhatsApp, e talvez planilha ou caderno simples.
- Assumi que o volume de clientes ainda é pequeno o suficiente para esses cuidados manuais serem
  viáveis no dia a dia.
- Assumi que ainda não houve nenhum disparo de mensagem em massa de promoção; se já houve, essa
  prática deve ser revista o quanto antes, com o cuidado de consentimento descrito acima.

## Perguntas para o dono responder

### Prática atual

1. Hoje, o dono já envia mensagens de promoção ou novidade para uma lista de contatos do
   WhatsApp? Se sim, essa lista já teve algum tipo de consentimento prévio, ou foi montada só a
   partir de quem comprou uma vez? Essa resposta define se é preciso ajustar a prática atual com
   urgência.
2. Onde os dados de pedidos (nome, telefone, endereço) estão guardados hoje, além do próprio
   WhatsApp? Isso ajuda a mapear quantos lugares diferentes precisam de atenção.

### Processo futuro

3. Existe intenção de usar algum sistema de gestão de pedidos ou CRM no futuro? Se sim, vale a
   pena revisar este documento novamente nesse momento, porque um sistema formal traz outras
   obrigações de segurança de dados.
4. O dono tem interesse em criar uma mensagem padrão simples de consentimento (por exemplo, uma
   frase fixa perguntando se pode enviar promoções) para usar a partir de agora? Isso resolveria
   o principal ponto de risco identificado neste documento de forma rápida e sem custo.
