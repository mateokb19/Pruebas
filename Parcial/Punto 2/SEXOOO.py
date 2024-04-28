# Definimos la función para multiplicar por 3
def multiplicar_por_3(numero):
    return numero * 3

# Definimos la función para verificar si es par
def es_par(numero):
    return numero % 2 == 0


# Usamos map para multiplicar cada valor por 3
resultado_map = map(multiplicar_por_3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Usamos filter para encontrar los números pares
numeros_pares = list(filter(es_par, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print(resultado_map)
print(numeros_pares)