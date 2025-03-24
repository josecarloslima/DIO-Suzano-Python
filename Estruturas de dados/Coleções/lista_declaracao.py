frutas = ["laranja", "maca", "uva"]
print(frutas)

frutas = []
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

frutas = ["maçã", "laranja", "uva", "pera"]
print(frutas[0])
print(frutas[2])

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

lista = ["p", "y", "t", "h", "o", "n"]
print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])

carros = ["Gol", "celta", "palio"]

for carro in carros:
    print(carros)

carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

numeros = [1, 30, 21, 1, 9, 65, 34]
pares = []

# usando for
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

numeros = [1, 30, 21, 1, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)

numeros = [1, 30, 21, 1, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]

print(quadrado)
