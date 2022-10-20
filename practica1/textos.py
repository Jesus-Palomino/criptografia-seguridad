import string
import os

class Textos:

    textoPlano = ""
    textoProcesado = ""
    textoNumerico = []

    mapa = None                                     #   Diccionario de letras a numeros Ej. a:0
    abecedario = list(string.ascii_lowercase)


    def __init__(self):
        self.crearMapa()
        self.textoConvertirNumerico()


    def crearMapa(self):
        self.mapa = { i : self.abecedario[i] for i in range(0, len(self.abecedario) ) }
        self.mapa = {v: k for k, v in self.mapa.items()}


    def textoConvertirNumerico(self):
        fichero = open(os.getcwd()+"/ficheros/input.txt")
        while 1:
            char = fichero.read(1).lower()         
            if not char:
                break
            if char != " " and char.isalpha():
                self.textoPlano += char
                self.textoNumerico.append(self.mapa[char])


    def numericoConvertirTexto(self, texto = textoNumerico):
        for num in texto:
            self.textoProcesado += self.abecedario[num]
    

    def imprimirTextos(self, modo = True, padding = 0):
        if(modo):
            mensaje1 = "Texto original"
            mensaje2 = "Texto cifrado"
        else:
            mensaje1 = "Texto cifrado"
            mensaje2 = "Texto decifrado"
        print(mensaje1, "\n", self.textoPlano, "\n\n", mensaje2)
        if(padding):
            print(self.textoProcesado[:-padding])
        else:
            print(self.textoProcesado)