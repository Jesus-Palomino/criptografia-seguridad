import gmpy2
import random
import time
import argparse


def generar_binario(n):
  return format(random.getrandbits(n), '0b')

def binario_a_numero(string_binario):
    return int(string_binario, 2)


# Funcion que implementa algoritmo de euclides extendido para calcular el inverso multiplicativo de b mod a 
def euclides_extendido(a, b):
    # Si "a" es 0 MCD = b y detenemos. En caso de que b sea 0, en el siguiente ciclo se detecta.
    if a == 0:
        return b, 0, 1
    # En caso contrario, se repite el ciclo con a = (b mod a) y b = a
    else:
        # mcd = a*x + b*y
        div = gmpy2.f_divmod(b,a)
        mcd, x, y = euclides_extendido(div[1], a)
        return mcd, y - div[0] * x, x


# Calcular el inverso multiplicativo de B en mod A
def inverso_multiplicativo(a, b):
    res = euclides_extendido(a, b)
    # Si el mcd es igual a 1 tiene inverso multiplicativo
    # El inverso multiplicativo es igual al segundo valor regresado por euclides_extendido mod 26
    inv = gmpy2.f_divmod(res[1],b)[1]
    return (res[0] == 1, int(inv))


# Funcion para calcular los cofactores primos del modulo del RSA
def find_prime_factors(n, d, e):
    #1. expresar ed -1
    m = e * d - 1
    t = 0
    
    while gmpy2.f_divmod(m, 2)[1] == 0:
        t+=1
        m, resto = gmpy2.f_divmod(m, 2)
    
    h=2
    contadorseg = 0
    while h!= 1 and contadorseg<100:
        #2. Elegir un numero aleatorio w, 1 < w < n - 1 
        w = random.randint(2, n - 1)

        #3. Si el mcd(w,n) = h > 1 --> o p = h, o q = h
        h = gmpy2.gcd(w,n)
        contadorseg+=1
    if(h == 1):
        res = gmpy2.powmod(int(w), int(m), int(n))
        auxexp = 1
        resAnterior = 1
        if res != 1 and res != n-1:    
            for i in range(0,t): #Aqui hay que poner t-1 veces
                res = gmpy2.powmod(int(w), int(m*(2**auxexp)), int(n))
                if res == 1:
                    resultadopoq = gmpy2.gcd(n,resAnterior + 1)
                    break
                if res == n-1:
                    resultadopoq = -1
                    break
                if auxexp==t and (res == 1 or res==resAnterior):
                    resultadopoq = gmpy2.gcd(n,resAnterior + 1)
                    break
                if auxexp==t and res == (n-1):
                    resultadopoq = -1
                    break
                resAnterior = res

                auxexp+=1
            if resultadopoq == -1:
                print()    
            else:
                temp = gmpy2.f_div(n, resultadopoq)
                p = max(temp, resultadopoq)
                q = min(temp, resultadopoq)
                print('El resultado de factorizar RSA nos dice que: \nP o Q: '+ str(p)+"\nP o Q: " + str(q) )
        else:
            print("res = 1 o res = n -1. No responde ")
    else:
        print("mcd(w,n) = h > 1. No se puede obtener el resultado")


print("\n----------------------\n FactorizacionRSA \n----------------------\npython factorizacionRSA.py --help  Para obtener ayuda\n")

parser = argparse.ArgumentParser(description='Parse the func action')
parser.add_argument('--mode', dest='mode', nargs='+', default=False,
                        help='indica el modo de ejecucion --mode N para utilizar valores default, --mode R para utilizar valores de p y q aleatoreos de cantidades de bits especificas, --mode P para ingresar propios valores para p y q')
parser.add_argument('--pBits', dest='pBits', nargs='+', default=False,
                        help='indica la cantida de bits a utilizar para p cuando se usa --mode R')
parser.add_argument('--qBits', dest='qBits', nargs='+', default=False,
                        help='indica la cantida de bits a utilizar para q cuando se usa --mode R')
parser.add_argument('--p', dest='p', nargs='+', default=False,
                        help='indica el valor de p a utilizar cuando se usa --mode P ')                   
parser.add_argument('--q', dest='q', nargs='+', default=False,
                        help='indica el valor de q a utilizar cuando se usa --mode P ')
parser.add_argument('--e', dest='e', nargs='+', default=False,
                        help='indica el valor de e a utilizar cuando se usa --mode P ')
args = parser.parse_args()


if args.mode:

    flag = False
    if args.mode[0] == 'N':
        print("Factorizacion RSA con valores default\n")
        p = 32317006071311007300714876688669951960444102669715484032130345427524655138867890893197201411522913463688717960921898019494119559150490921095088152386448283120630877367300996091750197750389652106796057638384067568276792218642619756161838094338476170470581645852036305042887575891541065808607552399123930385521914333389668342420684974786564569494856176035326322058077805659331026192708460314150258592864177116725943603718461857357598351152301645904403697613233287231227125684710820209725157101726931323469678542580656697935045997268352998638215525166389647960126939249806625440700685819469589938384356951833568218188663
        q = 32317006071311007300714876688669951960444102669715484032130345427524655138867890893197201411522913463688717960921898019494119559150490921095088152386448283120630877367300996091750197750389652106796057638384067568276792218642619756161838094338476170470581645852036305042887575891541065808607552399123930385521914333389668342420684974786564569494856176035326322058077805659331026192708460314150258592864177116725943603718461857357598351152334063994785580370721665417662212881203104945914551140008147396357886767669820042828793708588252247031092071155540224751031064253209884099238184688246467489498721336450133889385773
        
    elif args.mode[0] == 'R':
        print("Factorizacion RSA con valores aleatorios de p y q de cantidades de bits especificadas\n")
        if not args.pBits or not args.qBits:
            print("Error en formato de entrada. Ejemplo de formato correcto para --mode R:\npython factorizacionRSA.py --mode R --pBits 1024 --qBits 1024\n")
            exit(0)
        else:
            p = gmpy2.next_prime(binario_a_numero(generar_binario(int(args.pBits[0]))))
            q = gmpy2.next_prime(binario_a_numero(generar_binario(int(args.qBits[0]))))
        
    else:
        print("Factorizacion RSA con propios valores\n")
        if not args.p or not args.q or not args.e:
            print("Error en formato de entrada. Ejemplo de formato correcto para --mode P:\npython factorizacionRSA.py --mode P --p 5 --q 7 --e 5 \n")
            exit(0)
        else:
            p = int(args.p[0])
            q = int(args.q[0])
            e = int(args.e[0])
            flag = True
    

    n = gmpy2.mul(p, q)
    print("Cantidad de bits de p:", len(bin(p)[2:]))
    print("Cantidad de bits de q:", len(bin(q)[2:]))
    print("Cantidad de bits de n:", len(bin(n)[2:]))

    print("p: ", p)
    print("q: ", q)
    print("n: ", n)

    # Calcular φ(n) = (p-1) * (q-1)
    phi = (p-1) * (q-1)

    # Elegir un valor para e relativamente primo a to φ(n)
    if(not flag):
        e = 3
        while(not inverso_multiplicativo(e,phi)[0]):
            e += 1

    print("e: ", e)

    # Calcular el exponente de decifrado d, el cual es el inveros multiplicativo de e y φ(n)
    d = inverso_multiplicativo(e, phi)
    print("d: ", d)

    if(d[0]):
        d = d[1]
        inicio = time.time()
        find_prime_factors(n,d,e)
        final = time.time()

    print("Timepo de ejecucion: ", final - inicio)

if not args.mode:
    print("Error en formato de entrada. Ejemplo de formato correcto para factorizacion del modulo RSA con valores defualt:\npython factorizacionRSA.py --mode N\n")
    exit(0)










