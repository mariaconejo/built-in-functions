# 1. Filtrar los números pares de una lista usando filter()
def es_par(numero):
     return numero % 2 == 0

numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(es_par, numeros))
print(pares)  

# 2. Triplicar cada número de una lista usando map()
def tripilicar_numero(numero):
     return numero * 3
numeros = [1, 2, 3]
triplicados = list(map(tripilicar_numero, numeros))
print(triplicados)  

# 3. Convertir palabras en minúsculas a MAYÚSCULAS usando map()
palabras = ["hola", "mundo", "python"]
mayusculas = list(map(str.upper, palabras))
print(mayusculas) 

# 4. Ordenar una lista de números en orden descendente usando sorted()
numeros = [3, 1, 4, 1, 5, 9]
descendente = sorted(numeros, reverse=True)
print(descendente)  

# 5. Redondear los valores de un diccionario
valores = {"a": 3.14159, "b": 2.71828, "c": 1.61803}
redondeados = {k: round(v) for k, v in valores.items()}
print(redondeados) 

# 6. Obtener longitudes de palabras con map()
palabras = ["python", "es", "genial"]
longitudes = list(map(len, palabras))
print(longitudes)  

# 7. Filtrar palabras cortas con filter()
palabras = ["cielo", "sol", "estrella", "luz", "universo"]
largas = list(filter(lambda palabra: len(palabra) >= 5, palabras))
print(largas)  

# 8. Convertir una lista de strings a enteros con map()
strings = ["1", "2", "3"]
enteros = list(map(int, strings))
print(enteros)  

# 9. Filtrar números positivos con filter()
numeros = [-10, 5, 0, -2, 3, 8]
positivos = list(filter(lambda x: x > 0, numeros))
print(positivos)  # Salida: [5, 3, 8]

# 10. Ordenar tuplas por el segundo valor con sorted()
tuplas = [("Juan", 25), ("Ana", 20), ("Luis", 30)]
ordenadas = sorted(tuplas, key=lambda x: x[1])
print(ordenadas) 

# 11. Convertir Celsius a Fahrenheit con map()
celsius = [0, 20, 30, 40]
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
print(fahrenheit)

# 12. Redondear una lista de decimales con map()
decimales = [4.3, 5.7, 8.2]
redondeados = list(map(round, decimales))
print(redondeados) 

# 13. Lista única y ordenada
repetidos = [5, 3, 5, 2, 3, 1]
unicos_ordenados = sorted(set(repetidos))
print(unicos_ordenados)
