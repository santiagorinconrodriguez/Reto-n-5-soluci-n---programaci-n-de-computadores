import math

def calcular_volumen(r1:float, r2: float, h: float) -> float:
    return (4/3) * math.pi * r1**3 + (1/3) * math.pi * r2**2 * h

def calcular_area_superficial(r1: float, r2: float, h: float) -> float:
    pitagoras = math.sqrt(r2**2 + h**2)  
    return 4 * math.pi * r1**2 + math.pi * r2 * (r2 + pitagoras)


if __name__ == "__main__":
    r1 = float(input("Ingrese el radio de la esfera: "))
    r2 = float(input("Ingrese el radio del cono: "))
    h = float(input("Ingrese la altura del cono: "))

    volumen = calcular_volumen(r1, r2, h)
    area = calcular_area_superficial(r1, r2, h)

    print("El volumen olumen total de la figura es: " + str(volumen))
    print("Rl área superficial total de la figura es: " + str(area))
