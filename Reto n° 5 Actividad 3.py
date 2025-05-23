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


