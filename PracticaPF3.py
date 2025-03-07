# Paso 1: Generar una lista de números del 1 al 10
numeros = list(range(1, 11))

# Filtrar los números pares utilizando una función lambda
pares = list(filter(lambda x: x % 2 == 0, numeros))

# Paso 2: Calcular el cuadrado de cada número par
cuadrados = list(map(lambda x: x ** 2, pares))

# Paso 3: Sumar los cuadrados para obtener la suma total
suma_total = sum(cuadrados)

print(f"Números pares: {pares}")
print(f"Cuadrados: {cuadrados}")
print(f"Suma total de los cuadrados: {suma_total}")
