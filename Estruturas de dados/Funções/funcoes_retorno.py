def calcular_total(numeros):
    return sum(numeros)

print(calcular_total([10, 20, 34]))

print("-----")

def retorna_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

print(retorna_antecessor_sucessor(10))

print("-----")

def func_3():
    print("Olá, Mundo!")

print(func_3())