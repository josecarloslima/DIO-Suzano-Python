conjunto_a = {1,2}
conjunto_b = {3,4}
print(conjunto_a.union(conjunto_b))

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}
print(conjunto_a.intersection(conjunto_b))

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}
print(conjunto_a.symmetric_difference(conjunto_b))

conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}
print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9}
conjunto_c = {1,0}
print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))

sorteio = {1,23}
sorteio.add(25)
print(sorteio)
sorteio.add(42)
print(sorteio)
sorteio.add(25)
print(sorteio)

sorteio = {1,23}
print(sorteio)
sorteio.clear()
print(sorteio)

sorteio = {1,23}
print(sorteio)
sorteio.copy()
print(sorteio)

numeros = {1,2,3,1,2,4,5,5,67,8,9,0}
print(numeros)
numeros.discard(1)
print(numeros)
numeros.discard(45)
print(numeros)

numeros = {1,2,3,1,2,4,5,5,67,8,9,0}
print(numeros)
numeros.pop()
print(numeros)
numeros.pop()
print(numeros)

numeros = {1,2,3,1,2,4,5,5,67,8,9,0}
print(numeros)
numeros.remove(67)
print(numeros)

numeros = {1,2,3,1,2,4,5,5,67,8,9,0}
print(len(numeros))

numeros = {1,2,3,1,2,4,5,5,67,8,9,0}
print(1 in numeros)
print(10 in numeros)