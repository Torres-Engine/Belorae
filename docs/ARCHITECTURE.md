# ARCHITECTURE.md

## Visão geral

```
Visitante (celular/desktop)
        │
        ▼
  index.html (GitHub Pages)
        │
        ├── botão principal "Ver Cardápio" → abre PDF (assets/cardapio/cardapio-belorae.pdf)
        │                                         │
        │                                         └── (dentro do PDF, no rodapé) link wa.me/55XXXXXXXXXXX?text=mensagem+pronta
        │
        └── ícone de WhatsApp no rodapé do site → link wa.me/55XXXXXXXXXXX?text=mensagem+pronta
                                                │
                                                ▼
                                          WhatsApp do cliente
                                          (conversa direta com a Belorae)
```

## Decisão: sem backend, sem banco de dados

O objetivo do site é só **converter clique em conversa de WhatsApp**. Não há necessidade de guardar pedidos, usuários ou pagamentos no site — isso acontece dentro do próprio WhatsApp. Backend/banco de dados aumentariam custo e complexidade sem gerar benefício agora.

## Decisão: WhatsApp via link `wa.me`, não API paga

`https://wa.me/<numero>?text=<mensagem>` abre o WhatsApp do visitante com uma mensagem pré-preenchida. Grátis, funciona em qualquer navegador/celular, zero infraestrutura. A API oficial do WhatsApp Business (Meta Cloud API) permite automação real (bot respondendo sozinho), mas exige aprovação da Meta, custo por conversa e um servidor rodando — desnecessário nesta fase.

## Decisão: hospedagem GitHub Pages

Gratuito, versionado com Git, deploy automático a cada push. Ideal para site estático sem backend. Permite depois conectar um domínio próprio (ex: `beloraeconfeitaria.com.br`) sem trocar de arquitetura.

## Paleta de cores sugerida (não existe identidade visual ainda)

Tema "confeitaria saudável" — tons naturais, orgânicos, que fogem do clichê "doceria" (rosa/vermelho vibrante) e passam saúde + aconchego:

| Uso | Cor | Hex |
|---|---|---|
| Fundo principal | Creme claro | `#FDF8F0` |
| Destaque/CTA | Verde-sálvia | `#7A9471` |
| Texto principal | Marrom-café escuro | `#4A3728` |
| Acento secundário | Terracota suave | `#D98E73` |
| Branco/cards | Branco puro | `#FFFFFF` |

Essa paleta é um ponto de partida em `css/style.css` — trocar facilmente quando houver logo definido (variáveis CSS centralizadas em `:root`).

## Stack técnica

| Camada | Escolha | Por quê |
|---|---|---|
| Frontend | HTML + CSS + JS puro | Sem necessidade de framework para 1 página; zero build step, zero dependência, fácil pro dono do projeto entender |
| Hospedagem | GitHub Pages | Grátis, simples, já usa Git que o VS Code integra nativamente |
| Cardápio | PDF estático | Fácil de atualizar (o dono só troca o arquivo), sem precisar mexer em código |
| Contato | wa.me link | Zero custo, zero infraestrutura |

## Quando revisar esta arquitetura

Se no futuro surgir necessidade de: pagamento online, cadastro de clientes, painel de pedidos, ou automação de atendimento — reabrir este documento e registrar a mudança em `docs/DECISIONS.md` antes de implementar.
