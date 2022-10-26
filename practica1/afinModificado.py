import argparse
import os
import string
from gmpy2 import mpz
import gmpy2
from euclides_extendido import inverso_multiplicativo
from fileinput import close

#EJECUCION:
#   python afin.py --mode C --m 26 --a 15 --b 3 --i input.txt --o output.txt

abecedario = list(string.ascii_lowercase)
input = "input.txt"
output = "output.txt"

print("-----------\nCIFRADO AFIN MODIFICADO\n-----------\npython afin.py --help  Para obtener ayuda\n")

parser = argparse.ArgumentParser(description='Parse the func action')
parser.add_argument('--mode', dest='mode', nargs='+', default=False,
                        help='indica el modo de ejecucion --mode D para descifrar y --mode C para cifrar')
parser.add_argument('--nbloques', dest='size', nargs='+', default=False,
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
    size = 26**int(args.size[0])
    nBloqs = int(args.size[0])
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
respuesta, aInverso = inverso_multiplicativo(int(a),int(size))


if respuesta is False:
    print("Clave no valida, por favor, ingresa otra distinta.")
    exit(0)
else:
    print("Clave valida")


entrada = open(os.getcwd()+"/ficheros/" + input)
caracter = " "


#Cifrado:
if mode == 0:
    caracterNumerico = []
    caractCif = []
    listaAux = []

    #Leo caracter a caracter
    while caracter != "":
        caracter = entrada.readline(int(nBloqs))
        base = []
        for c in caracter:
            #En caso de que sea letra
            if caracter != " " and caracter != '\n' and caracter != '':
                #anyado a una lista el valor numerico
                
                base.append(abecedario.index(c))
        numNuevaBase = 0
        #CAMBIO DE BASE:
        if len(base) > 0:
            for cB in range(len(base)):
                numCambiado = base[cB] * (26 ** (len(base)-1-cB))
                numNuevaBase = numNuevaBase + numCambiado
        listaAux.append(caracter)
        caracterNumerico.append(numNuevaBase)
    entrada.close()
    print("\nTexto en claro:")
    print("".join(listaAux))
    
    indice = 0
    caracterNumerico.pop()
    for i in caracterNumerico:
        #aplico formula
        cif = (int(a)*int(i) + int(b))
        cif = gmpy2.f_divmod(cif,int(size))[1]
        cuenta = 0
        for i in range(nBloqs-1, -1, -1):
            for j in range(0,25):
                prueba = (26 ** i) * j + cuenta
                pruebaFinal = (26 ** i) * (j-1) + cuenta
                if prueba > cif:
                    cuenta = cuenta + (26**i) * (j-1)
                    #anyado a lista el valor textual
                    caractCif.append(abecedario[j-1])
                    break

    salida = open(os.getcwd()+"/ficheros/" + output, 'w')
    salida.write("".join(caractCif))
    print("////////////////\nTexto Cifrado:")
    print("".join(caractCif) + "\n")


else:
    caracterNumerico = []
    caractCif = []
    listaAux = []
    while caracter != "":
        caracter = entrada.readline(int(nBloqs))
        base = []
        for c in caracter:
            #En caso de que sea letra
            if caracter != " " and caracter != '\n' and caracter != '':
                #anyado a una lista el valor numerico
                base.append(abecedario.index(c))
        numNuevaBase = 0
        #CAMBIO DE BASE:
        if len(base) > 0:
            for cB in range(len(base)):
                numCambiado = base[cB] * (26 ** (len(base)-1-cB))
                numNuevaBase = numNuevaBase + numCambiado
        listaAux.append(caracter)        

        caracterNumerico.append(numNuevaBase)
    entrada.close()
    print("\nTexto en claro:")
    print("".join(listaAux))
    
    indice = 0
    caracterNumerico.pop()

    for i in caracterNumerico:
        #aplico formula
        cif = (int(aInverso)*(int(i) - int(b)))
        cif = gmpy2.f_divmod(cif,int(size))[1]
        cuenta = 0
        for i in range(nBloqs-1, -1, -1):
            for j in range(0,25):
                prueba = (26 ** i) * j + cuenta
                pruebaFinal = (26 ** i) * (j-1) + cuenta
                if prueba > cif:
                    cuenta = cuenta + (26**i) * (j-1)
                    #anyado a lista el valor textual
                    caractCif.append(abecedario[j-1])
                    break
    
    salida = open(os.getcwd()+"/ficheros/" + output, 'w')
    salida.write("".join(caractCif))
    salida.close()
    print("////////////////\nTexto Claro:")
    print("".join(caractCif) + "\n")
