import random
from operator import concat
import os
import desStandart


keyfile = open(os.getcwd()+"/ficheros/clave.txt")
key = " "

Key = []

#Leo caracter a caracter
while key != "":
    key = keyfile.readline(1)
    #En caso de que sea letra
    if key != " " and key != '\n' and key != '':
        Key.append(key)

#Parto de bloque a cifrar
print('----------------\nEstudio de Criterio de Avalancha en DES\n----------------')
#Genero bloque aleatorio
aleatb = []
for i in range(64):
    # randint function to generate
    # 0, 1 randomly and converting
    # the result into str
    temp = str(random.randint(0, 1))
    # Concatenation the random 0, 1
    # to the final result
    aleatb.append(temp)
print('\n------------\nEstudio variando Bloque\n-----------\nPartiendo del bloque: ' + "".join(aleatb))
print('Estudiamos la probabilidad de obtener cada bit de salida cambiando uno a uno los bits de entrada.')

contadorCambios = []
for i in range(64):
    contadorCambios.append(0)

salidaOriginal = desStandart.des.init(0 ,Key, aleatb)

for bitaCambiar in range(0,64):
    #Cambio un Bit:
    if aleatb[bitaCambiar] == '1':
        aleatb[bitaCambiar] = '0'
    else:
        aleatb[bitaCambiar] = '1'
    #Cifro 
    salida = desStandart.des.init(0 ,Key, aleatb)

    #Comparacion
    for j in range(64):
        if salida[j] == '1':
            contadorCambios[j] += 1

print('Tras cambiar cada uno de los bits de la entrada obtenemos la probablidad general\n')
suma = 0
for c in contadorCambios:
    suma += c/64
suma = suma / len(contadorCambios)

print('Probabilidad de que el bit m sea igual a 1: ' + str(suma*100) + '%')
print('Probabilidad de que el bit m sea igual a 0: ' + str(100-suma*100) + '%')

if suma > 0.45 and suma < 0.55:
    print('\nSe demuestra que al cambiar un único bit de la entrada,\nla probabilidad de obtener cada bit de salida es aprox 1/2 ')




#Variando CLAVE
#Genero bloque aleatorio
aleatb = []
for i in range(64):
    # randint function to generate
    # 0, 1 randomly and converting
    # the result into str
    temp = str(random.randint(0, 1))
    # Concatenation the random 0, 1
    # to the final result
    aleatb.append(temp)

Key = []
for i in range(64):
    # randint function to generate
    # 0, 1 randomly and converting
    # the result into str
    temp = str(random.randint(0, 1))
    # Concatenation the random 0, 1
    # to the final result
    Key.append(temp)
print('\n\n------------\nEstudio variando clave\n-----------\nPartiendo de la clave: ' + "".join(aleatb))
print('Estudiamos la probabilidad de obtener cada bit de salida cambiando uno a uno los bits de entrada.')

contadorCambios = []
for i in range(64):
    contadorCambios.append(0)

salidaOriginal = desStandart.des.init(0 ,Key, aleatb)

for bitaCambiar in range(0,64):
    #Cambio un Bit:
    if Key[bitaCambiar] == '1':
        Key[bitaCambiar] = '0'
    else:
        Key[bitaCambiar] = '1'
    #Cifro 
    salida = desStandart.des.init(0 ,Key, aleatb)

    #Comparacion
    for j in range(64):
        if salida[j] == '1':
            contadorCambios[j] += 1

print('Tras cambiar cada uno de los bits de la entrada obtenemos la probablidad general\n')
suma = 0
for c in contadorCambios:
    suma += c/64
suma = suma / len(contadorCambios)

print('Probabilidad de que el bit m sea igual a 1: ' + str(suma*100) + '%')
print('Probabilidad de que el bit m sea igual a 0: ' + str(100-suma*100) + '%')

if suma > 0.45 and suma < 0.55:
    print('\nSe demuestra que al cambiar un único bit de la entrada,\nla probabilidad de obtener cada bit de salida es aprox 1/2 ')