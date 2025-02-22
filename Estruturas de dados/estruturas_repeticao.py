a = int(input("informe um numero inteiro: "))
print(a)

a += 1
print(a)

a+=1
print(a)

print("----------")

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()
    print("executado no final do laço")
    
print("----------")

for numero in range(0, 11):
    print(numero, end=" ")

# tabuada do 5
for numero in range(0,51,5):
    print(numero, end=" ")

print("----------")

opcao = -1
while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo extrato...")
else:
    print("Obrigado e até logo!")

print("----------")

while True:
    numero = int(input("informe um numero: "))
    if numero == 5:
        break
    print(numero)

for numero in range(10):
    if numero == 5:
        break
    print(numero, end=" ")

print("----------")

for numero in range(10):
    if numero == 5:
        continue
    print(numero, end=" ")

print("----------")

while True:
    numero = int(input("informe um numero:"))
    if numero == 10:
        break
    if numero % 2 == 0:
        continue
print(numero)