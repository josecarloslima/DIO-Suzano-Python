def calcular_saldo(transacoes):
    saldo = 0
    
    # Itera sobre cada transação e atualiza o saldo
    for transacao in transacoes:
        saldo += transacao
    
    # Retorna o saldo formatado em moeda brasileira com duas casas decimais
    return f"Saldo: R$ {saldo:.2f}"  

# Substitua a entrada abaixo para testar com diferentes transações:
entrada_usuario = "[100, -50, 200, -75]"

# Processa a entrada para remover colchetes e espaços desnecessários
entrada_usuario = entrada_usuario.strip("[]").replace(" ", "").replace(",", " ")

# Converte a entrada em uma lista de números
transacoes = [float(valor) for valor in entrada_usuario.split()]

# Calcula o saldo com base nas transações informadas
resultado = calcular_saldo(transacoes)

# Exibe o resultado
print(resultado)