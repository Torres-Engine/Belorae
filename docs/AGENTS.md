# AGENTS.md — Time de Agentes da Belorae

Time hierárquico de subagentes do Claude Code, salvos em `.claude/agents/`. Cada um tem um nome próprio (fácil de reconhecer no chat quando estão trabalhando) e escopo fechado — revisa (ou é revisado por) o próximo da fila, ninguém publica nada sem passar pela cadeia completa.

> Nota técnica: o arquivo continua com o nome do cargo (ex: `product-manager.md`), só o campo `name` dentro dele mudou para o nome próprio (ex: `fernanda`). Isso não muda como os agentes funcionam, só como você os reconhece e aciona.

## Fluxo hierárquico (quem confere quem)

```
Ricardo (CEO AI — orquestrador)
   │  define prioridade e sequência
   ▼
Fernanda (Product Manager)
   │  define O QUE (conteúdo, escopo, textos)
   ▼
Eduardo (Solution Architect)
   │  aprova COMO (viabilidade técnica, simplicidade)
   ▼
Marcos (Backend & Database Guardian)
   │  confirma que não precisa de servidor/banco (ou escala se precisar)
   ▼
Sofia (UX/UI Designer)
   │  define a direção visual antes de implementar
   ▼
Camila (Frontend Engineer)
   │  implementa (HTML/CSS/JS)
   ▼
Sofia (UX/UI Designer)
   │  revisão final de polimento visual
   ▼
Rafael (QA Engineer)
   │  testa — barra tudo que estiver quebrado
   ▼
Beatriz (Security Engineer)
   │  revisa dados sensíveis, links, credenciais
   ▼
Lucas (DevOps Engineer)
   │  publica (GitHub Pages)
   ▼
Juliana (Technical Writer)
      documenta (CHANGELOG, TASKS, README, CLAUDE.md)
```

Cada seta é um **gate**: o agente de baixo só começa depois que o de cima aprovou. Se algo falha, volta para o agente responsável — não pula etapa.

**Execução em ondas:** o fluxo acima mostra a ordem lógica, mas nem tudo precisa ser um atrás do outro. O Ricardo agrupa em **ondas** os agentes que não dependem do resultado um do outro (ex: Fernanda, Eduardo e Marcos podem revisar em paralelo antes da implementação; Rafael, Beatriz e Ricardo podem revisar em paralelo depois dela). Uma onda só avança pra próxima quando todo mundo dela aprovar. Ver exemplo aplicado em `SPEC.md`, seção 12.

## Tabela de referência rápida

| Nome | Cargo | O que faz | Não faz | Entrega para |
|---|---|---|---|---|
| **Ricardo** | CEO AI / Orquestrador | Prioriza e destrava impasses | Não implementa nada | Fernanda |
| **Fernanda** | Product Manager | Define conteúdo/escopo/textos | Não escreve código | Eduardo |
| **Eduardo** | Solution Architect | Aprova abordagem técnica mais simples | Não implementa produção | Marcos |
| **Marcos** | Backend & Database Guardian | Impede backend/banco desnecessário | Não implementa backend | Sofia |
| **Sofia** | UX/UI Designer | Define direção visual e cobra nível premium | Não escreve código, não decide conteúdo | Camila |
| **Camila** | Frontend Engineer | Implementa HTML/CSS/JS | Não decide conteúdo nem arquitetura | Sofia (revisão) → Rafael |
| **Rafael** | QA Engineer | Testa o fluxo de conversão (WhatsApp) | Não corrige código | Beatriz |
| **Beatriz** | Security Engineer | Revisa dados sensíveis e credenciais | Não implementa correções | Lucas |
| **Lucas** | DevOps Engineer | Publica no GitHub Pages | Não decide arquitetura de hospedagem | Juliana |
| **Juliana** | Technical Writer | Mantém docs/README/CLAUDE.md atualizados | Não decide nada técnico/produto | — (fim do ciclo) |

## Como usar no VS Code (extensão Claude Code)

Duas formas de acionar:

1. **Automática:** o Claude Code lê a `description` de cada agente e aciona sozinho o mais adequado, se o pedido combinar.
2. **Manual, pelo nome:** peça diretamente, ex: *"pede pra Fernanda revisar os textos do cardápio"* ou *"chama o Rafael pra testar antes de eu publicar"*.

Para um pedido grande (ex: "prepara o site pro lançamento"), comece pelo **Ricardo** — ele monta o plano e indica a ordem.

## Por que esse tamanho de time

Time completo de ponta a ponta, mas o papel do **Marcos** (Backend & Database Guardian) tem escopo intencionalmente pequeno nesta fase: o projeto não usa backend nem banco de dados (ver `docs/ARCHITECTURE.md`), então sua função principal hoje é **impedir** complexidade desnecessária, não construir. Se o negócio crescer e precisar de painel de pedidos ou pagamento online, é ele quem lidera a proposta — registrada primeiro em `docs/DECISIONS.md`.
