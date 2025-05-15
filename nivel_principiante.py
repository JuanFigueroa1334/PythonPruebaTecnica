
from collections import Counter
def numero_mas_frecuente(lista):
    cont = Counter(lista)
    rep = max(cont.values())
    num_repetidos = [num for num, freq in cont.items() if freq == rep]

    # Devuelve
    return min(num_repetidos)
    lista 
lista_numeros = [4, 2, 3, 8, 7, 4, 2, 3, 3]
resultado = numero_mas_frecuente(lista_numeros)
print(f"El número que más se repite es: {resultado}")