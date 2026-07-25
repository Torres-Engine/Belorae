# -*- coding: utf-8 -*-
import io, os
from PIL import Image as PILImage
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT

PROJETO = "/sessions/zen-nifty-mendel/mnt/Belorae Start R0"
SELO = f"{PROJETO}/assets/logo/belorae-selo-circular.jpg"
SAIDA = f"{PROJETO}/assets/cardapio/cardapio-belorae.pdf"

pdfmetrics.registerFont(TTFont("BeloraeSerif", "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"))
pdfmetrics.registerFont(TTFont("BeloraeSerif-Bold", "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("BeloraeSerif-Italic", "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"))

VERDE_ESCURO = colors.HexColor("#4F6647")
VERDE = colors.HexColor("#6E8763")
TEXTO = colors.HexColor("#3E2F22")
ACENTO = colors.HexColor("#C98A63")
CREME = colors.HexColor("#FAF6EE")
BADGE_FUNDO = colors.HexColor("#F3E4D6")
LINHA_SUAVE = colors.HexColor("#D8CDBB")

titulo_style = ParagraphStyle("Titulo", fontName="BeloraeSerif-Bold", fontSize=21,
    textColor=VERDE_ESCURO, alignment=TA_CENTER, spaceAfter=4, leading=25)
subtitulo_style = ParagraphStyle("Subtitulo", fontName="BeloraeSerif-Italic", fontSize=11,
    textColor=TEXTO, alignment=TA_CENTER, spaceAfter=8, leading=13)
aviso_style = ParagraphStyle("Aviso", fontName="BeloraeSerif-Italic", fontSize=9,
    textColor=VERDE_ESCURO, alignment=TA_CENTER, leading=13)
categoria_style = ParagraphStyle("Categoria", fontName="BeloraeSerif-Bold", fontSize=14,
    textColor=VERDE_ESCURO, spaceBefore=2, spaceAfter=5, alignment=TA_LEFT)
nome_style = ParagraphStyle("Nome", fontName="BeloraeSerif-Bold", fontSize=11,
    textColor=TEXTO, alignment=TA_LEFT, leading=13)
preco_style = ParagraphStyle("Preco", fontName="BeloraeSerif-Bold", fontSize=10,
    textColor=ACENTO, alignment=TA_RIGHT, leading=13)
desc_style = ParagraphStyle("Desc", fontName="BeloraeSerif-Italic", fontSize=8.7,
    textColor=colors.HexColor("#6B5A48"), alignment=TA_LEFT, leading=11)
footer_style = ParagraphStyle("Footer", fontName="BeloraeSerif-Italic", fontSize=9.5,
    textColor=TEXTO, alignment=TA_CENTER, leading=13)

# (nome, descricao, preco, caminho_da_foto_relativo_ao_projeto_ou_None)
CARDAPIO = [
    ("Bolos", [
        ("Bolo Integral de Cenoura",
         "Massa de cenoura com farinha integral, cobertura de chocolate 70% cacau. Sem açúcar refinado.",
         "Fatia R$ 12,00  |  Inteiro R$ 65,00",
         "assets/images/bolo-cenoura-placeholder.jpg"),
        ("Bolo Vegano de Banana com Canela",
         "Sem ingredientes de origem animal, adoçado com banana madura e um toque de canela.",
         "Fatia R$ 12,00  |  Inteiro R$ 60,00",
         "assets/images/cardapio/banana-canela-placeholder.jpg"),
    ]),
    ("Doces individuais", [
        ("Brownie Fit de Amêndoas",
         "Farinha de amêndoas e adoçante natural, textura úmida, sem glúten.",
         "Unidade R$ 9,00  |  Caixa c/ 6 R$ 48,00",
         "assets/images/brownie-placeholder.jpg"),
        ("Cookies Sem Glúten",
         "Aveia, castanhas e gotas de chocolate meio amargo. Crocante por fora, macio por dentro.",
         "Unidade R$ 7,00  |  Pacote c/ 4 R$ 24,00",
         "assets/images/cookies-placeholder.jpg"),
        ("Trufa de Cacau 70% com Castanha-do-Pará",
         "Trufa pequena, cacau intenso, sem açúcar refinado.",
         "Unidade R$ 6,00  |  Caixa c/ 6 R$ 32,00",
         "assets/images/cardapio/trufa-placeholder.png"),
    ]),
    ("Sem açúcar / linha diet", [
        ("Cheesecake Proteico de Frutas Vermelhas",
         "Base de castanhas, recheio proteico, cobertura de frutas vermelhas frescas.",
         "Fatia R$ 14,00",
         "assets/images/cheesecake-placeholder.jpg"),
        ("Pavê Fit de Morango",
         "Camadas de biscoito integral, creme leve e morango, montado em copo individual.",
         "Porção individual R$ 15,00",
         "assets/images/cardapio/pave-morango-placeholder.jpg"),
    ]),
    ("Salgados fit", [
        ("Mini Quiche de Legumes",
         "Massa sem glúten, recheio de legumes e ovos.",
         "Unidade R$ 8,00  |  Caixa c/ 6 R$ 42,00",
         "assets/images/cardapio/quiche-placeholder.jpg"),
    ]),
]

def foto_quadrada(caminho_relativo, tamanho_px=300):
    """Recorta a imagem em quadrado central e devolve um flowable Image do reportlab.
    Se o arquivo nao existir ainda, devolve None (o item aparece so com texto)."""
    caminho = os.path.join(PROJETO, caminho_relativo)
    if not os.path.exists(caminho):
        return None
    try:
        img = PILImage.open(caminho).convert("RGB")
    except Exception:
        return None
    w, h = img.size
    lado = min(w, h)
    esquerda = (w - lado) // 2
    topo = (h - lado) // 2
    img = img.crop((esquerda, topo, esquerda + lado, topo + lado)).resize((tamanho_px, tamanho_px))
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=85)
    buf.seek(0)
    return Image(buf, width=20 * mm, height=20 * mm)

def fundo_pagina(canvas, doc):
    canvas.saveState()
    largura, altura = A4
    canvas.setFillColor(CREME)
    canvas.rect(0, 0, largura, altura, stroke=0, fill=1)
    margem = 10 * mm
    canvas.setStrokeColor(VERDE)
    canvas.setLineWidth(0.8)
    canvas.roundRect(margem, margem, largura - 2 * margem, altura - 2 * margem, 8, stroke=1, fill=0)
    canvas.restoreState()

def linha_item(nome, desc, preco, foto_rel):
    foto = foto_quadrada(foto_rel)
    celula_texto = [Paragraph(nome, nome_style), Paragraph(desc, desc_style)]
    if foto:
        dados = [[foto, celula_texto, Paragraph(preco, preco_style)]]
        larguras = [23 * mm, 82 * mm, 45 * mm]
    else:
        dados = [[celula_texto, Paragraph(preco, preco_style)]]
        larguras = [105 * mm, 45 * mm]
    tabela = Table(dados, colWidths=larguras)
    tabela.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return tabela

def build():
    doc = SimpleDocTemplate(
        SAIDA, pagesize=A4,
        topMargin=13 * mm, bottomMargin=13 * mm,
        leftMargin=24 * mm, rightMargin=24 * mm,
        title="Cardapio Belorae Confeitaria Saudavel (rascunho)",
    )
    story = []

    story.append(Image(SELO, width=20 * mm, height=20 * mm))
    story.append(Spacer(1, 4))
    story.append(Paragraph("Cardápio de Encomendas", titulo_style))
    story.append(Paragraph("Feito à mão, com ingredientes naturais. Pedidos via WhatsApp.", subtitulo_style))

    aviso_tabela = Table(
        [[Paragraph("RASCUNHO. Conteúdo e fotos de exemplo, produtos e preços reais ainda serão definidos pela Belorae.", aviso_style)]],
        colWidths=[150 * mm],
    )
    aviso_tabela.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BADGE_FUNDO),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(aviso_tabela)
    story.append(Spacer(1, 10))

    for i, (categoria, itens) in enumerate(CARDAPIO):
        if i > 0:
            story.append(Spacer(1, 3))
        story.append(Paragraph(categoria.upper(), categoria_style))
        story.append(HRFlowable(width="100%", thickness=0.6, color=VERDE, spaceAfter=6))
        for j, (nome, desc, preco, foto_rel) in enumerate(itens):
            story.append(linha_item(nome, desc, preco, foto_rel))
            if j < len(itens) - 1:
                story.append(HRFlowable(width="100%", thickness=0.4, color=LINHA_SUAVE, spaceBefore=4, spaceAfter=6))
            else:
                story.append(Spacer(1, 2))

    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=0.6, color=VERDE, spaceAfter=6))
    story.append(Paragraph(
        "Belorae Confeitaria Saudável. Rio Negro, PR. Atendemos Mafra e região. Pedidos via WhatsApp.",
        footer_style,
    ))

    doc.build(story, onFirstPage=fundo_pagina, onLaterPages=fundo_pagina)
    print("PDF v3 gerado em:", SAIDA)

if __name__ == "__main__":
    build()
