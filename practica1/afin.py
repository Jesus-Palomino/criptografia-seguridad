
import argparse


# Ejemplos uso de gmpy2
# print(mpz('123') + 1)
# print(10 - mpz(1))
# print(gmpy2.is_prime(17))

#EJECUCION:
#   python afin.py --mode C --m 45 --a 15 --b 3 --i input.txt --o output.txt



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
    print("Has elegido size: " + args.size[0])
    size = args.size[0]

# a = coeficiente multiplicato
if args.a:
    print("Has elegido coef mult: " + args.a[0])
    a = args.a[0]

# b = constante de desplazamiento
if args.b:
    b = args.b[0]

if args.i:
    i = args.i[0]

if args.o:
    o = args.o[0]

# ci = (a*mi + b) mod n



# c = testo cifrado 

# m = texto claro







# 1
# Selector cifrado/descifrado
# cinco valores de entrada

# 2
# Verificar que A y B MCD = 1 usando Euclides Extendido
# Si no lo cumple = mensaje de error

# 3
# Asignar un estandar al parametro   i (fichero entrada)
#                                    o (fichero salida)












