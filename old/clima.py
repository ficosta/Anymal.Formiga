import PIL
from icons import *

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


HLight40 = ImageFont.truetype("fonts/HelveticaNeue-Light.ttf",40)
HUltraLight40 = ImageFont.truetype("fonts/HelveticaNeue-UltraLight.ttf",40)
HMedium40 = ImageFont.truetype("fonts/HelveticaNeue-Medium.ttf",40)


icon_font = ImageFont.truetype("fonts/weathericons-regular-webfont.ttf",80)
text = "Sample Text"

bg = Image.open("imagens/sol.jpg")
icone_climatempo = Image.open("imagens/climatempo.png")


draw = ImageDraw.Draw(bg)

#draw icon
draw.text((100,100), day_hail, fill=(255,255,255), font=icon_font)
draw.text((30,30), "Sao Paulo - SP", fill=(255,255,255), font=HLight40)



bg.paste(icone_climatempo, (370, 390), icone_climatempo)

del draw

bg.save("a_test.jpg")