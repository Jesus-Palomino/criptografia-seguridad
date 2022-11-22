import random
from operator import concat
import os

sBoxes = []
sbox = []
list2aux = []
listaAux = []
sBoxfile = open(os.getcwd()+"/ficheros/s_boxes.txt")
sboxcont = " "

cntaux = 0
while sboxcont != "":
    sboxcont = sBoxfile.readline(1)
    #En caso de que sea letra
    if cntaux == 1 and sboxcont == '\n':
        cntaux = 0
    else:    
        if sboxcont == 's':
            sBoxes.append(sbox)
            sbox = []
            cntaux = 0
        else:    
            if sboxcont != " " and sboxcont != '\n' and sboxcont != '':
                listaAux.append(sboxcont)
                cntaux = 0
            elif sboxcont == ' ':
                list2aux.append("".join(listaAux))
                listaAux = []
                cntaux = 0

            elif sboxcont == '\n' or sboxcont == '':
                cntaux = 1
                list2aux.append("".join(listaAux))
                sbox.append(list2aux)
                list2aux = []
                listaAux = []
Nrounds = 15000
coincid = 0
print('-----------------------\nEstudio de la no Linealidad de la funcion F\n-----------------------\n')
print('Ejemplo de ejecucion:\nPrimero, damos valores aleatorios A a y b')
for x in range(0,Nrounds):                
    aleat = []
    for i in range(48):
        # randint function to generate
        # 0, 1 randomly and converting
        # the result into str
        temp = str(random.randint(0, 1))
        # Concatenation the random 0, 1
        # to the final result
        aleat.append(temp)

    aleatb = []
    for i in range(48):
        # randint function to generate
        # 0, 1 randomly and converting
        # the result into str
        temp = str(random.randint(0, 1))
        # Concatenation the random 0, 1
        # to the final result
        aleatb.append(temp)

    degubb = 1
    if x == 0:
        print('a = '+ "".join(aleat))
        print('b = ' + "".join(aleatb))
    for i in range(0,16):
        #funcion f
        f = []
        for j in range(0,48):
            suma = (int(aleat[j]) + int(aleatb[j])) % 2
            f.append(str(suma))

        #S-boxes
        Bx = [f[0:6], f[6:12], f[12:18], f[18:24], f[24:30], f[30:36], f[36:42], f[42:48]] 
        b_chain = ''

        for j in range(0,8):
            #Cojo los bits de columna:
            if degubb == 0:
                print(Bx[j])
            col_bits = concat(Bx[j][0], Bx[j][5])
            row_bits = concat(Bx[j][1], Bx[j][2])

            row_bits = concat(row_bits, Bx[j][3])
            row_bits = concat(row_bits, Bx[j][4])
            s = sBoxes[j] 

            ele = s[int(col_bits,2)][int(row_bits,2)]
            binele = bin(int(ele))[2:]
            while len(binele) < 4:
                binele = concat('0',binele)
            b_chain = concat(b_chain,binele)

            
        if degubb == 0:    
            print('----------\nValores B tras aplicar S boxes: ')
            print(b_chain)
    resfaplusb = b_chain
    if x == 0:
        print('Resultado de F ( a + b ) = ' + str(b_chain))


    for i in range(0,16):
        #funcion f
        f = []
        for j in range(0,48):
            suma = (int(aleat[j]) + 0) % 2
            f.append(str(suma))

        #S-boxes
        Bx = [f[0:6], f[6:12], f[12:18], f[18:24], f[24:30], f[30:36], f[36:42], f[42:48]] 
        b_chain = ''

        for j in range(0,8):
            #Cojo los bits de columna:
            if degubb == 0:
                print(Bx[j])
            col_bits = concat(Bx[j][0], Bx[j][5])
            row_bits = concat(Bx[j][1], Bx[j][2])

            row_bits = concat(row_bits, Bx[j][3])
            row_bits = concat(row_bits, Bx[j][4])
            s = sBoxes[j] 

            ele = s[int(col_bits,2)][int(row_bits,2)]
            binele = bin(int(ele))[2:]
            while len(binele) < 4:
                binele = concat('0',binele)
            b_chain = concat(b_chain,binele)

            
        if degubb == 0:    
            print('----------\nValores B tras aplicar S boxes: ')
            print(b_chain)
    resfa = b_chain


    for i in range(0,16):
        #funcion f
        f = []
        for j in range(0,48):
            suma = (int(aleatb[j]) + 0) % 2
            f.append(str(suma))

        #S-boxes
        Bx = [f[0:6], f[6:12], f[12:18], f[18:24], f[24:30], f[30:36], f[36:42], f[42:48]] 
        b_chain = ''

        for j in range(0,8):
            #Cojo los bits de columna:
            if degubb == 0:
                print(Bx[j])
            col_bits = concat(Bx[j][0], Bx[j][5])
            row_bits = concat(Bx[j][1], Bx[j][2])

            row_bits = concat(row_bits, Bx[j][3])
            row_bits = concat(row_bits, Bx[j][4])
            s = sBoxes[j] 

            ele = s[int(col_bits,2)][int(row_bits,2)]
            binele = bin(int(ele))[2:]
            while len(binele) < 4:
                binele = concat('0',binele)
            b_chain = concat(b_chain,binele)

            
        if degubb == 0:    
            print('----------\nValores B tras aplicar S boxes: ')
            print(b_chain)
    resfb = b_chain


    #F(a)+F(b)
    resfab = []
    for j in range(0,32):
        suma = (int(resfa[j]) + int(resfb[j])) % 2
        resfab.append(str(suma))
    if x == 0:
        print('Resultado de F ( a ) + F ( b ) = ' + "".join(resfab))
        print('\nIterando ' +str(Nrounds)+' veces y registrando las coincidencias...')

    if resfab == resfaplusb:
        coincid = coincid +1
print('\n-----Resultados:\n')
print('Tras estudiar '+ str(Nrounds)+ ' valores distintos de a y b, las')
print('veces que se cumple que f(a+b) != f(a) + f(b) es:  ' + str((Nrounds-coincid)))
print('Se ha cumplido un ' + str(((Nrounds-coincid)/Nrounds)*100)+ '% de las veces')