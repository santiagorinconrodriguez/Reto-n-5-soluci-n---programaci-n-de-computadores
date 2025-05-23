def calcular_prestamo(capital: float, interes: float, meses: int) -> float:
    return capital * (1 + interes) ** meses

if __name__ == "__main__":
    capital = float(input("Ingrese el valor del préstamo (capital inicial): "))
    interes = float(input("Ingrese la tasa de interés mensual (en dicimal no porcentaje): "))
    meses = int(input("Ingrese el número de meses: "))
    
    valor_final = calcular_prestamo(capital, interes, meses)
    print("El valor futuro del préstamo es: " + str(valor_final))
