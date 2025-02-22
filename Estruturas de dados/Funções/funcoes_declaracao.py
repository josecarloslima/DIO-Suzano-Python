def exibir_mensagem2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem2(nome="Guilherme")
exibir_mensagem2("Gui")
exibir_mensagem3()
exibir_mensagem3(nome="Chappie")