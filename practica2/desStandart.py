import argparse
from curses import KEY_BACKSPACE
from operator import concat
import os
from re import M
import numpy as np
from operator import xor

class des():
    
    def init(mode,Key, Mtext):
        degubb = 1
        listaDespK = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

        
        pc1file = open(os.getcwd()+"/ficheros/pc1.txt")
        pc1cont = " "

        pc2file = open(os.getcwd()+"/ficheros/pc2.txt")
        pc2cont = " "

        ipfile = open(os.getcwd()+"/ficheros/ip.txt")
        ipcont = " "

        expandfile = open(os.getcwd()+"/ficheros/E.txt")
        expandcont = " "

        sBoxfile = open(os.getcwd()+"/ficheros/s_boxes.txt")
        sboxcont = " "

        Pfile = open(os.getcwd()+"/ficheros/P.txt")
        pcont = " "

        ipinvfile = open(os.getcwd()+"/ficheros/ip_inverso.txt")
        ipinvcont = " "


        

        ################################
        #Lectura de Parametros:
        ###############################


        pc1 = []
        pc2 = []
        ip = []
        expand = []
        listaAux = []
        sBoxes = []
        sbox = []
        perm = []
        ip_inverso = []
        
        

        

        #Leo caracter a caracter
        list2aux = []

        while pc1cont != "":
            pc1cont = pc1file.readline(1)
            #En caso de que sea letra
            if pc1cont != " " and pc1cont != '\n' and pc1cont != '':
                listaAux.append(pc1cont)

            elif pc1cont == ' ':
                list2aux.append("".join(listaAux))
                listaAux = []

            elif pc1cont == '\n' or pc1cont == '':
                list2aux.append("".join(listaAux))
                pc1.append(list2aux)
                list2aux = []
                listaAux = []

        while expandcont != "":
            expandcont = expandfile.readline(1)
            #En caso de que sea letra
            if expandcont != " " and expandcont != '\n' and expandcont != '':
                listaAux.append(expandcont)

            elif expandcont == ' ':
                list2aux.append("".join(listaAux))
                listaAux = []

            elif expandcont == '\n' or expandcont == '':
                list2aux.append("".join(listaAux))
                expand.append(list2aux)
                list2aux = []
                listaAux = []

        while pc2cont != "":
            pc2cont = pc2file.readline(1)
            #En caso de que sea letra
            if pc2cont != " " and pc2cont != '\n' and pc2cont != '':
                listaAux.append(pc2cont)

            elif pc2cont == ' ':
                list2aux.append("".join(listaAux))
                listaAux = []

            elif pc2cont == '\n' or pc2cont == '':
                list2aux.append("".join(listaAux))
                pc2.append(list2aux)
                list2aux = []
                listaAux = []

        while ipcont != "":
            ipcont = ipfile.readline(1)
            #En caso de que sea letra
            if ipcont != " " and ipcont != '\n' and ipcont != '':
                listaAux.append(ipcont)

            elif ipcont == ' ':
                list2aux.append("".join(listaAux))
                listaAux = []

            elif ipcont == '\n' or ipcont == '':
                list2aux.append("".join(listaAux))
                ip.append(list2aux)
                list2aux = []
                listaAux = []

        while pcont != "":
            pcont = Pfile.readline(1)
            #En caso de que sea letra
            if pcont != " " and pcont != '\n' and pcont != '':
                listaAux.append(pcont)

            elif pcont == ' ':
                list2aux.append("".join(listaAux))
                listaAux = []

            elif pcont == '\n' or pcont == '':
                list2aux.append("".join(listaAux))
                perm.append(list2aux)
                list2aux = []
                listaAux = []

        while ipinvcont != "":
            ipinvcont = ipinvfile.readline(1)
            #En caso de que sea letra
            if ipinvcont != " " and ipinvcont != '\n' and ipinvcont != '':
                listaAux.append(ipinvcont)

            elif ipinvcont == ' ':
                list2aux.append("".join(listaAux))
                listaAux = []

            elif ipinvcont == '\n' or ipinvcont == '':
                list2aux.append("".join(listaAux))
                ip_inverso.append(list2aux)
                list2aux = []
                listaAux = []

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



            
        if degubb == 0:
            print("\nTexto en claro:")
            print("".join(Mtext))


        LM = Mtext[0:32]
        RM = Mtext[32:]
        if degubb == 0:
            print("---------\nPartimos el texto\nLeft : "+"".join(LM))
            print("Right: "+"".join(RM)+"\n------------")
            print("K: "+ "".join(Key))
        kplus = []
        for fila in pc1:
            for ele in fila:
                kplus.append(Key[int(ele)-1]) 
        if degubb == 0:
            print("K+: "+ "".join(kplus))
        c0 = kplus[0:28]
        d0 = kplus[28:]



        cKeys = []
        cKeys.append(c0)
        dKeys = []
        dKeys.append(d0)
        listc = []
        listc.append("".join(c0))
        listd = []
        listd.append("".join(d0))

        for i in range(0,16):
            c_aux = cKeys[i]
            for j in range(0,listaDespK[i]):
                c_aux = []
                c_aux = cKeys[i]
                ele = c_aux.pop(0)
                c_aux.append(ele)

                d_aux = []
                d_aux = dKeys[i]
                ele = d_aux.pop(0)
                d_aux.append(ele)

            cKeys.append(c_aux)
            listc.append(str("".join(c_aux)))
            dKeys.append(d_aux)
            listd.append(str("".join(d_aux)))
        if degubb == 0:   
            print("\n-----------\nLista claves:\n")
            ind = 0
            for fila in range(0,len(listc)):
                print("C"+ str(ind)+ ": " + str(listc[fila]))
                print("D"+ str(ind)+ ": " + str(listd[fila]) + "\n")
                ind = ind +1 

        kFinals = []

        for i in range(1, 17):
            concatcd =  concat(listc[i], listd[i])
            k_aux = []
            for fila in pc2:
                for ele in fila:
                    k_aux.append(concatcd[int(ele)-1])
            kFinals.append("".join(k_aux))
        if degubb == 0:
            print("\n-----------\nLista claves Finales:\n")
            ind = 1
            for fila in range(0,len(kFinals)):
                print("K"+ str(ind)+ ": " + str(kFinals[fila]) + "\n")
                ind = ind +1 

        ip_b = []
        for fila in ip:
            for ele in fila:
                ip_b.append(Mtext[int(ele)-1])

        ipL = ip_b[:32]
        ipR = ip_b[32:]
        if degubb == 0:
            print("IP: " + "".join(ip_b))
            print("IP L: " + "".join(ipL))
            print("IP R: " + "".join(ipR))
        ipLgen = [ipL]
        ipRgen = [ipR]
        if degubb == 0:
            print('Claves K finales: ')
            print(kFinals[0])
        if mode != 0:
            #Revertimos orden de K's
            kFinals = list(reversed(kFinals))
        for i in range(0,16):
            ipl_aux = ipRgen[i]
            ipLgen.append(ipl_aux)
            #Expando Rn-1
            ipR_expanded = []
            for fila in expand:
                for ele in fila:
                    ipR_expanded.append(ipRgen[i][int(ele)-1])
            #funcion f
            f = []
            for j in range(0,48):
                suma = (int(kFinals[i][j]) + int(ipR_expanded[j])) % 2
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

            #P permutation to S boxes
            b_chainPerm = []
            for fila in perm:
                for ele in fila:
                    b_chainPerm.append(b_chain[int(ele)-1])
            if degubb == 0:
                print('-----------\nF final:')
                print("".join(b_chainPerm))

            ipr_aux = []
            for j in range(0,32):
                suma = (int(ipLgen[i][j]) + int(b_chainPerm[j])) % 2
                ipr_aux.append(str(suma))
            if degubb == 0:
                print('Ronda '+ str(i+1))
                print("".join(ipr_aux))
            ipRgen.append(ipr_aux)

        final = concat(ipRgen[16], ipLgen[16])
        final_permutado = []
        if degubb == 0:
            print('swap final: ')
            print("".join(final))

        for fila in ip_inverso:
            for ele in fila:
                final_permutado.append(final[int(ele)-1])

        if degubb == 0:
            print('Vector Final: ')
            print("".join(final_permutado))
        return final_permutado