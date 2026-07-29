# EQUIPE_NEGOCIO.md — Time de Negócio da Belorae

Segundo time de agentes do Claude Code, salvo em `.claude/agents/`. Diferente do **time técnico** (Ricardo e equipe, ver `docs/AGENTS.md`), que cuida do site, este time cuida da **empresa em si**: produção, insumos, financeiro, marketing, atendimento, qualidade, jurídico e pessoas. Objetivo declarado pelo dono do projeto: transformar a Belorae na melhor confeitaria saudável da região.

> Nota técnica: assim como no time técnico, o `name` interno de cada agente é um nome próprio (fácil de reconhecer no chat), mas o arquivo mantém o nome do setor (ex: `financeiro.md` tem `name: renato`).

## Fluxo (quem aciona quem)

```
Marina (Diretora Geral / CEO do Negócio)
   │  decide prioridade e qual(is) setor(es) entram em ação
   ▼
Vitor (Produção)  ──┐
Patrícia (Compras)  ├─→ trabalham em conjunto: receita, insumo e custo
Renato (Financeiro) ┘   alimentam a precificação final
   │
   ▼
Bianca (Marketing & Vendas)  ──┐
Diego (Atendimento & Operação) ┘  comunicam e vendem o produto já precificado
   │
   ▼
Helena (Qualidade & Segurança Alimentar)   ─┐
Otávio (Jurídico & Regulatório)             ├─ camadas de proteção do negócio
Fabiana (Recursos Humanos)                 ─┘   e preparação para crescer
```

Não é uma cadeia rígida como o time técnico — a Marina decide, para cada pedido, quais setores respondem e se em paralelo ou em sequência (mesma lógica de "ondas" usada no time técnico).

## Tabela de referência rápida

| Nome | Setor | O que faz | Não faz |
|---|---|---|---|
| **Marina** | Diretora Geral / CEO do Negócio | Prioriza, aciona setores, aprova entregáveis | Não escreve os documentos dos setores |
| **Vitor** | Produção / Chef Executivo | Fichas técnicas, padroniza receitas e processo produtivo | Não define preço nem fornecedor |
| **Patrícia** | Compras & Insumos | Fornecedores, cotações, custo de insumo, estoque mínimo | Não define receita nem preço de venda |
| **Renato** | Financeiro | Precificação, fluxo de caixa, ponto de equilíbrio | Não define receita nem marketing |
| **Bianca** | Marketing & Vendas | Calendário de conteúdo, campanhas, posicionamento de marca | Não define preço final nem implementa o site |
| **Diego** | Atendimento & Operações de Pedido | Scripts de WhatsApp, fluxo de pedido, entrega, reclamações | Não decide marketing nem receita |
| **Helena** | Qualidade & Segurança Alimentar | Validade, rotulagem, alérgenos, boas práticas de higiene | Não substitui vigilância sanitária real |
| **Otávio** | Jurídico & Regulatório | Formalização, nota fiscal, alvarás, LGPD básico | Não substitui advogado/contador real |
| **Fabiana** | Recursos Humanos | Descrição de cargos futuros, checklist de contratação/treinamento | Não contrata ninguém de fato |

## Como usar no VS Code

Peça diretamente pelo nome, ex: *"pede pra Patrícia levantar fornecedores de farinha de amêndoa na região"* ou *"chama a Helena pra montar a ficha de rotulagem do brownie"*.

Para um pedido grande ou vago (ex: "organiza minha empresa", "preciso de toda a documentação do negócio"), comece pela **Marina** — ela decide quais setores entram em ação e em que ordem.

## Relação com o time técnico

Os dois times são independentes, mas se cruzam em alguns pontos: o posicionamento de marca da Bianca deve ser coerente com a identidade visual que a Sofia (time técnico) aplica no site; os produtos e preços que o Vitor/Renato definem alimentam o cardápio do site, mantido pelo time técnico.
