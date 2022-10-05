from math import gcd  

def mcd1(numeros):
    mcd_ = 0
    if len(numeros) < 2:
       return 0
    mcd_ = numeros[0]
    for numero in numeros:
        mcd_ = gcd(mcd_, numero)
    return mcd_