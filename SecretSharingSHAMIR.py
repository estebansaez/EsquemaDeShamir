import random
from sympy import symbols, simplify

def generar_Polinomio(n, constante):
    coeficientes = [random.randint(0, 10000) for _ in range(n-1)]  # Genera n-1 coeficientes aleatorios
    
    terminos = [f"{coeficientes[i]}x^{n-i-1}" for i in range(n-1)]
    polinomio_str = " + ".join(terminos)
    
    polinomio_str += f" + {constante}"  # Agregar el coeficiente constante
    
    return polinomio_str

def evaluarPolinomio(polinomio, x):
    # Separar el polinomio en términos
    terminos = polinomio.split(" + ")
    resultados = []
    for x in x:
        result = 0
        for term in terminos:
            if 'x^' in term:
                coeficiente, power = term.split("x^")  # Separar coeficiente y potencia
                coeficiente = int(coeficiente)
                power = int(power)
                result += coeficiente * (x ** power)  # Calcular el término
            else:
                constante = int(term)
                result += constante  # Sumar el coeficiente constante
        resultados.append(result)
    return resultados

def lagrange_interpolation(points):
    x = symbols('x')
    n = len(points)
    polynomial = 0
    for i in range(n):
        xi, yi = points[i]
        term = yi
        for j in range(n):
            if j != i:
                xj, _ = points[j]
                term *= (x - xj) / (xi - xj)
        polynomial += term
    return simplify(polynomial)

# Ejecucion de creacion del polinomio y evaluacion de puntos

n = 16  # Número mínimo requerido para reconstruir el secreto
constante = 98944675233973  # Coeficiente constante definido (secreto)

print ("El secreto a compartir es: ", constante)
polinomioInicial = generar_Polinomio(n, constante) #crear polinomio de n-1 grados
print("Polinomio generado:", polinomioInicial)

x_value = list(range(1, 31)) # Valor de x para evaluar el polinomio
resultado = evaluarPolinomio(polinomioInicial, x_value)
#print("Resultado de evaluar el polinomio en x =", x_value, ":", resultado)

# Ejecucion de reconstruccion del secreto:

#evaluamos el umbral de puntos necesarios para reconstruir el secreto
puntosaEvaluar = [1,3,5,4,10,11,19,2,6,14,7,8,20,17,24,28,9]
print ("Puntos para reconstruir secreto: ",puntosaEvaluar)
puntos_evaluados = evaluarPolinomio(polinomioInicial, puntosaEvaluar)
points =  list(zip(puntosaEvaluar, puntos_evaluados)) # Lista de tuplas (x, y) para la interpolación de Lagrange
polinomioLagrange = lagrange_interpolation(points)
print("Polinomio interpolante de Lagrange:", polinomioLagrange)
