import argparse
import os
import string
from gmpy2 import mpz
from euclides_extendido import inverso_multiplicativo
from fileinput import close

#EJECUCION:
#   python afin.py --mode C --m 26 --a 15 --b hola --i input.txt --o output.txt

abecedario = list(string.ascii_lowercase)
input = "input.txt"
output = "output.txt"

print("-----------\nCIFRADO AFIN\n-----------\npython afin.py --help  Para obtener ayuda\n")

parser = argparse.ArgumentParser(description='Parse the func action')
parser.add_argument('--mode', dest='mode', nargs='+', default=False,
                        help='indica el modo de ejecucion --mode D para descifrar y --mode C para cifrar')
parser.add_argument('--m', dest='size', nargs='+', default=False,
                        help='indica el tamanio del espacio de texto')
parser.add_argument('--a', dest='a', nargs='+', default=False,
                        help='indica el coeficiente multiplicativo')
parser.add_argument('--b', dest='b', nargs='+', default=False,
                        help='indica el termino constante de la funcion')
parser.add_argument('--i', dest='i', nargs='+', default=False,
                        help='indica el nombre del fichero input')
parser.add_argument('--o', dest='o', nargs='+', default=False,
                        help='indica el nombre del fichero output')
args = parser.parse_args()

if args.mode:
    if args.mode[0] == 'C':
        print("Modo Cifrado")
        mode = 0 #Modo cifrar
    else:
        print("Modo Descifrado")
        mode = 1 #Modo descifrar

# n = numero de letras
if args.size:
    size = args.size[0]

# a = coeficiente multiplicato
if args.a:
    a = args.a[0]

# b = constante de desplazamiento
if args.b:
    b = args.b[0]

if args.i:
    input = args.i[0]

if args.o:
    output = args.o[0]

if not args.mode or not a or not b or not args.size:
    print("Error en formato de entrada. Ejemplo de formato correcto:\npython afin.py --mode C --m 26 --a 5 --b clave --i input.txt --o output.txt")
    exit(0)

respuesta, aInverso = inverso_multiplicativo(int(size),int(a))
if aInverso < 0:
    aInverso = int(aInverso) * -1

if respuesta is False:
    print("Clave no valida, por favor, ingresa otra distinta.")
    exit(0)
else:
    print("Clave valida")
# ci = (a*mi + b) mod n

entrada = open(os.getcwd()+"/ficheros/" + input)
caracter = " "


#Cifrado:
if mode == 0:
    caracterNumerico = []
    caractCif = []
    listaAux = []

    #Leo caracter a caracter
    while caracter != "":
        caracter = entrada.readline(1)
        #En caso de que sea letra
        if caracter != " " and caracter != '\n' and caracter != '':
            #anyado a una lista el valor numerico
            caracterNumerico.append(abecedario.index(caracter)+1)
            listaAux.append(caracter)
    entrada.close()
    print("\nTexto en claro:")
    print("".join(listaAux))
    indice = 0

    for i in caracterNumerico:
        #aplico formula
        #Si ha llegado al final de la clave, vuelve al principio
        if indice >= len(b):
            indice = 0
        #Si no, guardo el asci del caracter de la clave
        newB = abecedario.index(b[indice]) + 1
        indice = indice + 1

        cif = (int(a)*int(i) + int(newB)) % int(size)
        #anyado a lista el valor textual
        caractCif.append(abecedario[cif-1])
        

    salida = open(os.getcwd()+"/ficheros/" + output, 'w')
    salida.write("".join(caractCif))
    print("////////////////\nTexto Cifrado:")
    print("".join(caractCif) + "\n")

else:

    caracterNumerico = []
    caractCif = []
    listaAux = []
    while caracter != "":
        caracter = entrada.readline(1)
        if caracter != " " and caracter != '\n' and caracter != '':
            caracterNumerico.append(abecedario.index(caracter)+1)
            listaAux.append(caracter)
    entrada.close()
    print("\nTexto en claro:")
    print("".join(listaAux))
    indice = 0
    for i in caracterNumerico:
        #Si ha llegado al final de la clave, vuelve al principio
        if indice >= len(b):
            indice = 0
        #Si no, guardo el asci del caracter de la clave
        newB = abecedario.index(b[indice]) + 1
        indice = indice + 1
        cif = (int(aInverso)*(int(i) - int(newB))) % int(size)
        caractCif.append(abecedario[cif-1])

    salida = open(os.getcwd()+"/ficheros/" + output, 'w')
    salida.write("".join(caractCif))
    salida.close()
    print("////////////////\nTexto Claro:")
    print("".join(caractCif) + "\n")

