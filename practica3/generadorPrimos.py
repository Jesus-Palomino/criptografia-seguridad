import gmpy2
import os

Primo = 2
listaPrimos = []
listaPrimos.append(Primo)
for p in range(2000):
    Primo = gmpy2.next_prime(Primo)
    listaPrimos.append(Primo)

f =  open(os.getcwd()+"/ficheros/primos.txt", 'w')

for p in listaPrimos:
    f.write(str(p)+' ')