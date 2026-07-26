# Cardápio em PDF

Coloque aqui o arquivo do cardápio com o nome exato:

```
cardapio-belorae.pdf
```

O botão "Ver Cardápio" (na seção Cardápio do site, ao lado do botão "Fazer Pedido") já aponta para esse nome de arquivo — não é preciso mexer em código, só substituir o PDF. O link de WhatsApp com mensagem pronta também vive no rodapé do próprio PDF (gerado pelo script `gerar_cardapio.py`, ver abaixo), além de aparecer no botão "Fazer Pedido" e no botão flutuante fixo de WhatsApp do site (canto inferior direito da tela). No total, são 3 pontos de acesso ao WhatsApp: botão "Fazer Pedido", botão flutuante fixo e este link dentro do PDF.

**Dica de conteúdo do PDF:** nome do produto, descrição curta, preço, e se possível uma foto pequena de cada item. Manter o arquivo leve (menos de 5MB) para abrir rápido no celular.

## Como o PDF atual foi gerado

`gerar_cardapio.py` neste mesmo diretório monta o PDF automaticamente (fontes, cores da marca, fotos por item) a partir de uma lista de produtos escrita no próprio script. Não precisa mexer nele diretamente — quando o cardápio real (produtos, preços, fotos) estiver definido, é só pedir pro Claude atualizar a lista e rodar o script de novo. Requer Python 3 com as bibliotecas `reportlab` e `Pillow` instaladas.
