# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario 
# con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def contar_frecuencias(cadena):
    frecuencias = {}  # Creamos un diccionario vacío para guardar las frecuencias
    for letra in cadena:
        if letra != " ":  # Ignoramos los espacios
            if letra in frecuencias:
                frecuencias[letra] += 1  # Si la letra ya está en el diccionario, sumamos 1
            else:
                frecuencias[letra] = 1  # Si no está, la añadimos con valor 1
    return frecuencias

# 2. Escribe una función que reciba una lista de números y devuelva una nueva lista con los números
# ordenados de menor a mayor, pero sin usar la función sort() ni sorted().

def ordenar_lista(numeros):
    lista_ordenada = []  # Lista vacía donde iremos poniendo los números ordenados
    while numeros:  # Mientras la lista original no esté vacía
        minimo = numeros[0]  # Suponemos que el primer número es el mínimo
        for num in numeros:
            if num < minimo:
                minimo = num  # Encontramos el número más pequeño en la lista
        lista_ordenada.append(minimo)  # Añadimos el mínimo a la lista ordenada
        numeros.remove(minimo)  # Quitamos el mínimo de la lista original para no repetirlo
    return lista_ordenada

# 3. Escribe una función que reciba una cadena de texto y devuelva la misma cadena pero con las vocales en mayúsculas.

def vocales_mayusculas(texto):
    resultado = ""  # Cadena vacía donde iremos guardando el resultado
    vocales = "aeiou"  # Definimos las vocales minúsculas para comparar
    for letra in texto:  # Recorremos cada letra del texto
        if letra in vocales:  # Si la letra es una vocal minúscula
            resultado += letra.upper()  # Convertimos la vocal a mayúscula y la añadimos
        else:
            resultado += letra  # Si no es vocal, la añadimos tal cual
    return resultado

# 4. Escribe una función que reciba una lista de números y devuelva una lista con los números pares de la lista original.

def filtrar_pares(lista):
    resultado = []  # Creamos una lista vacía para guardar los números pares
    for numero in lista:  # Recorremos cada número de la lista original
        if numero % 2 == 0:  # Comprobamos si el número es par (resto de la división entre 2 es 0)
            resultado.append(numero)  # Si es par, lo añadimos a la lista resultado
    return resultado

# 5. Escribe una función que reciba una lista de números y devuelva la suma de todos los números.

def sumar_lista(lista):
    suma = 0  # Empezamos con una suma en 0
    for numero in lista:  # Recorremos cada número de la lista
        suma += numero  # Sumamos el número actual a la suma total
    return suma

# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n):
    if n == 0 or n == 1:
        return 1  # Caso base: el factorial de 0 o 1 es 1
    else:
        return n * factorial(n - 1)  # Llamada recursiva: n * factorial del número anterior
    
# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def tuplas_a_strings(lista_tuplas):
    # Usamos map para aplicar la función str a cada tupla en la lista
    return list(map(str, lista_tuplas))

# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. 
# Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada.
# Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.

def division_segura():
    try:
        numerador = float(input("Introduce el numerador: "))
        denominador = float(input("Introduce el denominador: "))
        resultado = numerador / denominador
    except ValueError:
        print("Error: Debes introducir un número válido.")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    else:
        print(f"La división fue exitosa. El resultado es: {resultado}")

# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
# excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
# "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter()

def filtrar_mascotas(mascotas):
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    # La función filter recibe una función y una lista.
    # Aquí usamos una función lambda que devuelve True si la mascota no está en la lista de prohibidas.
    mascotas_permitidas = filter(lambda mascota: mascota not in mascotas_prohibidas, mascotas)
    # filter devuelve un objeto iterable, convertimos a lista para devolverlo.
    return list(mascotas_permitidas)

# 10. Escribe una función que reciba una lista de números y calcule su promedio.
# Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

def calcular_promedio(lista_numeros):
    if len(lista_numeros) == 0:
        # Lanzamos una excepción personalizada si la lista está vacía
        raise ValueError("La lista está vacía, no se puede calcular el promedio.")
    suma = sum(lista_numeros)  # sum() suma todos los números de la lista
    promedio = suma / len(lista_numeros)  # Dividimos la suma entre la cantidad de números
    return promedio

# 11. Escribe un programa que pida al usuario que introduzca su edad.
# Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado
# (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

def pedir_edad():
    try:
        edad = int(input("Introduce tu edad: "))  # Convertimos la entrada a entero
        if edad < 0 or edad > 120:
            # Si la edad está fuera del rango válido, lanzamos un error
            raise ValueError("La edad debe estar entre 0 y 120.")
        print(f"Tu edad es {edad} años.")
    except ValueError as e:
        # Capturamos el error y mostramos un mensaje adecuado
        print(f"Error: {e}. Por favor, introduce un número válido entre 0 y 120.")

pedir_edad()


# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra.
# Usa la función map()

def longitudes_palabras(frase):
    palabras = frase.split()  # Dividimos la frase en palabras usando espacios
    # Aplicamos map para obtener la longitud de cada palabra
    longitudes = list(map(len, palabras))
    return longitudes


# 13. Genera una función la cual, para un conjunto de caracteres,
# devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas.
# Las letras no pueden estar repetidas. Usa la función map()

def letras_mayus_minus(caracteres):
    # Quitamos caracteres repetidos convirtiendo a conjunto (set)
    letras_unicas = set(caracteres)
    # Para cada letra, creamos una tupla (mayúscula, minúscula) usando map
    resultado = list(map(lambda c: (c.upper(), c.lower()), letras_unicas))
    return resultado

# 14. Crea una función que retorne las palabras de una lista de palabras
# que comiencen con una letra específica. Usa la función filter()

def palabras_con_letra(palabras, letra):
    # Usamos filter para seleccionar solo las palabras que empiezan con la letra dada
    resultado = list(filter(lambda palabra: palabra.startswith(letra), palabras))
    return resultado

# 15. Crea una función lambda que sume 3 a cada número de una lista dada.

def sumar_tres(lista):
    # Usamos map con una función lambda que suma 3 a cada elemento de la lista
    return list(map(lambda x: x + 3, lista))

# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros 
# y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().

def palabras_mas_largas(texto, n):
    # Separamos el texto en palabras usando split()
    palabras = texto.split()
    # Usamos filter para seleccionar solo las palabras con longitud mayor que n
    resultado = list(filter(lambda palabra: len(palabra) > n, palabras))
    return resultado

# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente.
# Por ejemplo, [5,7,2] corresponde al número 572.
# Usa la función reduce().

from functools import reduce

def lista_a_numero(digitos):
    # reduce aplica una función acumuladora que multiplica el acumulador por 10 y suma el siguiente dígito
    return reduce(lambda acumulador, digito: acumulador * 10 + digito, digitos)

# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
# (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90.
# Usa la función filter().

def estudiantes_destacados(estudiantes):
    # Usamos filter para quedarnos solo con estudiantes cuya calificación es >= 90
    return list(filter(lambda estudiante: estudiante['calificacion'] >= 90, estudiantes))

# 19. Crea una función lambda que filtre los números impares de una lista dada.

# Definimos la función lambda que usa filter para quedarnos solo con números impares
filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))

# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int.
# Usa la función filter()

def filtrar_enteros(lista):
    # filter mantiene solo los elementos para los que la función devuelve True
    return list(filter(lambda x: isinstance(x, int), lista))

# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda

def cubo(numero):
    # Función lambda que eleva al cubo el número recibido
    calcular_cubo = lambda x: x ** 3
    return calcular_cubo(numero)

# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce().

def producto_total(lista):
    # reduce aplica una función que multiplica dos elementos, recorriendo toda la lista
    return reduce(lambda x, y: x * y, lista)
# 23. Concatena una lista de palabras. Usa la función reduce().

def concatenar_palabras(lista_palabras):
    # reduce va juntando las palabras de dos en dos hasta formar una cadena completa
    return reduce(lambda x, y: x + y, lista_palabras)

# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().

from functools import reduce

def diferencia_total(lista):
    # La función reduce va restando los elementos de la lista uno a uno,
    # empezando desde el primer elemento
    return reduce(lambda x, y: x - y, lista)

# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres(cadena):
    return len(cadena)

# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

resto = lambda a, b: a % b

# 27. Crea una función que calcule el promedio de una lista de números

def promedio(lista):
    if len(lista) == 0:
        return 0  # Evitamos división por cero si la lista está vacía
    suma = sum(lista)  # sum() suma todos los elementos de la lista
    cantidad = len(lista)  # len() obtiene la cantidad de elementos en la lista
    return suma / cantidad  # Calculamos el promedio dividiendo suma entre cantidad

# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada

def primer_duplicado(lista):
    vistos = set()  # Creamos un conjunto para guardar los elementos que ya hemos visto
    for elemento in lista:  # Recorremos cada elemento de la lista
        if elemento in vistos:  # Si el elemento ya está en el conjunto, es el primer duplicado
            return elemento  # Devolvemos ese elemento
        vistos.add(elemento)  # Si no está, lo añadimos al conjunto para futuras comprobaciones
    return None  # Si no hay duplicados, devolvemos None (nada)


# 29. Crea una función que convierta una variable en una cadena de texto
# y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.

def enmascarar_variable(valor):
    texto = str(valor)  # Convertimos el valor a cadena de texto
    longitud = len(texto)  # Obtenemos la longitud del texto
    if longitud <= 4:
        return texto  # Si la longitud es 4 o menos, no enmascaramos nada
    # Reemplazamos todos los caracteres menos los últimos 4 por '#'
    enmascarado = '#' * (longitud - 4) + texto[-4:]
    return enmascarado


# 30. Crea una función que determine si dos palabras son anagramas,
# es decir, si están formadas por las mismas letras pero en diferente orden.

def son_anagramas(palabra1, palabra2):
    # Convertimos ambas palabras a minúsculas para evitar diferencias por mayúsculas/minúsculas
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    
    # Comparamos si al ordenar las letras de ambas palabras, son iguales
    return sorted(palabra1) == sorted(palabra2)

# 31. Crea una función que solicite al usuario ingresar una lista de nombres
# y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista,
# se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

def buscar_nombre():
    # Pedimos al usuario que ingrese nombres separados por comas
    entrada = input("Introduce una lista de nombres separados por comas: ")
    # Convertimos la cadena en una lista de nombres, eliminando espacios extras
    lista_nombres = [nombre.strip() for nombre in entrada.split(",")]
    
    # Pedimos un nombre para buscar
    nombre_buscar = input("Introduce el nombre a buscar: ").strip()
    
    # Comprobamos si el nombre está en la lista
    if nombre_buscar in lista_nombres:
        print(f"El nombre '{nombre_buscar}' fue encontrado en la lista.")
    else:
        # Si no está, lanzamos una excepción personalizada
        raise ValueError(f"El nombre '{nombre_buscar}' NO se encontró en la lista.")

# Para usar la función simplemente llama a buscar_nombre()

# 32. Crea una función que tome un nombre completo y una lista de empleados,
# busque el nombre completo en la lista y devuelva el puesto del empleado si está en la lista,
# de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def buscar_puesto(nombre_completo, lista_empleados):
    # lista_empleados es una lista de diccionarios, cada uno con 'nombre' y 'puesto'
    for empleado in lista_empleados:
        if empleado['nombre'] == nombre_completo:
            return empleado['puesto']  # Devolvemos el puesto si encontramos el nombre
    return "La persona no trabaja aquí."  # Si no se encuentra, devolvemos este mensaje

# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

sumar_listas = lambda lista1, lista2: [a + b for a, b in zip(lista1, lista2)]

# 34. Crea la clase Arbol, define un árbol genérico con un tronco y ramas como atributos.
# Los métodos disponibles son: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama e info_arbol.

class Arbol:
    def __init__(self):
        # Inicializar un árbol con un tronco de longitud 1 y lista vacía de ramas
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        # Aumentar la longitud del tronco en 1
        self.tronco += 1

    def nueva_rama(self):
        # Agregar una nueva rama de longitud 1 a la lista de ramas
        self.ramas.append(1)

    def crecer_ramas(self):
        # Aumentar la longitud de todas las ramas en 1
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        # Quitar una rama en la posición especificada (posiciones empiezan en 0)
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print("Posición inválida para quitar rama")

    def info_arbol(self):
        # Devolver información sobre el tronco, número de ramas y longitudes de las mismas
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }

# Caso de uso:

arbol = Arbol()        # 1. Crear un árbol
arbol.crecer_tronco()  # 2. Hacer crecer el tronco una unidad
arbol.nueva_rama()     # 3. Añadir una nueva rama
arbol.crecer_ramas()   # 4. Hacer crecer todas las ramas una unidad
arbol.nueva_rama()     # 5. Añadir dos nuevas ramas
arbol.nueva_rama()
arbol.quitar_rama(2)   # 6. Retirar la rama en la posición 2
info = arbol.info_arbol()  # 7. Obtener información sobre el árbol

print(info)

# 36. Clase UsuarioBanco que representa a un usuario de banco con nombre, saldo y cuenta corriente.

class UsuarioBanco:
    def __init__(self, nombre, saldo, tiene_cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.tiene_cuenta_corriente = tiene_cuenta_corriente

    def retirar_dinero(self, cantidad):
        # Retirar dinero del saldo si hay suficiente saldo o si tiene cuenta corriente
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")
        if self.saldo >= cantidad:
            self.saldo -= cantidad
        else:
            # Si no hay saldo suficiente y no tiene cuenta corriente, error
            if not self.tiene_cuenta_corriente:
                raise ValueError(f"{self.nombre} no tiene suficiente saldo ni cuenta corriente para retirar {cantidad}.")
            else:
                # Si tiene cuenta corriente, permitir saldo negativo
                self.saldo -= cantidad

    def transferir_dinero(self, desde_usuario, cantidad):
        # Transferencia desde otro usuario al actual
        if cantidad <= 0:
            raise ValueError("La cantidad a transferir debe ser positiva.")
        # El usuario desde_usuario intenta retirar la cantidad
        try:
            desde_usuario.retirar_dinero(cantidad)
        except ValueError as e:
            raise ValueError(f"Transferencia fallida: {e}")
        # Si no hay error, agregar la cantidad al saldo del usuario actual
        self.saldo += cantidad

    def agregar_dinero(self, cantidad):
        # Agrega dinero al saldo, cantidad debe ser positiva
        if cantidad <= 0:
            raise ValueError("La cantidad a agregar debe ser positiva.")
        self.saldo += cantidad

# Caso de uso:

alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

bob.agregar_dinero(20)             # Bob agrega 20 unidades de saldo
alicia.transferir_dinero(bob, 80) # Transferencia de 80 unidades de Bob a Alicia
alicia.retirar_dinero(50)          # Alicia retira 50 unidades

print(f"Alicia tiene saldo: {alicia.saldo}")  # Debería ser 150 (100 + 80 - 50)
print(f"Bob tiene saldo: {bob.saldo}")        # Debería ser -10 (50 + 20 - 80)

# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras,
# reemplazar_palabras, eliminar_palabra. Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
# de la función procesar_texto.
#
# Código a seguir:
# 1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene
# que devolver un diccionario.
# 2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva. Tiene
# que devolver el texto con el remplazo de palabras.
# 3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra
# eliminada.
# 4. Crear la función procesar_texto que tome un texto, una opción (entre "contar", "reemplazar", "eliminar") y un
# número de argumentos variable según la opción indicada.
#
# Caso de uso:
# Comprueba el funcionamiento completo de la función procesar_texto

def contar_palabras(texto):
    """
    Cuenta la cantidad de veces que aparece cada palabra en el texto.
    Devuelve un diccionario {palabra: cantidad}.
    """
    # Convertimos el texto a minúsculas y lo separamos en palabras
    palabras = texto.lower().split()
    contador = {}
    # Contamos cada palabra
    for palabra in palabras:
        contador[palabra] = contador.get(palabra, 0) + 1
    return contador

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """
    Reemplaza todas las apariciones de palabra_original por palabra_nueva en el texto.
    Devuelve el texto modificado.
    """
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra):
    """
    Elimina todas las apariciones de una palabra en el texto.
    Devuelve el texto modificado.
    """
    # Dividimos el texto en palabras
    palabras = texto.split()
    # Filtramos todas las palabras que no sean la palabra a eliminar
    palabras_filtradas = [p for p in palabras if p != palabra]
    # Unimos las palabras filtradas con espacios
    return " ".join(palabras_filtradas)

def procesar_texto(texto, opcion, *args):
    """
    Función que procesa el texto según la opción dada:
    - "contar": cuenta las palabras (no necesita args)
    - "reemplazar": reemplaza palabra_original por palabra_nueva (args: palabra_original, palabra_nueva)
    - "eliminar": elimina una palabra (args: palabra)
    """
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Para 'reemplazar' se requieren dos argumentos: palabra_original y palabra_nueva.")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("Para 'eliminar' se requiere un argumento: palabra a eliminar.")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción no válida. Usa 'contar', 'reemplazar' o 'eliminar'.")

# Caso de uso:
texto_ejemplo = "Hola mundo mundo esto es un ejemplo de texto de prueba prueba prueba."

print("Contar palabras:")
print(procesar_texto(texto_ejemplo, "contar"))

print("\nReemplazar palabra 'prueba' por 'test':")
print(procesar_texto(texto_ejemplo, "reemplazar", "prueba", "test"))

print("\nEliminar palabra 'mundo':")
print(procesar_texto(texto_ejemplo, "eliminar", "mundo"))

# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

def determinar_momento_del_dia(hora):
    """
    Determina si es de noche, día o tarde según la hora.
    Se considera:
    - Noche: de 0 a 5 (inclusive) y de 21 a 23 (inclusive)
    - Día: de 6 a 12 (inclusive)
    - Tarde: de 13 a 20 (inclusive)
    
    Parámetro:
    hora: entero de 0 a 23
    
    Devuelve un string con el momento del día.
    """
    if not (0 <= hora <= 23):
        return "Hora inválida, debe estar entre 0 y 23."
    
    if 0 <= hora <= 5 or 21 <= hora <= 23:
        return "Es de noche."
    elif 6 <= hora <= 12:
        return "Es de día."
    else:
        return "Es de tarde."

# Programa principal
try:
    entrada = int(input("Introduce la hora actual (0-23): "))
    resultado = determinar_momento_del_dia(entrada)
    print(resultado)
except ValueError:
    print("Por favor, introduce un número entero válido para la hora.")

  # 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
# Las reglas de calificación son:
# - 0 - 69 insuficiente
# - 70 - 79 bien
# - 80 - 89 muy bien
# - 90 - 100 excelente

def calificacion_texto(nota):
    if 0 <= nota <= 69:
        return "insuficiente"
    elif 70 <= nota <= 79:
        return "bien"
    elif 80 <= nota <= 89:
        return "muy bien"
    elif 90 <= nota <= 100:
        return "excelente"
    else:
        return "Nota inválida"

# Ejemplo de uso
# print(calificacion_texto(85))  # Debería imprimir "muy bien"


# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo")
# y datos (una tupla con los datos necesarios para calcular el área de la figura).

import math

def calcular_area(figura, datos):
    if figura == "rectangulo":
        # datos = (base, altura)
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        # datos = (radio,)
        (radio,) = datos
        return math.pi * radio ** 2
    elif figura == "triangulo":
        # datos = (base, altura)
        base, altura = datos
        return (base * altura) / 2
    else:
        return "Figura no reconocida"

# Ejemplo de uso:
# print(calcular_area("rectangulo", (5, 3)))  # 15
# print(calcular_area("circulo", (4,)))       # 50.26548245743669
# print(calcular_area("triangulo", (6, 2)))   # 6

# 41. Programa para calcular el precio final de una compra con posible descuento

def calcular_precio_final():
    try:
        precio_original = float(input("Introduce el precio original del artículo: "))
        if precio_original < 0:
            print("El precio no puede ser negativo.")
            return
        
        tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()
        
        if tiene_cupon == "sí" or tiene_cupon == "si":
            descuento = float(input("Introduce el valor del cupón de descuento (€): "))
            if descuento > 0:
                precio_final = precio_original - descuento
                if precio_final < 0:
                    precio_final = 0  # El precio no puede ser negativo
                print(f"Precio final con descuento aplicado: {precio_final:.2f} €")
            else:
                print("El valor del cupón debe ser mayor que cero. No se aplica descuento.")
                print(f"Precio final: {precio_original:.2f} €")
        elif tiene_cupon == "no":
            print(f"Precio final sin descuento: {precio_original:.2f} €")
        else:
            print("Respuesta no reconocida. No se aplica descuento.")
            print(f"Precio final: {precio_original:.2f} €")
            
    except ValueError:
        print("Error: Por favor, introduce un número válido.")

# Ejecutar la función
calcular_precio_final()





