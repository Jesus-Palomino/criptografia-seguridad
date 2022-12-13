import gmpy2
from gmpy2 import mpz
import random
import time
import argparse


def generar_binario(n):
  return format(random.getrandbits(n), '0b')

def binario_a_numero(string_binario):
    return int(string_binario, 2)


def exponenciacion_binaria(base, potencia, mod):
    r = mpz(1)
    while potencia > 0:
        if potencia % 2 == 1:
            r = r * base % mod
        base = base * base
        potencia = potencia // 2

    return r


def potencia(base, exponente, mod) -> int:
    result = 1
    while exponente > 0:
        # Si el exponente es impar se multiplica el resultado por la base
        if exponente % 2 == 1:
            result = result * base % mod
        
        # Elevar la base al cuadrado
        base = base * base
        
        # Dividir el exponente
        exponente = exponente // 2
    
    return result


def potenciacion(a = 278909403292135818483710081258118101459943237778710937312118218105710907593179653806810871625455354304620272931575737814, b = 12311695, m = 26):
    a = mpz(a)
    b = mpz(b)
    print("Base:\n", a)
    print("Potencia:\n", b)
    print("Modulo: \n", m)
    print("Cantidad de bits de la base: ", a.bit_length())
    print("Cantidad de bits de la potencia: ", b.bit_length())
    print("Cantidad de bits del modulo: ", m.bit_length())

    print("Resultados:")

    start1 = time.time()
    print("Exponenciacion binaria: ", exponenciacion_binaria(a, b, m))
    start2 = time.time()
    print("Cuadrado y multiplicacion: ", potencia(a,b, m))
    start3 = time.time()
    print("GMP: ", gmpy2.powmod(a, b, m))
    end = time.time()

    print("Tiempo de ejecucion en segundos:")
    print("Exponenciacion binaria: ", start2 - start1)
    print("Cuadrado y multiplicacion: ", start3 - start2)
    print("GMP: ", end - start3)




print("\n----------------------\n Potenciacion de grandes numeros\n----------------------\npython potenciacion.py --help  Para obtener ayuda\n")

parser = argparse.ArgumentParser(description='Parse the func action')
parser.add_argument('--mode', dest='mode', nargs='+', default=False,
                        help='indica el modo de ejecucion --mode N para utilizar valores default, --mode R para utilizar valores aleatoreos de cierta cantidad de bits con mod 26, --mode P para ingresar propios valores')
parser.add_argument('--baseBits', dest='baseBits', nargs='+', default=False,
                        help='indica la cantida de bits a utilizar en la base cuando se usa --mode R')
parser.add_argument('--exponenteBits', dest='exponenteBits', nargs='+', default=False,
                        help='indica la cantida de bits a utilizar en el exponente cuando se usa --mode R')
parser.add_argument('--base', dest='base', nargs='+', default=False,
                        help='indica la base a utilizar cuando se usa --mode P ')                   
parser.add_argument('--exponente', dest='exponente', nargs='+', default=False,
                        help='indica el exponente a utilizar cuando se usa --mode P')
parser.add_argument('--modulo', dest='modulo', nargs='+', default=False,
                        help='indica el modulo a utilizar cuando se usa --mode P')
args = parser.parse_args()


if args.mode:
    if args.mode[0] == 'N':
        print("Exponenciacion con valores default\n")
        potenciacion()
        
    elif args.mode[0] == 'R':
        print("Exponenciacion con valores aleatorios\n")
        if args.baseBits:
            x = binario_a_numero(generar_binario(int(args.baseBits[0])))
        if args.exponenteBits:
            y = binario_a_numero(generar_binario(int(args.exponenteBits[0])))
        if not args.baseBits or not args.exponenteBits:
            print("Error en formato de entrada. Ejemplo de formato correcto para --mode R:\npython potenciacion.py --mode R --baseBits 4000 --exponenteBits 25\n")
            exit(0)
        potenciacion(x, y, 26)
        
    else:
        print("Exponenciacion con propios valores\n")
        if not args.base or not args.exponente or not args.modulo:
            print("Error en formato de entrada. Ejemplo de formato correcto para --mode P:\npython potenciacion.py --mode P --base 8623781942 --exponente 1247187 --modulo 26\n")
            exit(0)
        potenciacion(args.base[0], args.exponente[0], args.modulo[0])


if not args.mode:
    print("Error en formato de entrada. Ejemplo de formato correcto para exponenciacion con valores default:\npython potenciacion.py --mode N\n")
    exit(0)