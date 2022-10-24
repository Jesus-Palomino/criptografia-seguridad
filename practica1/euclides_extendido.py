import gmpy2

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

# Funcion que implementa algoritmo de euclides para calcular el MCD entre a y b
def euclides(a, b):
    
    if(a == 0 or b == 0):
        return a + b

    return euclides(b, gmpy2.f_divmod(a,b)[1])


# Calcular el inverso multiplicativo de B en mod A
def inverso_multiplicativo(a, b):
    res = euclides_extendido(a, b)
    # Si el mcd es igual a 1 tiene inverso multiplicativo
    # El inverso multiplicativo es igual al segundo valor regresado por euclides_extendido mod 26
    inv = gmpy2.f_divmod(res[1],26)[1]
    return (res[0] == 1, int(inv))



# a = 15
# m = 26

# print(inverso_multiplicativo(a, m))

# Da 7

