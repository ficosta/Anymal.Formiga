from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# Definição tamanhos de fonte
GothamRnd_Book_25 = ImageFont.truetype("fonts\\GothamRnd-Book.otf", 25)
GothamRnd_Book_31 = ImageFont.truetype("fonts\\GothamRnd-Book.otf", 31)
GothamRnd_Book_42 = ImageFont.truetype("fonts\\GothamRnd-Book.otf", 42)
GothamRnd_Book_75 = ImageFont.truetype("fonts\\GothamRnd-Book.otf", 75)
GothamRnd_Book_110 = ImageFont.truetype("fonts\\GothamRnd-Book.otf", 110)
GothamRnd_Book_175 = ImageFont.truetype("fonts\\GothamRnd-Book.otf", 175)

FONT_COLOR = (54, 54, 59)
class post():
    def generate_image(id: int, cidade: str, maxima: str, minima: str,  texto: str, umidade: str, preciptacao: str, icone: str,
                       icone_6: str, icone_12: str, icone_16: str, icone_24: str):


        bg = Image.open("images/bg_amarelo.jpg")
        draw = ImageDraw.Draw(bg)

        # Centralizar texto cidade
        w, h = draw.textsize(cidade, font=GothamRnd_Book_75)
        draw.text(((1080 - w) / 2, 90), text=cidade, fill=FONT_COLOR, font=GothamRnd_Book_75)

        # Centralizar texto maxima
        w, h = draw.textsize(maxima, font=GothamRnd_Book_175)
        draw.text((810 - (w / 2), 320), text=maxima, fill=FONT_COLOR, font=GothamRnd_Book_175)

        # Centralizar texto minima
        w, h = draw.textsize(minima, font=GothamRnd_Book_110)
        draw.text((810 - (w / 2), 480), text=minima, fill=FONT_COLOR, font=GothamRnd_Book_110)

        # texto
        w, h = draw.textsize(texto, font=GothamRnd_Book_31)
        draw.text((370 - (w / 2), 740), text=texto, fill=FONT_COLOR, font=GothamRnd_Book_31)

        # Umidade
        draw.text((835, 710), text=umidade, fill=FONT_COLOR, font=GothamRnd_Book_31)

        # PRECIPTACAO
        draw.text((835, 765), text=preciptacao, fill=FONT_COLOR, font=GothamRnd_Book_31)

        # Icone principal
        icone = Image.open(f"images\\icons\\xl_{icone}.png")
        bg.paste(icone, (135, 200), icone)

        # Icone 6
        icone = Image.open(f"images\\icons\\s_{icone_6}.png")
        bg.paste(icone, (90, 940), icone)

        # Icone 12
        icone = Image.open(f"images\\icons\\s_{icone_12}.png")
        bg.paste(icone, (360, 940), icone)

        # Icone 12
        icone = Image.open(f"images\\icons\\s_{icone_16}.png")
        bg.paste(icone, (630, 940), icone)

        # Icone 12
        icone = Image.open(f"images\\icons\\s_{icone_24}.png")
        bg.paste(icone, (900, 940), icone)

        bg.save(f"{id}.jpg")
