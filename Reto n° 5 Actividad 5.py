
def calcular_promedio(a, b, c, d, e):
    return (a + b + c + d + e) / 5

def promedio_multiplicativo(a, b, c, d, e):
    producto = a * b * c * d * e
    return producto ** (1/5)

# No sabría cómo hacer una función más corta para la buena práctica DRy (don't repeat yourself)
def encontrar_mayor(a, b, c, d, e):
    mayor = a
    if b > mayor:
        mayor = b
    if c > mayor:
        mayor = c
    if d > mayor:
        mayor = d
    if e > mayor:
        mayor = e
    return mayor

def encontrar_menor(a, b, c, d, e):
    menor = a
    if b < menor:
        menor = b
    if c < menor:
        menor = c
    if d < menor:
        menor = d
    if e < menor:
        menor = e
    return menor

def potencia_mayor_al_menor(a, b, c, d, e):
    mayor = encontrar_mayor(a, b, c, d, e)
    menor = encontrar_menor(a, b, c, d, e)
    return mayor ** menor

def raiz_cubica_menor(a, b, c, d, e):
    menor = encontrar_menor(a, b, c, d, e)
    return menor ** (1/3)

if __name__ == "__main__":
    n1 = float(input("Ingrese el número 1: "))
    n2 = float(input("Ingrese el número 2: "))
    n3 = float(input("Ingrese el número 3: "))
    n4 = float(input("Ingrese el número 4: "))
    n5 = float(input("Ingrese el número 5: "))

    promedio:float = calcular_promedio(n1, n2, n3, n4, n5)
    promedio_2: float = promedio_multiplicativo(n1, n2, n3, n4, n5)
    potencia: float = potencia_mayor_al_menor(n1, n2, n3, n4, n5)
    raiz:float = raiz_cubica_menor(n1, n2, n3, n4, n5)

    print("El promedio de los números ingresados: " + str(promedio))
    print("El promedio multiplicativo de los números ingresados es:" + str(promedio_2))
    print("La potencia del mayor elevado al menor de los números ingresados es:" + str(potencia))
    print("La raíz cúbica del menor número de los números ingresados es: " +str(raiz))

