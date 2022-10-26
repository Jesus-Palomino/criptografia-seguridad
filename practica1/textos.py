import string
import os

class Textos:

    textoPlano = ""
    textoProcesado = ""
    textoNumerico = []
    ficheroInput = ""
    ficheroOutput = ""

    mapa = None                                     #   Diccionario de letras a numeros Ej. a:0
    abecedario = list(string.ascii_lowercase)


    def __init__(self, input, output):
        self.ficheroInput = input
        self.ficheroOutput = output
        self.crearMapa()
        self.leerFicheroInput()

    # Creacion de diccionario de letras con su equivalencia numerica
    def crearMapa(self):
        self.mapa = { i : self.abecedario[i] for i in range(0, len(self.abecedario) ) }
        self.mapa = {v: k for k, v in self.mapa.items()}

    # Leer contenidos de fichero input y convertir texto plano a numerico
    def leerFicheroInput(self):
        fichero = open(os.getcwd()+"/ficheros/"+self.ficheroInput)
        while 1:
            char = fichero.read(1).lower()         
            if not char:
                break
            if char != " " and char.isalpha():
                self.textoPlano += char
                self.textoNumerico.append(self.mapa[char])

    # Convertir texto numerico a texto plano
    def numericoConvertirTexto(self, texto = textoNumerico):
        for num in texto:
            self.textoProcesado += self.abecedario[num]
    
    # Imprimir textos segun el tipo (cifrado o descifrado)
    def imprimirTextos(self, modo = True):
        fichero = open(os.getcwd()+"/ficheros/" + self.ficheroOutput, 'w')
        fichero.write("".join(self.textoProcesado))

        if(modo):
            mensaje1 = "Texto original"
            mensaje2 = "Texto cifrado"
        else:
            mensaje1 = "Texto cifrado"
            mensaje2 = "Texto decifrado"
        print(mensaje1)
        print(self.textoPlano,"\n\n")
        print(mensaje2)
        print(self.textoProcesado,"\n")