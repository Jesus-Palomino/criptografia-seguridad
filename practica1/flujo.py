import sys
import os
import random
from datetime import datetime
from textos import Textos

class Flujo:

    texto = Textos()
    llave = []                          #   Llave en forma de texto
    textoNumericoProcesado = []
    n = 0
    lenSC = 10                          #   Longitud de secuencia cifrante

    def __init__(self, modo = True):
        # Longitud de texto original
        self.n = len(self.texto.textoPlano)

        if(modo):
            self.cifrado()
        else:
            self.descifrado()

        self.texto.imprimirTextos(modo)

    def crearLlave(self):
        random.seed(int(datetime.now().strftime("%Y%m%d%H%M%S")))

        # Creacion de valores iniciales llave ESTOS SERIAN LOS RANDOM?
        # self.funcionLFSR = [1,2]        # MODIFICAR
        # llave = [2, 4]                  # MODIFICAR

        # Caso de logitud de secuencia cifrante mayor a longitud de texto a cifrar
        n = min(self.n, self.lenSC)

        # Generacion de valores random para secuencia cifrante
        num = 999999999
        funcionLFSR = random.sample(range(-num, num), n)
        llave = random.sample(range(0, 26), n)

        num = len(funcionLFSR)
        start = 0

        # Calculo de cada valor restante de la llave
        while (len(llave) < self.n):
            # Calcular suma con modulo 26
            value = 0

            for i in range(num):
                value += funcionLFSR[i] * llave[i + start]

            llave.append(value % 26)
            start += 1

        self.llave = llave
        self.texto.numericoConvertirTexto(self.llave)
        textoLlave = self.texto.textoProcesado
        # Limpiar texto procesado --> para ser usado para guarder texto cifrado
        self.texto.textoProcesado = ""

        # Escribir llave en fichero para utilizarla en el descifrado
        fichero = open(os.getcwd()+"/ficheros/llaveFlujo.txt", "w")
        fichero.write(textoLlave)
        fichero.close()


    def leerLlave(self):
        # Lectura de llave del fichero
        fichero = open(os.getcwd()+"/ficheros/llaveFlujo.txt")
        for i in range(self.n):
            char = fichero.read(1).lower()
            if not char:
                break
            if char != " " and char.isalpha():
                self.llave.append(self.texto.mapa[char])
        fichero.close()
        # Verificar que la llave no sea menor en logitud que el texto a descifrar.
        # En caso de que sea mayor, se toman los n primeros caracteres, donde n es la longitud del texto.
        if(len(self.llave) < self.n):
            raise ValueError('El texto a descifrar debe de tener una longitud igual a la llave')
        

    def cifrado(self):
        # Generar llave utilizando LFSR - Linear Feedback Shift Register
        self.crearLlave()
        # Cifrado de desplazamiento
        for i in range(self.n):
            self.textoNumericoProcesado.append((self.texto.textoNumerico[i] + self.llave[i]) % 26)
        
        self.texto.numericoConvertirTexto(self.textoNumericoProcesado)

    
    
    def descifrado(self):
        # Leer llave del fichero, tiene que ser la misma que fue generada al momento de cifrar
        self.leerLlave()
        # Descifrado de desplazamiento
        for i in range(self.n):
            self.textoNumericoProcesado.append((self.texto.textoNumerico[i] - self.llave[i]) % 26)
        
        self.texto.numericoConvertirTexto(self.textoNumericoProcesado)

        
prueba = Flujo(False)