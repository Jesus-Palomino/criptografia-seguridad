
# Funcion que implementa algoritmo de euclides extendido para calcular el inverso multiplicativo de b mod a 
def euclides_extendido(a, b):
    # Si "a" es 0 MCD = b y detenemos. En caso de que b sea 0, en el siguiente ciclo se detecta.
    if a == 0:
        return b, 0, 1
    # En caso contrario, se repite el ciclo con a = (b mod a) y b = a
    else:
        # mcd = a*x + b*y
        mcd, x, y = euclides_extendido(b % a, a)
        return mcd, y - (b // a) * x, x


# Calcular el inverso multiplicativo de B en mod A
def inverso_multiplicativo(a, b):
    res = euclides_extendido(a, b)
    # Si el mcd es igual a 1 tiene inverso multiplicativo
    # El inverso multiplicativo es igual al valor de y en el resultado dado por la funcion
    if(res[0] == 1):
        return True, res[2]
    else:
        return False, res[2]
