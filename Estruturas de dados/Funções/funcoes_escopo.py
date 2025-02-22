salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(salario_bonus(500))

print("------")

def lista_oficial(lista):
    #lista.append(5)
    lista_aux = lista.copy()
    lista_aux.append(5)
    print(f"lista_aux={lista_aux}")
    return lista

lista = [1]
print(lista_oficial(lista))
