# -*- coding: utf-8 -*-
"""
Gera docs/FICHA-TECNICA-PRODUTOS.pdf a partir de docs/FICHA-TECNICA-PRODUTOS.md.
Capa personalizada com a marca Belorae; miolo formatado seguindo as regras
gerais da ABNT NBR 14724 (margens 3-2-3-2 cm, fonte serifada 12pt, espacamento
1,5, numeracao de pagina no canto superior direito a partir da primeira
pagina de conteudo).
Requer: reportlab (mesma dependencia do gerar_cardapio.py).
"""
import os
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, NextPageTemplate, PageBreak,
    Paragraph, Spacer, Image, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

DIRETORIO_SCRIPT = os.path.dirname(os.path.abspath(__file__))
PROJETO = os.path.dirname(DIRETORIO_SCRIPT)
ORIGEM_MD = os.path.join(DIRETORIO_SCRIPT, "FICHA-TECNICA-PRODUTOS.md")
SAIDA = os.path.join(DIRETORIO_SCRIPT, "FICHA-TECNICA-PRODUTOS.pdf")
LOGO_CAPA = os.path.join(PROJETO, "assets", "logo", "belorae-logo-vertical.jpg")

_LIBERATION_REGULAR = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
_LIBERATION_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
_LIBERATION_ITALIC = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"

if os.path.exists(_LIBERATION_REGULAR):
    pdfmetrics.registerFont(TTFont("BeloraeSerif", _LIBERATION_REGULAR))
    FONTE = "BeloraeSerif"
else:
    FONTE = "Times-Roman"

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

VERDE_MARCA = colors.HexColor("#4A543C")
VERDE_ESCURO = colors.HexColor("#4F6647")
VERDE = colors.HexColor("#6E8763")
TEXTO = colors.HexColor("#3E2F22")
ACENTO = colors.HexColor("#C98A63")
CREME = colors.HexColor("#FAF6EE")
LINHA_SUAVE = colors.HexColor("#D8CDBB")

# ===== Margens ABNT NBR 14724: superior 3cm, esquerda 3cm, inferior 2cm, direita 2cm =====
MARGEM_SUP = 3 * cm
MARGEM_ESQ = 3 * cm
MARGEM_INF = 2 * cm
MARGEM_DIR = 2 * cm

# ===== Estilos do miolo (ABNT: fonte serifada 12pt, espacamento 1,5) =====
corpo_style = ParagraphStyle(
    "Corpo", fontName=FONTE, fontSize=12, leading=18,
    textColor=TEXTO, alignment=TA_JUSTIFY, spaceAfter=8,
)
campo_style = ParagraphStyle(
    "Campo", fontName=FONTE, fontSize=12, leading=18,
    textColor=TEXTO, alignment=TA_LEFT, spaceAfter=4,
)
titulo1_style = ParagraphStyle(
    "Titulo1", fontName=FONTE_BOLD, fontSize=14, leading=18,
    textColor=VERDE_ESCURO, alignment=TA_LEFT, spaceBefore=18, spaceAfter=10,
)
titulo2_style = ParagraphStyle(
    "Titulo2", fontName=FONTE_BOLD, fontSize=12, leading=16,
    textColor=VERDE_ESCURO, alignment=TA_LEFT, spaceBefore=12, spaceAfter=6,
)
aviso_style = ParagraphStyle(
    "Aviso", fontName=FONTE_ITALIC, fontSize=10, leading=14,
    textColor=TEXTO, alignment=TA_JUSTIFY, spaceAfter=4,
)
tabela_cabecalho_style = ParagraphStyle(
    "TabelaCabecalho", fontName=FONTE_BOLD, fontSize=10, leading=13,
    textColor=colors.HexColor("#FFFFFF"), alignment=TA_LEFT,
)
tabela_celula_style = ParagraphStyle(
    "TabelaCelula", fontName=FONTE, fontSize=10, leading=13,
    textColor=TEXTO, alignment=TA_LEFT,
)

# ===== Capa =====
capa_titulo_style = ParagraphStyle(
    "CapaTitulo", fontName=FONTE_BOLD, fontSize=22, leading=27,
    textColor=VERDE_ESCURO, alignment=TA_CENTER, spaceBefore=28, spaceAfter=6,
)
capa_subtitulo_style = ParagraphStyle(
    "CapaSubtitulo", fontName=FONTE_ITALIC, fontSize=13, leading=17,
    textColor=TEXTO, alignment=TA_CENTER, spaceAfter=4,
)
capa_rodape_style = ParagraphStyle(
    "CapaRodape", fontName=FONTE, fontSize=11, leading=15,
    textColor=TEXTO, alignment=TA_CENTER,
)


def fundo_capa(canvas, doc):
    canvas.saveState()
    largura, altura = A4
    canvas.setFillColor(CREME)
    canvas.rect(0, 0, largura, altura, stroke=0, fill=1)
    canvas.setStrokeColor(VERDE)
    canvas.setLineWidth(1.2)
    canvas.rect(1.5 * cm, 1.5 * cm, largura - 3 * cm, altura - 3 * cm, stroke=1, fill=0)
    canvas.restoreState()


def fundo_miolo(canvas, doc):
    """Pagina de conteudo: fundo branco padrao ABNT, numero de pagina no canto
    superior direito (2 cm da borda superior e da borda direita)."""
    canvas.saveState()
    canvas.setFont(FONTE, 10)
    canvas.setFillColor(TEXTO)
    largura, altura = A4
    numero = canvas.getPageNumber() - 1  # capa nao conta como pagina numerada visivel
    canvas.drawRightString(largura - MARGEM_DIR, altura - 2 * cm, str(numero))
    canvas.restoreState()


def construir_capa():
    elementos = []
    elementos.append(Spacer(1, 4 * cm))
    if os.path.exists(LOGO_CAPA):
        elementos.append(Image(LOGO_CAPA, width=7 * cm, height=8.1 * cm, hAlign="CENTER"))
    elementos.append(Spacer(1, 1.5 * cm))
    elementos.append(Paragraph("FICHA TÉCNICA DE PRODUTOS", capa_titulo_style))
    elementos.append(Paragraph("Linha de produtos saudáveis Belorae", capa_subtitulo_style))
    elementos.append(Spacer(1, 0.4 * cm))
    elementos.append(Paragraph("Documento interno de produção. Template de referência.", capa_subtitulo_style))
    elementos.append(Spacer(1, 6 * cm))
    elementos.append(Paragraph("Rio Negro, Paraná", capa_rodape_style))
    elementos.append(Paragraph("2026", capa_rodape_style))
    return elementos


def linha_para_paragrafo(linha):
    """Converte negrito markdown (**texto**) para a tag <b> do reportlab."""
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", linha)


def construir_miolo(caminho_md):
    with open(caminho_md, "r", encoding="utf-8") as f:
        linhas = [l.rstrip("\n") for l in f.readlines()]

    elementos = []
    i = 0
    dentro_aviso = False
    buffer_aviso = []

    def fecha_aviso():
        nonlocal dentro_aviso, buffer_aviso
        if buffer_aviso:
            texto = " ".join(buffer_aviso)
            elementos.append(Paragraph(linha_para_paragrafo(texto), aviso_style))
            elementos.append(Spacer(1, 6))
        dentro_aviso = False
        buffer_aviso = []

    while i < len(linhas):
        linha = linhas[i].strip()

        if linha.startswith("> "):
            dentro_aviso = True
            buffer_aviso.append(linha[2:].lstrip(">").strip())
            i += 1
            continue
        elif dentro_aviso and linha.startswith(">"):
            buffer_aviso.append(linha.lstrip(">").strip())
            i += 1
            continue
        elif dentro_aviso:
            fecha_aviso()

        if not linha:
            i += 1
            continue

        if linha.startswith("# "):
            i += 1
            continue

        if linha.startswith("## "):
            elementos.append(PageBreak())
            elementos.append(Paragraph(linha[3:].upper(), titulo1_style))
            elementos.append(HRFlowable(width="100%", thickness=0.8, color=VERDE, spaceAfter=10))
            i += 1
            continue

        if linha.startswith("### "):
            elementos.append(Paragraph(linha[4:], titulo2_style))
            i += 1
            continue

        if linha == "---":
            i += 1
            continue

        if linha.startswith("|"):
            linhas_tabela = []
            while i < len(linhas) and linhas[i].strip().startswith("|"):
                linhas_tabela.append(linhas[i].strip())
                i += 1
            dados = []
            for j, lt in enumerate(linhas_tabela):
                if set(lt.replace("|", "").strip()) <= {"-", " "}:
                    continue
                celulas = [c.strip() for c in lt.strip("|").split("|")]
                if j == 0:
                    dados.append([Paragraph(c, tabela_cabecalho_style) for c in celulas])
                else:
                    dados.append([Paragraph(linha_para_paragrafo(c), tabela_celula_style) for c in celulas])
            if dados:
                largura_util = A4[0] - MARGEM_ESQ - MARGEM_DIR
                n_col = len(dados[0])
                larguras = [largura_util * 0.42] + [largura_util * (0.58 / (n_col - 1))] * (n_col - 1) if n_col > 1 else None
                tabela = Table(dados, colWidths=larguras)
                tabela.setStyle(TableStyle([
                    ("BACKGROUND", (0, 0), (-1, 0), VERDE_ESCURO),
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("GRID", (0, 0), (-1, -1), 0.5, LINHA_SUAVE),
                    ("TOPPADDING", (0, 0), (-1, -1), 4),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                    ("LEFTPADDING", (0, 0), (-1, -1), 6),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ]))
                elementos.append(tabela)
                elementos.append(Spacer(1, 8))
            continue

        if linha.startswith("- **"):
            elementos.append(Paragraph(linha_para_paragrafo(linha[2:]), campo_style))
            i += 1
            continue

        if re.match(r"^\d+\.\s", linha):
            elementos.append(Paragraph(linha_para_paragrafo(linha), corpo_style))
            i += 1
            continue

        elementos.append(Paragraph(linha_para_paragrafo(linha), corpo_style))
        i += 1

    fecha_aviso()
    return elementos


def build():
    doc = BaseDocTemplate(
        SAIDA, pagesize=A4,
        topMargin=MARGEM_SUP, bottomMargin=MARGEM_INF,
        leftMargin=MARGEM_ESQ, rightMargin=MARGEM_DIR,
        title="Ficha Tecnica de Produtos Belorae",
    )

    frame_capa = Frame(0, 0, A4[0], A4[1], id="capa", leftPadding=2.5 * cm, rightPadding=2.5 * cm,
                        topPadding=1 * cm, bottomPadding=1 * cm)
    frame_miolo = Frame(MARGEM_ESQ, MARGEM_INF, A4[0] - MARGEM_ESQ - MARGEM_DIR,
                         A4[1] - MARGEM_SUP - MARGEM_INF, id="miolo")

    doc.addPageTemplates([
        PageTemplate(id="Capa", frames=[frame_capa], onPage=fundo_capa),
        PageTemplate(id="Miolo", frames=[frame_miolo], onPage=fundo_miolo),
    ])

    story = construir_capa()
    story.append(NextPageTemplate("Miolo"))
    story.append(PageBreak())
    story.extend(construir_miolo(ORIGEM_MD))

    doc.build(story)
    print("PDF gerado em:", SAIDA)


if __name__ == "__main__":
    build()
