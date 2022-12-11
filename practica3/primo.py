import argparse
import random
from re import M
import numpy as np
from os import sys
import gmpy2
import os
import time
inicio = time.time()



input = "/ficheros/primos.txt"
output = "output.txt"

print("-----------\nGeneracion Primos Miller-Rabin\n-----------\npython3 primos.py --help  Para obtener ayuda\n")

parser = argparse.ArgumentParser(description='Parse the func action')
parser.add_argument('--b', dest='b', nargs='+', default=False,
                        help='indica el numero maximo de bits')
parser.add_argument('--p', dest='p', nargs='+', default=False,
                        help='indica la probabilidad de equivocacion')
parser.add_argument('--o', dest='o', nargs='+', default=False,
                        help='indica el nombre del fichero output')
args = parser.parse_args()

if args.b:
    lenPrimo = int(args.b[0])

if args.p:
    probeq = float(args.p[0])

listaPrimos = []
listaAux = []

f =  open(os.getcwd()+"/ficheros/primos.txt", 'r')
fcont = " "

while fcont != "":
    fcont = f.readline(1)
    #En caso de que sea letra
    if fcont != " " and fcont != '\n' and fcont != '':
        listaAux.append(fcont)
    if fcont == ' ':
        listaPrimos.append("".join(listaAux))
        listaAux = []

#Calculamos el número de veces que tendremos que hacer el test dada la probabilidad
mVeces = 0
probabilidadReal = 1
while probabilidadReal > probeq:
    mVeces+=1
    probabilidadReal = 1 / (1+ ((4**mVeces)/(lenPrimo*np.log(lenPrimo))))


#Generamos numero impar:
candidato = []
#Aseguramos longitud
candidato.append("1")
for i in range(0,lenPrimo-2):
    num = random.randint(0,1)
    candidato.append(str(num))
#Aseguramos que sea impar
candidato.append("1")

num_candidato = int("".join(candidato),2)
flag_encontrado = 0
#print('Numero Candidato: '+ str(num_candidato))

while flag_encontrado != 1:

    flag_test = 0
    flag_compuesto = 0

    #Expresamos p-1 
    num = num_candidato-1
    cont = 0
    resto = 0
    #print('p-1 = '+str(num))

    while gmpy2.f_divmod(num, 2)[1] == 0:
        cont+=1
        num, resto = gmpy2.f_divmod(num, 2)


    # print('exponente K = '+ str(cont) )
    # print('impar m = '+ str(num))

    #print('Comprobando test....')
    for i in range(0,mVeces):
        #vemos si pasa el test mVeces
        if flag_compuesto == 1:
            break
        #1. elegimos numero al azar
        aleat = random.randint(2,num_candidato-1)
        # print('base aleatoria a =' + str(aleat)+'\n')
        # print(str(aleat)+'^'+str(num)+ ' mod '+str(num_candidato))
        res = gmpy2.powmod(int(aleat), int(num), int(num_candidato))

        auxexp = 1
        if res != 1 and res != num_candidato-1:    
            for n in range(0,cont): #Aqui hay que poner t-1 veces
                res = gmpy2.powmod(int(aleat), int(num*(2**auxexp)), int(num_candidato))
                # print(str(aleat)+'^'+str(num*(2**auxexp))+ ' mod '+str(num_candidato))
                # print('= ' + str(res))
                if res == 1:
                    flag_compuesto = 1
                    break
                if res == num_candidato-1:
                    break
                if auxexp==cont and res != num_candidato-1:
                    flag_compuesto=1
                    break
                
                auxexp+=1
    
    if flag_compuesto == 1:
        #cambiamos el número
        flag_nodivPrimo = 1
        while flag_nodivPrimo != 0:
            flag_nodivPrimo = 0
            num_candidato = num_candidato+2
            #Dividimos al candidato por los primeros primos:
            for pc in listaPrimos:
                if gmpy2.f_divmod(num_candidato,int(pc))[1] == 0:
                    flag_nodivPrimo =  1 
                    break 
          
        # print('Resultado: Compuesto')
        # print('\nNumero Candidato: '+ str(num_candidato))
    else:
        flag_encontrado = 1
        fin = time.time()
        print('\n--------------\nEncontado posible primo: '+ str(num_candidato))
        print('Ha pasado el test ' + str(mVeces)+' veces por lo que\ntiene una probabilidad de equivocacion igual a: '+ str(probabilidadReal))
        print('\nResultado GMP: ' + str(gmpy2.is_prime(num_candidato)))
        print('Tiempo Empleado: ' + str(round(fin-inicio, 5))+ ' segundos')
