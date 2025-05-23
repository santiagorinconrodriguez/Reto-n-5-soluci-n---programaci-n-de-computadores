# Solución reto n° 5: funciones

## Nombre : Brayan Santiago Rincón Rodríguez

## Curso: Programación de computadores


A lo largo de este repositorio se le dará solución a todas las actividades planteadas en el reto n°5.

1. Dado la figura de la imagen, desarrolle:
![imagen 1](imagenes/img_1.jpg)

- Una función matemática para calcular el volumen y el área superficial.
- Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.
- Revise como utilizar el valor de pi usando import math y math.pi.
```python
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
```

2. Dado la figura de la imagen, desarrolle:
![imagen 2](imagenes/img_2.jpg)

- Una función matemática para calcular el área y el perimetro.
- Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.
- Revise como utilizar el valor de pi usando import math y math.pi
```python
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
```

3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.
```python
def carne_de_aves(gallinas: int, gallos: int, pollitos: int) -> int:
    peso_gallina = 6
    peso_gallo = 7
    peso_pollito = 1
    total = (gallinas * peso_gallina) + (gallos * peso_gallo) + (pollitos * peso_pollito)
    return total

if __name__ == "__main__":
    gallinas = int(input("Ingrese la cantidad de gallinas: "))
    gallos = int (input("Ingrese la canyidad de gallos: "))
    pollitos = int(input("Ingrese la cantidad de pollitos: "))
    cantidad_de_carne = carne_de_aves(gallinas, gallos, pollitos)
    print("El peso total de la carne de los animales ingresado es: " + str(cantidad_de_carne) + " kilos")
```

4. Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.
```python
def calcular_prestamo(capital: float, interes: float, meses: int) -> float:
    return capital * (1 + interes) ** meses

if __name__ == "__main__":
    capital = float(input("Ingrese el valor del préstamo (capital inicial): "))
    interes = float(input("Ingrese la tasa de interés mensual (en dicimal no porcentaje): "))
    meses = int(input("Ingrese el número de meses: "))
    
    valor_final = calcular_prestamo(capital, interes, meses)
    print("El valor futuro del préstamo es: " + str(valor_final))
```

5. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:

- El promedio
- El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
- La potencia del mayor número elevado al menor número
- La raíz cúbica del menor número
```python
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
```

6. Consultar qué es y cómo funciona pip en python.

pip es el administrador de paquetes de Python. Sirve para instalar, actualizar y eliminar librerías desde el repositorio oficial PyPI.

Algunos comandos básicos:

- pip install paquete : instala un paquete.

- pip uninstall paquete : desinstala.

- pip list : muestra paquetes instalados.

- pip install -r requirements.txt : instala varios desde un archivo.

7. Hacer un listado de módulos populares para python que se puedan instalar com pip y consultar cómo instalarlos.

Algunos de los módulos más populares son:

### numpy
Sirve para cálculos matemáticos y operaciones con matrices.
Instalación:
-  pip install numpy

### pandas
Se usa para análisis y manipulación de datos, especialmente en forma de tablas.
Instalación:
-  pip install pandas

### matplotlib
Permite crear gráficos y visualizaciones.
Instalación:
-  pip install matplotlib

### scikit-learn
Muy usado en inteligencia artificial y machine learning.
Instalación: pip install scikit-learn

### requests
Para hacer peticiones HTTP, útil para consumir APIs.
Instalación:
-  pip install requests

### flask
Un microframework para desarrollar aplicaciones web.
Instalación:
-  pip install flask

### django
Framework completo para aplicaciones web robustas.
Instalación:
-  pip install django

### openpyxl
Sirve para leer y modificar archivos Excel (.xlsx).
Instalación: 
- pip install openpyxl

### beautifulsoup4
Para extraer información de páginas web (web scraping).
Instalación:
-  pip install beautifulsoup4

### pygame
Se usa para crear videojuegos en Python.
Instalación:
-  pip install pygame

