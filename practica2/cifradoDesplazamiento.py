from textos import Textos

class CifradoDesplazamiento:

    texto = None

    textoProcesado = ""         # Texto cifrado o descifrado, depende del modo de uso
    textoProcesado = []         # Representacion numerica de textoProcesado

    n = None                    # Cardinalidad del lenguaje

    def __init__(self, input, output, n = 26):

        self.texto = Textos(input, output)

        self.n = n
    
    def cifrado(self, llave):
        for i in range(len(self.texto.textoNumerico)):
            self.textoProcesado.append((self.texto.textoNumerico[i] + llave[i]) % self.n)

        self.texto.numericoConvertirTexto(self.textoProcesado)


    def descifrado(self, llave):
        for i in range(len(self.texto.textoNumerico)):
            self.textoProcesado.append((self.texto.textoNumerico[i] - llave[i]) % self.n)
        
        self.texto.numericoConvertirTexto(self.textoProcesado)