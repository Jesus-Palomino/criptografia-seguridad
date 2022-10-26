import random
import argparse
from textos import Textos

class Flujo:

    texto = None
    llave = []                          #   Llave en forma de texto
    textoNumericoProcesado = []
    n = 0                               #   Longitud de texto
    m = 0                               #   Tamano de espacio del texto (Cardinalidad)
    lenSC = 5                           #   Longitud de secuencia cifrante
    semilla = 0
    lenSemilla = 0


    def __init__(self, mode, m, semilla, input, output):

        self.m = m
        self.semilla = semilla
        self.texto = Textos(input, output)

        self.n = len(self.texto.textoPlano)

        # Generar llave utilizando LFSR (Linear Feedback Shift Register) en base a la semilla dada
        self.crearLlave()

        if(mode):
            self.cifrado()
        else:
            self.descifrado()

        self.texto.imprimirTextos(mode)

    def crearLlave(self):
        random.seed(self.semilla)

        # Caso de logitud de secuencia cifrante mayor a longitud de texto a cifrar
        llave = [int(i) for i in str(self.semilla)]
        self.lenSemilla = len(llave)

        # Generacion de valores random para secuencia cifrante
        funcionLFSR = [random.randint(0,1) for _ in range(self.lenSemilla)]

        num = len(funcionLFSR)
        start = 0

        # Calculo de cada valor restante de la llave
        while (len(llave) < self.n + self.lenSemilla):
            # Calcular suma con modulo m
            value = 0

            for i in range(num):
                value += funcionLFSR[i] * llave[i + start]

            llave.append(value % self.m)
            start += 1

        self.llave = llave[:len(llave) - self.lenSemilla]


    def cifrado(self):
        # Cifrado de desplazamiento
        for i in range(self.n):
            self.textoNumericoProcesado.append((self.texto.textoNumerico[i] + self.llave[i]) % self.m)
        
        self.texto.numericoConvertirTexto(self.textoNumericoProcesado)

    
    def descifrado(self):
        # Descifrado de desplazamiento
        # El valor de la semilla de descifrado tiene que ser el mismo utilizado para el cifrado para un correcto funcionamiento
        for i in range(self.n):
            self.textoNumericoProcesado.append((self.texto.textoNumerico[i] - self.llave[i]) % self.m)
        
        self.texto.numericoConvertirTexto(self.textoNumericoProcesado)




print("\n----------------------\nCIFRADO FLUJO LFSR\n----------------------\npython flujo.py --help  Para obtener ayuda\n")

parser = argparse.ArgumentParser(description='Parse the func action')
parser.add_argument('--mode', dest='mode', nargs='+', default=False,
                        help='indica el modo de ejecucion --mode D para descifrar y --mode C para cifrar')
parser.add_argument('--m', dest='size', nargs='+', default=False,
                        help='indica el tamanio del espacio de texto cifrado')
parser.add_argument('--s', dest='seed', nargs='+', default=False,
                        help='indica la semilla para la generacion de la secuencia de claves cifrante')
parser.add_argument('--i', dest='i', nargs='+', default=False,
                        help='indica el nombre del fichero input')
parser.add_argument('--o', dest='o', nargs='+', default=False,
                        help='indica el nombre del fichero output')
args = parser.parse_args()


if args.mode:
    if args.mode[0] == 'C':
        print("Modo Cifrado\n")
        mode = 1 #Modo cifrar
    else:
        print("Modo Descifrado\n")
        mode = 0 #Modo descifrar

# Cardinalidad del lenguaje
if args.size:
    m = int(args.size[0])

# Semilla para generacion de clave cifrante
if args.seed:
    semilla = args.seed[0]

# Nombre fichero de input
if args.i:
    input = args.i[0]

# Nombre fichero de output
if args.o:
    output = args.o[0]


if not args.mode or not args.size or not args.seed or not args.i or not args.o:
    print("Error en formato de entrada. Ejemplo de formato correcto:\npython flujo.py --mode C --m 26 --s 12345 --i input.txt --o output.txt\n")
    exit(0)



prueba = Flujo(mode, m, semilla, input, output)



