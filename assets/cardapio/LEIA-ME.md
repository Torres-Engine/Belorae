# Cardápio em PDF

Coloque aqui o arquivo do cardápio com o nome exato:

```
cardapio-belorae.pdf
```

O botão "Abrir Cardápio (PDF)" do site e a mensagem automática do WhatsApp já apontam para esse nome de arquivo — não é preciso mexer em código, só substituir o PDF.

**Dica de conteúdo do PDF:** nome do produto, descrição curta, preço, e se possível uma foto pequena de cada item. Manter o arquivo leve (menos de 5MB) para abrir rápido no celular.

## Como o PDF atual foi gerado

`gerar_cardapio.py` neste mesmo diretório monta o PDF automaticamente (fontes, cores da marca, fotos por item) a partir de uma lista de produtos escrita no próprio script. Não precisa mexer nele diretamente — quando o cardápio real (produtos, preços, fotos) estiver definido, é só pedir pro Claude atualizar a lista e rodar o script de novo. Requer Python 3 com as bibliotecas `reportlab` e `Pillow` instaladas.
