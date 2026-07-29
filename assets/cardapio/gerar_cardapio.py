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

DIRETORIO_SCRIPT = os.path.dirname(os.path.abspath(__file__))
# O script mora em assets/cardapio/, entao a raiz do projeto fica dois niveis acima
PROJETO = os.path.dirname(os.path.dirname(DIRETORIO_SCRIPT))
SELO = f"{PROJETO}/assets/logo/belorae-selo-circular.jpg"
SAIDA = f"{PROJETO}/assets/cardapio/cardapio-belorae.pdf"

# Liberation Serif no Linux (ambiente original); em outros sistemas (ex. Windows,
# sem essas fontes instaladas), cai para as fontes serifadas base do reportlab
# (Times-Bold/Times-Italic), que nao precisam de arquivo externo nem registro.
_LIBERATION_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
_LIBERATION_ITALIC = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"

if os.path.exists(_LIBERATION_BOLD):
    pdfmetrics.registerFont(TTFont("BeloraeSerif-Bold", _LIBERATION_BOLD))
    FONTE_BOLD = "BeloraeSerif-Bold"
else:
    FONTE_BOLD = "Times-Bold"

if os.path.exists(_LIBERATION_ITALIC):
    pdfmetrics.registerFont(TTFont("BeloraeSerif-Italic", _LIBERATION_ITALIC))
    FONTE_ITALIC = "BeloraeSerif-Italic"
else:
    FONTE_ITALIC = "Times-Italic"

VERDE_ESCURO = colors.HexColor("#4F6647")
VERDE = colors.HexColor("#6E8763")
TEXTO = colors.HexColor("#3E2F22")
ACENTO = colors.HexColor("#C98A63")
CREME = colors.HexColor("#FAF6EE")
BADGE_FUNDO = colors.HexColor("#F3E4D6")
LINHA_SUAVE = colors.HexColor("#D8CDBB")

titulo_style = ParagraphStyle("Titulo", fontName=FONTE_BOLD, fontSize=21,
    textColor=VERDE_ESCURO, alignment=TA_CENTER, spaceAfter=4, leading=25)
subtitulo_style = ParagraphStyle("Subtitulo", fontName=FONTE_ITALIC, fontSize=11,
    textColor=TEXTO, alignment=TA_CENTER, spaceAfter=8, leading=13)
aviso_style = ParagraphStyle("Aviso", fontName=FONTE_ITALIC, fontSize=9,
    textColor=VERDE_ESCURO, alignment=TA_CENTER, leading=13)
categoria_style = ParagraphStyle("Categoria", fontName=FONTE_BOLD, fontSize=14,
    textColor=VERDE_ESCURO, spaceBefore=2, spaceAfter=5, alignment=TA_LEFT)
nome_style = ParagraphStyle("Nome", fontName=FONTE_BOLD, fontSize=11,
    textColor=TEXTO, alignment=TA_LEFT, leading=13)
preco_style = ParagraphStyle("Preco", fontName=FONTE_BOLD, fontSize=10,
    textColor=ACENTO, alignment=TA_RIGHT, leading=13)
desc_style = ParagraphStyle("Desc", fontName=FONTE_ITALIC, fontSize=8.7,
    textColor=colors.HexColor("#6B5A48"), alignment=TA_LEFT, leading=11)
footer_style = ParagraphStyle("Footer", fontName=FONTE_ITALIC, fontSize=9.5,
    textColor=TEXTO, alignment=TA_CENTER, leading=13)
footer_link_style = ParagraphStyle("FooterLink", fontName=FONTE_BOLD, fontSize=9.5,
    textColor=ACENTO, alignment=TA_CENTER, leading=13)

# Link de WhatsApp usado no rodape do PDF
LINK_WHATSAPP = "https://wa.me/5541996123682?text=Ol%C3%A1!%20Vi%20o%20site%20da%20Belorae%20e%20quero%20fazer%20um%20pedido."

# (nome, descricao, preco, caminho_da_foto_relativo_ao_projeto_ou_None)
CARDAPIO = [
    ("Bolos", [
        ("Bolo Integral de Cenoura",
         "Massa de cenoura com farinha integral, cobertura de chocolate 70% cacau. Sem açúcar refinado.",
         "Fatia R$ 12,00  |  Inteiro R$ 65,00",
         "assets/images/bolo-cenoura-placeholder.jpg"),
        ("Bolo de Chocolate com Amêndoas",
         "Massa de chocolate úmida com farinha de amêndoas, cobertura de brigadeiro. Sem açúcar refinado.",
         "Fatia R$ 13,00  |  Inteiro R$ 68,00",
         "assets/images/cardapio/bolo-chocolate-placeholder.jpg"),
        ("Bolo Vegano de Banana com Canela",
         "Receita sem ingredientes de origem animal na composição, adoçada com banana madura e um toque de canela.",
         "Fatia R$ 12,00  |  Inteiro R$ 60,00",
         "assets/images/cardapio/banana-canela-placeholder.jpg"),
        ("Bolo de Milho Cremoso",
         "Massa cremosa de milho verde, textura macia, sem açúcar refinado.",
         "Fatia R$ 12,00  |  Inteiro R$ 62,00",
         "assets/images/cardapio/bolo-milho-placeholder.jpg"),
        ("Bolo de Maracujá com Cobertura Leve",
         "Massa fofinha com suco concentrado de maracujá e cobertura leve de iogurte, sem açúcar refinado.",
         "Fatia R$ 13,00  |  Inteiro R$ 66,00",
         "assets/images/cardapio/bolo-maracuja-placeholder.jpg"),
        ("Bolo de Laranja com Especiarias",
         "Massa aromática de laranja com canela e cravo, sem açúcar refinado.",
         "Fatia R$ 12,00  |  Inteiro R$ 62,00",
         "assets/images/cardapio/bolo-laranja-placeholder.jpg"),
    ]),
    ("Brownies", [
        ("Brownie Fit de Amêndoas",
         "Farinha de amêndoas, textura úmida e intensa em chocolate.",
         "Unidade R$ 9,00  |  Caixa c/ 6 R$ 48,00",
         "assets/images/brownie-placeholder.jpg"),
        ("Brownie de Doce de Leite",
         "Brownie úmido com um recheio surpresa de doce de leite. Sem açúcar refinado.",
         "Unidade R$ 10,00  |  Caixa c/ 6 R$ 54,00",
         "assets/images/cardapio/brownie-doce-de-leite-placeholder.jpg"),
        ("Brownie de Castanhas",
         "Textura densa e úmida, com pedaços generosos de castanha-do-pará. Sem açúcar refinado.",
         "Unidade R$ 10,00  |  Caixa c/ 6 R$ 54,00",
         "assets/images/cardapio/brownie-castanhas-placeholder.jpg"),
        ("Brownie Leve de Coco",
         "Feito com óleo de coco, adoçado de forma mais suave, uma opção mais leve para o seu dia.",
         "Unidade R$ 9,00  |  Caixa c/ 6 R$ 48,00",
         "assets/images/cardapio/brownie-coco-placeholder.jpg"),
        ("Brownie Trio de Chocolates",
         "Camadas de chocolate ao leite, meio amargo e branco, sem açúcar refinado.",
         "Unidade R$ 11,00  |  Caixa c/ 6 R$ 60,00",
         "assets/images/cardapio/brownie-trio-chocolates-placeholder.jpg"),
        ("Brownie de Pistache",
         "Massa de chocolate com pedaços generosos de pistache.",
         "Unidade R$ 11,00  |  Caixa c/ 6 R$ 60,00",
         "assets/images/cardapio/brownie-pistache-placeholder.jpg"),
    ]),
    ("Bolachas", [
        ("Cookies de Aveia e Castanhas",
         "Aveia, castanhas e gotas de chocolate meio amargo. Crocante por fora, macio por dentro.",
         "Unidade R$ 7,00  |  Pacote c/ 4 R$ 24,00",
         "assets/images/cookies-placeholder.jpg"),
        ("Bolacha de Especiarias",
         "Bolachinha crocante com canela, gengibre e cravo, uma releitura mais leve do biscoito de especiarias.",
         "Pacote c/ 4 R$ 14,00",
         "assets/images/cardapio/bolacha-especiarias-placeholder.jpg"),
        ("Biscoito de Cacau",
         "Crocante, feito com cacau intenso.",
         "Pacote c/ 4 R$ 13,00",
         "assets/images/cardapio/biscoito-cacau-placeholder.jpg"),
        ("Biscoito de Coco",
         "Sabor suave de coco, crocante por fora.",
         "Pacote c/ 4 R$ 13,00",
         "assets/images/cardapio/biscoito-coco-placeholder.jpg"),
        ("Cookie de Amendoim com Gotas de Chocolate",
         "Sabor marcante de amendoim com gotas de chocolate meio amargo.",
         "Unidade R$ 7,00  |  Pacote c/ 4 R$ 25,00",
         "assets/images/cardapio/cookie-amendoim-placeholder.jpg"),
        ("Bolacha de Aveia com Frutas Vermelhas",
         "Aveia crocante com pedaços de frutas vermelhas desidratadas, sem açúcar refinado.",
         "Pacote c/ 4 R$ 15,00",
         "assets/images/cardapio/bolacha-aveia-frutas-placeholder.jpg"),
    ]),
    ("Doces e Brigadeiros", [
        ("Trufa de Cacau 70% com Castanha-do-Pará",
         "Trufa pequena, cacau intenso, sem açúcar refinado.",
         "Unidade R$ 6,00  |  Caixa c/ 6 R$ 32,00",
         "assets/images/cardapio/trufa-placeholder.png"),
        ("Brigadeiro Gourmet de Pistache",
         "Brigadeiro cremoso envolto em pistache triturado, feito sem açúcar refinado.",
         "Unidade R$ 8,00  |  Caixa c/ 6 R$ 42,00",
         "assets/images/cardapio/brigadeiro-pistache-placeholder.jpg"),
        ("Brigadeiro de Ninho com Avelã",
         "Brigadeiro de leite ninho com um toque de creme de avelã, sem açúcar refinado.",
         "Unidade R$ 8,00  |  Caixa c/ 6 R$ 42,00",
         "assets/images/cardapio/brigadeiro-avela-placeholder.jpg"),
        ("Brigadeiro Trufado de Avelã Crocante",
         "Base de brigadeiro com creme de avelã e um crocante de castanhas por fora.",
         "Unidade R$ 8,00  |  Caixa c/ 6 R$ 42,00",
         "assets/images/cardapio/brigadeiro-avela-crocante-placeholder.jpg"),
        ("Docinho de Coco Queimado",
         "Clássico docinho brasileiro reinventado sem açúcar refinado, com coco levemente tostado.",
         "Unidade R$ 5,00  |  Caixa c/ 6 R$ 26,00",
         "assets/images/cardapio/docinho-coco-placeholder.jpg"),
        ("Bombom de Damasco com Castanhas",
         "Damasco recheado com um creme leve de castanhas, envolto em chocolate meio amargo.",
         "Unidade R$ 7,00  |  Caixa c/ 6 R$ 38,00",
         "assets/images/cardapio/bombom-damasco-placeholder.jpg"),
    ]),
    ("Salgados", [
        ("Mini Pão Sírio de Frango com Alface, Requeijão e Cenoura",
         "Pão sírio mini recheado com frango desfiado, alface fresca, requeijão light e cenoura ralada.",
         "Unidade R$ 8,00  |  Caixa c/ 6 R$ 42,00",
         "assets/images/cardapio/pao-sirio-frango-placeholder.jpg"),
        ("Sanduíche Natural de Frango com Requeijão e Rúcula",
         "Pão de forma integral com frango desfiado, requeijão light e rúcula fresca.",
         "Unidade R$ 12,00",
         "assets/images/cardapio/sanduiche-natural-frango-placeholder.jpg"),
        ("Sanduíche Natural de Atum com Requeijão e Tomate",
         "Pão de forma integral com atum, requeijão light e tomate fresco.",
         "Unidade R$ 12,00",
         "assets/images/cardapio/sanduiche-natural-atum-placeholder.jpg"),
    ]),
]

# Secao especial: sem itens de catalogo com preco fixo (por isso fica fora da
# tabela CARDAPIO), mas e um servico que a Belorae ja atende de verdade.
# Objetivo: deixar claro que esse publico (festas e eventos) e atendido,
# e direcionar para contato via WhatsApp, ja que cada pedido e sob consulta.
FESTAS_EVENTOS = {
    "titulo": "Festas e Eventos",
    "flag": "SOB CONSULTA",
    "texto": (
        "A Belorae também atende festas e eventos: bolos e docinhos personalizados "
        "para aniversários, casamentos e eventos empresariais, sob consulta de "
        "disponibilidade e valores conforme o pedido."
    ),
    "cta": "Consultar disponibilidade pelo WhatsApp",
}

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
    story.append(Paragraph("Feito à mão, com carinho e cuidado em cada etapa. Pedidos via WhatsApp.", subtitulo_style))

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
    story.append(Spacer(1, 4))

    alergenos_tabela = Table(
        [[Paragraph(
            "Produzimos em cozinha artesanal que também manipula trigo, leite e oleaginosas "
            "(castanhas, amêndoas, avelã, pistache, castanha-do-pará). Se você tem alergia ou "
            "restrição alimentar, fale com a gente antes de pedir.",
            aviso_style,
        )]],
        colWidths=[150 * mm],
    )
    alergenos_tabela.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#EFF1E9")),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(alergenos_tabela)
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

    # Bloco "Festas e Eventos": servico real, sob consulta (sem preco fixo em catalogo)
    story.append(Spacer(1, 6))
    festas_flag = Table(
        [[Paragraph(FESTAS_EVENTOS["flag"], ParagraphStyle(
            "FestasFlag", fontName=FONTE_BOLD, fontSize=8,
            textColor=colors.HexColor("#FFFFFF"), alignment=TA_CENTER, leading=10))]],
        colWidths=[32 * mm],
    )
    festas_flag.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), VERDE_ESCURO),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]))
    festas_cta = Paragraph(
        f'<link href="{LINK_WHATSAPP}"><u>{FESTAS_EVENTOS["cta"]}</u></link>',
        ParagraphStyle("FestasCta", fontName=FONTE_BOLD, fontSize=9,
            textColor=ACENTO, alignment=TA_LEFT, leading=12, spaceBefore=4),
    )
    festas_bloco = Table(
        [[[Paragraph(FESTAS_EVENTOS["titulo"], categoria_style), festas_flag,
           Spacer(1, 3), Paragraph(FESTAS_EVENTOS["texto"], desc_style),
           festas_cta]]],
        colWidths=[150 * mm],
    )
    festas_bloco.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BADGE_FUNDO),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(festas_bloco)

    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=0.6, color=VERDE, spaceAfter=6))
    story.append(Paragraph(
        "Belorae Confeitaria Saudável. Rio Negro, PR. Atendemos Mafra e região. Pedidos via WhatsApp.",
        footer_style,
    ))
    story.append(Paragraph(
        f'<link href="{LINK_WHATSAPP}"><u>Fazer pedido pelo WhatsApp</u></link>',
        footer_link_style,
    ))

    doc.build(story, onFirstPage=fundo_pagina, onLaterPages=fundo_pagina)
    print("PDF v3 gerado em:", SAIDA)

if __name__ == "__main__":
    build()
