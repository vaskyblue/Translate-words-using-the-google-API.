#traducir palabras en ingles a español y viceversa utilizando la consola 
#para ingresar las palabras y el programa las traduce y las muestra en la consola 

import os
import sys
import re
import json
import requests
import urllib.request
import urllib.parse
import urllib.error

def translate(to_translate, to_language="en", language="es"):
    # la base_url es la url de la api de google translate a la que se le va a enviar 
    # la palabra a traducir y el idioma de la palabra 
    base_url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl={}&tl={}&dt=t&q={}" 
    # to_translate es la palabra a traducir 
    to_translate = urllib.parse.quote(to_translate)
    # to_language es el idioma de la palabra a traducir
    url = base_url.format(language, to_language, to_translate)
    # se hace la peticion a la api de google translate
    response = urllib.request.urlopen(url)
    # se obtiene la respuesta en formato json
    result = json.loads(response.read().decode())
    # se obtiene la traduccion de la palabra
    return result[0][0][0]


def traducir(palabra):
    palabra = translate(palabra)
    return palabra


def main():
    while True:
        palabra = input("Ingrese la palabra a traducir: ")
        if palabra == "salir":
            break
        else:
            print(traducir(palabra))


if __name__ == "__main__":
    main()
    sys.exit(0)
    #print(traducir("hola"))


