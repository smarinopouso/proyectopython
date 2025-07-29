Ejercicio 2: ordenar_lista
def ordenar_lista(numeros):
    temp = list(numeros)  # Hacemos una copia para no modificar la original
    n = len(temp)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if temp[j] < temp[min_idx]:
                min_idx = j
        # Intercambiamos el elemento actual con el mínimo encontrado
        temp[i], temp[min_idx] = temp[min_idx], temp[i]

    return temp

Ejercicio 3: vocales_mayusculas

def vocales_mayusculas(texto):
    vocales = "aeiouáéíóú"
    resultado = ""

    for letra in texto:
        if letra.lower() in vocales:
            resultado += letra.upper()
        else:
            resultado += letra

    return resultado



Ejercicio 10: calcular_promedio

def calcular_promedio(lista_numeros):
    if len(lista_numeros) == 0:
        raise ValueError("La lista está vacía, no se puede calcular el promedio.")
    return sum(lista_numeros) / len(lista_numeros)

# Manejo del error al usar la función
try:
    datos = []  # Cambia por datos = [10, 20, 30] para ver un resultado válido
    promedio = calcular_promedio(datos)
    print(f"Promedio: {promedio}")
except ValueError as e:
    print(f"Error al calcular promedio: {e}")



Ejercicio 13: letras_mayus_minus

def letras_mayus_minus(caracteres):
    letras_unicas = sorted(set(caracteres))  # Ordenamos para que el resultado sea consistente
    return [(c.upper(), c.lower()) for c in letras_unicas]


Ejercicio 17: lista_a_numero

from functools import reduce

def lista_a_numero(digitos):
    if not digitos:
        return 0
    return reduce(lambda acc, d: acc * 10 + d, digitos)

Ejercicio 22: producto_total

from functools import reduce

def producto_total(lista):
    return reduce(lambda x, y: x * y, lista, 1)


Ejercicio 23: concatenar_palabras

def concatenar_palabras(lista_palabras):
    return "".join(lista_palabras)
