MAIOR_IDADE = 18
idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade")

if idade < MAIOR_IDADE:
    print("Menor idade")

print("-----------")

if idade >= MAIOR_IDADE:
    print("Pode tirar CNH")
else:
    print("Não pode tirar CNH")

print("--------")
IDADE_ESPECIAL = 17

if idade >= MAIOR_IDADE:
    print("Pode fazer as aulas e tirar a habilitação")
elif idade == IDADE_ESPECIAL:
    print("pode fazer as aulas mas não pode tirar a habilitação")
else:
    print("Não pode fazer as aulas ou tirar habilitação")