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

CIDADE = "Sao Paulo - SP".upper()
MAXIMA = "22"
MINIMA = "8"
UMIDADE = "33%"
UV = "6"
PRECIPTACAO = "0% 0mm"

FONT_COLOR = (54, 54, 59)

bg = Image.open("images/bg_amarelo.jpg")
draw = ImageDraw.Draw(bg)

# Centralizar texto cidade
w, h = draw.textsize(CIDADE, font=GothamRnd_Book_75)
draw.text(((1080 - w) / 2, 90), text=CIDADE, fill=FONT_COLOR, font=GothamRnd_Book_75)

# Centralizar texto maxima
w, h = draw.textsize(MAXIMA, font=GothamRnd_Book_175)
draw.text((810 - (w / 2), 320), text=MAXIMA, fill=FONT_COLOR, font=GothamRnd_Book_175)

# Centralizar texto minima
w, h = draw.textsize(MINIMA, font=GothamRnd_Book_110)
draw.text((810 - (w / 2), 480), text=MINIMA, fill=FONT_COLOR, font=GothamRnd_Book_110)

# Umidade
draw.text((275, 745), text=UMIDADE, fill=FONT_COLOR, font=GothamRnd_Book_31)

# UV
draw.text((540, 745), text=UV, fill=FONT_COLOR, font=GothamRnd_Book_31)

# PRECIPTACAO
draw.text((780, 745), text=PRECIPTACAO, fill=FONT_COLOR, font=GothamRnd_Book_31)


#Icone principal
icone_principal = Image.open("images\\icons\\xl_1.png")
bg.paste(icone_principal,(135, 200), icone_principal)

#Icone 6
icone_principal = Image.open("images\\icons\\s_1.png").convert("RGBA")
bg.paste(icone_principal, (90, 940), icone_principal)

#Icone 12
icone_principal = Image.open("images\\icons\\s_1.png").convert("RGBA")
bg.paste(icone_principal, (360, 940), icone_principal)

#Icone 12
icone_principal = Image.open("images\\icons\\s_1.png").convert("RGBA")
bg.paste(icone_principal, (630, 940), icone_principal)

#Icone 12
icone_principal = Image.open("images\\icons\\s_1.png").convert("RGBA")
bg.paste(icone_principal, (900, 940), icone_principal)

bg.save("SP.jpg")
