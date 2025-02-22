nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Guilherme", "idade": 28}

print("nome: %s, idade: %d" %(nome, idade))
print("nome: {}, idade: {}" .format(nome, idade))
print("nome: {1}, idade: {0}" .format(idade, nome))
print("nome: {1}, idade: {0}, nome: {1} {1}" .format(idade, nome))
print("nome: {nome}, idade: {idade}" .format(nome=nome, idade=idade))
print("nome: {name}, idade: {age}" .format(name=nome, age=idade))
print("nome: {nome}, idade: {idade}" .format(**dados))
print(f"nome: {nome}, idade: {idade}")
print(f"nome: {nome}, idade: {idade}, saldo: {saldo}")
print(f"nome: {nome}, idade: {idade}, saldo: {saldo:.2f}")
print(f"nome: {nome}, idade: {idade}, saldo: {saldo:10.2f}")