import math

def area_de_la_figura(a: float, b: float, r:float)->float:
    return (a*b) + 2*(math.pi*r**2)

def perimetro_de_la_figura (a: float, b: float, r:float)->float:
    return (2*a + 2*b) + 2* (2*math.pi*r)

if __name__ == "__main__":
    a = float(input("Ingrese la altura del rectángulo: "))
    b = float(input("Ingrese la base del rectángulo: "))
    r = float(input("Ingrese el radio de los círculos: "))
    area = area_de_la_figura(a,b,r)
    perimetro = perimetro_de_la_figura (a,b,r)
    print ("El área de la figura es "+str(area) + " unidades cuadradas")
    print ("El perímetro de la figura es "+ str(perimetro) + " unidades")


