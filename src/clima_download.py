import json
import os
import requests
import logging
import sys
from collections import namedtuple
from generate_image import post


logging.basicConfig(stream=sys.stdout, format='%(name)s - %(levelname)s - %(message)s')

token = os.getenv('TOKEN')

def busca_clima(id: int):
    print(token)
    clima = requests.get(f'http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/{id}/days/15?token={token}').json()

    print(clima)
    post.generate_image(clima["id"],
                   "{} - {}".format(clima["name"], clima["state"]).upper(),
                   str(clima["data"][0]["temperature"]["max"]),
                   str(clima["data"][0]["temperature"]["min"]),
                   clima["data"][0]["text_icon"]["text"]["pt"].upper(),
                   str(clima["data"][0]["humidity"]["min"])+"%",
                   str(clima["data"][0]["rain"]["probability"])+"% " + str(clima["data"][0]["rain"]["precipitation"])+"mm " ,
                   clima["data"][0]["text_icon"]["icon"]["day"],
                   clima["data"][0]["text_icon"]["icon"]["morning"],
                   clima["data"][0]["text_icon"]["icon"]["afternoon"],
                   clima["data"][0]["text_icon"]["icon"]["night"],
                   clima["data"][1]["text_icon"]["icon"]["dawn"])


if __name__ == '__main__':
    busca_clima(3477)
    busca_clima(5959)
