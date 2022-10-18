import argparse
from ctypes import sizeof
from fileinput import close
import os
from random import randint
import string
from gmpy2 import mpz
from euclides_extendido import inverso_multiplicativo
from mcd import mcd1
import pandas as pd


#EJECUCION:
#   python afin.py --mode C --m 26 --a 15 --b hola --i input.txt --o output.txt
print("--------------\nCRIPTOANALISIS VIGENERE\n--------------\npython cAnalisisVigenere.py --help  Para obtener ayuda\n")

abecedario = list(string.ascii_lowercase)
diccionarioProb = {}
diccionarioProbEsp = {'a': 0.1196,'b':0.00092,'c':0.0292,'d':0.0687,'e':0.1678,'f':0.0052,'g':0.0073,'h':0.0089,'i':0.0415,'j':0.0030,'k':0,'l':0.0837,'m':0.0212,'n':0.0701,'o':0.0869,'p':0.0277,'q':0.0153,'r':0.0494,'s':0.0788,'t':0.0331,'u':0.0480,'v':0.0039,'w':0,'x':0.0006,'y':0.014,'z':0.0019}
diccionarioProbIng = {'a': 0.084,'b':0.0154,'c':0.0306,'d':0.0399,'e':0.1251,'f':0.0230,'g':0.0196,'h':0.0549,'i':0.0726,'j':0.0016,'k':0.0067,'l':0.0414,'m':0.0253,'n':0.0709,'o':0.0760,'p':0.0200,'q':0.0011,'r':0.0612,'s':0.0654,'t':0.0925,'u':0.0271,'v':0.0099,'w':0.0192,'x':0.0019,'y':0.0173,'z':0.0019}
input = "texto_cifrado.txt"
output = "output.txt"
size = 26

parser = argparse.ArgumentParser(description='Parse the func action')
parser.add_argument('--mode', dest='mode', nargs='+', default=False,
                        help='indica el modo de ejecucion --mode K para Kasiski y --mode IC para Indice de Coincidencia')
parser.add_argument('--n', dest='n', nargs='+', default=False,
                        help='indica el numero de caracteres maximo')
parser.add_argument('--l', dest='l', nargs='+', default=False,
                        help='indica el lenguaje del texto --l esp para espanyol --l eng para ingles')
parser.add_argument('--i', dest='i', nargs='+', default=False,
                        help='indica el nombre del fichero input')
parser.add_argument('--o', dest='o', nargs='+', default=False,
                        help='indica el nombre del fichero output')
args = parser.parse_args()

if args.mode:
    if args.mode[0] == 'K':
        print("Se ha elegido kasiski")
        mode = 0 #Modo Kasiski
    else:
        print("Se ha elegido Índice de Coincidencia")
        mode = 1 #Modo IC
if args.n:
    n = args.n[0]
if args.l:
    lan = args.l[0]
    if lan == 'esp':
        diccionarioProb = diccionarioProbEsp
    else:
        diccionarioProb = diccionarioProbIng
if args.i:
    input = args.i[0]

if args.o:
    output = args.o[0]

entrada = open(os.getcwd()+"/ficheros/" + input)
caracter = " "
cadena = entrada.read()

#Modo kasiski
if mode == 0:
    
    listaLeng = []
    #Hacer la prueba varias veces con textos rand, muchos results y con esos "votacion"
    for i in range(2,int(n)):
        flag = 0
        aleat = 0
        oportunidades = 0
        print("Probando con cadenas de " + str(i) + " Caractres")
        while flag != 1:
            entradaAux = cadena
            distancias = []
            buscador = entradaAux[aleat:(aleat+i)]
            if oportunidades == 0:
                entradaAux = cadena[i:]
            else:
                print("Otra oportunidad")
            contador = entradaAux.count(buscador)
            contadorAjuste = 0

            while contador != 0:
                distancia = 0
                contadorAjuste = contadorAjuste + 1
                contador = entradaAux.count(buscador)
                distancia_index = entradaAux.find(buscador)
                corte2 = distancia_index + i - contadorAjuste
                entradaAux = entradaAux[corte2:]
                if len(distancias) > 0:
                    distancia_index = distancia_index + ult_dist
                ult_dist = distancia_index
                if contador != 0:
                    distancias.append(distancia_index)
                
            if len(distancias) > 0:
                for d in distancias:
                    print("Distancia de la ocurrencia: " + str(d))
            
            oportunidades = oportunidades + 1

            md = mcd1(distancias)
            if md != 1 and md != 0:
                listaLeng.append([md, i])
                flag = 1
            else:
                if oportunidades > 5:
                    flag = 1
                else:
                    aleat = randint(0,len(cadena)-i)
        print("----------")
    for ele in listaLeng:
        print("Con el tamanyo de cadena: "+str(ele[1])+"\nEl tamanio de clave posiblemente sea: " + str(ele[0]))


#Tamanyo de clave por indice de coincidencia
else:
    listaMedias = []
    listaLeng = []
    icAleat = 0.038
    if lan == "es":
        icLan = 0.073
    else:
        icLan = 0.065

    icMed = (icLan + icAleat)/2
    for i in range(1,int(n)):
        numCols = i
        numFilas = round((len(cadena) / i))
        entrada.seek(0)
        matrix = []
        
        for k in range(0,numFilas-1):
            tupla = []
            for p in range(0,i):
                caracter = entrada.readline(1)
                while caracter == " " or caracter == '\n' or caracter == '':
                    caracter = entrada.readline(1)
                    if caracter == '':
                        break
                if caracter != '':
                    caracter = caracter.lower()
                    if caracter.islower() == True:
                        tupla.append(caracter)

            matrix.append(tupla)
        
        media = 0
        #Aplicar Indice de coincidencia con matriz cargada.
        for col in range(0,i):

            lista = []
            for fila in matrix:
                if len(fila) == i:
                    lista.append(fila[col])

            total = 26
            listaUnic = pd.unique(lista)
           

            probTotal = 0
            probSum = 0
            sum = 0
            for ele in listaUnic:
                FrecEle = lista.count(ele)
               
                ftot = FrecEle/len(lista)
                ftot2 = (FrecEle-1)/(len(lista)-1)
                probSum = probSum + ftot * ftot2

            media =  media + probSum

            
        media = media / i
        listaMedias.append([i,media])
        print("para clave de tamanio "+ str(i) + ", el indice de coincidencia medio es: " + "{:.4f}".format(media))
        if media > icMed:
            #listaLeng.append([i,media])
            print("Predice lenguaje para este tamanyo de clave\n-----------")

    listaMedias.sort(key = lambda x: x[1]) 
    tup = listaMedias[len(listaMedias)-1]
    listaLeng.append(tup)
    print("\n-----------------")
    print("el tamanio de clave posiblemente sea: " + str(tup[0]+1) + " Con un I.C = " + "{:.4f}".format(tup[1]))
    print("-----------------\n")


print("\n----------\nIniciando Descifrado de Clave\n---------")
#Calculo de clave por Indice de frecuencia.
for ncol, i in listaLeng:
    print("\nNueva Hipotesis: \n tamanyo de clave = "+ str(ncol))
    #Cargar matriz
    numFilas = round(len(cadena) / ncol)
    entrada.seek(0)
    matrix = []
    
    for k in range(0,numFilas):
        tupla = []
        for p in range(0,ncol):
            caracter = entrada.readline(1)
            while caracter == " " or caracter == '\n' or caracter == '':
                    caracter = entrada.readline(1)
                    if caracter == '':
                        break
            if caracter != '':
                caracter = caracter.lower()
                if caracter.islower() == True:
                    tupla.append(caracter)
        matrix.append(tupla)
    listaGen = []
    #print("Estudiando tamanyo: "+ str(ncol))
    #Aplicar Indice de coincidencia con matriz cargada.
    for col in range(0,ncol):
        #print("Columna: " + str(col))
        listaTuplaProb = []
        lista = []
        for fila in matrix:
            if len(fila) == ncol:
                lista.append(fila[col])
        total = 26
        listaUnic = pd.unique(lista)
        probTotal = 0
        probSum = 0

        #Para cada elemento miro su probabilidad
        for desp in range(0,25):
            probSum = 0
            for ele in listaUnic:
                antele = ele
                #print("antes buscaba: " + ele)
                ele = ord(ele) + desp
                if ele > 122:
                    ele = ele - 26
                if ele < 97:
                    ele = ele + 26
                ele = chr(ele)
                #print("tras desplazarlo: "+ str(desp) + "ahora busco: " + ele)
                FrecEle = lista.count(ele)
                FrecantEle = lista.count(antele)
                ftot = FrecEle/len(lista) #Fracción de la formula
                ftot2 = FrecantEle/len(lista)
                icele = ftot * diccionarioProb.get(antele)
                probSum = probSum + icele  
            listaTuplaProb.append(["{:.4f}".format(probSum), desp])    
        
        listaTuplaProb.sort(key = lambda x: x[0] , reverse=True)
        apuesta = listaTuplaProb[0]
        letra = (97+apuesta[1])
        if letra > 122:
            letra = letra - 26
        listaGen.append(chr(letra))
        print("La letra mas probable para la columna: "+str(col)+" es: " + str(chr(letra)))

    print("Podria ser la clave:\n                          "+ "".join(listaGen) + " ? ")