
import argparse
from fileinput import close
import os
import string
from euclides_extendido import inverso_multiplicativo


# Ejemplos uso de gmpy2
# print(mpz('123') + 1)
# print(10 - mpz(1))
# print(gmpy2.is_prime(17))

#EJECUCION:
#   python afin.py --mode C --m 45 --a 15 --b 3 --i input.txt --o output.txt

abecedario = list(string.ascii_lowercase)

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
        print("Has elegido mode: " + args.mode[0])
        mode = 0 #Modo cifrar
    else:
        print("Has elegido mode: " + args.mode[0])
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
    print("Error en formato de entrada. Ejemplo de formato correcto:\npython practica1/afin.py --mode C --m 45 --a 5 --b 3 --i input.txt --o output.txt")
    exit(0)

respuesta, aInverso = inverso_multiplicativo(int(a),int(b))
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
    #Leo caracter a caracter
    while caracter != "":
        caracter = entrada.readline(1)
        #En caso de que sea letra
        if caracter != " " and caracter != '\n' and caracter != '':
            #anyado a una lista el valor numerico
            caracterNumerico.append(abecedario.index(caracter)+1)
    entrada.close()

    for i in caracterNumerico:
        #aplico formula
        cif = (int(a)*int(i) + int(b)) % int(size)
        #anyado a lista el valor textual
        caractCif.append(abecedario[cif-1])

    salida = open(os.getcwd()+"/ficheros/" + output, 'w')
    salida.write("".join(caractCif))

else:

    caracterNumerico = []
    caractCif = []

    while caracter != "":
        caracter = entrada.readline(1)
        if caracter != " " and caracter != '\n' and caracter != '':
            caracterNumerico.append(abecedario.index(caracter)+1)
    entrada.close()


    for i in caracterNumerico:
        cif = (int(aInverso)*(int(i) - int(b))) % int(size)
        caractCif.append(abecedario[cif-1])

    salida = open(os.getcwd()+"/ficheros/" + output, 'w')
    salida.write("".join(caractCif))
    salida.close()
