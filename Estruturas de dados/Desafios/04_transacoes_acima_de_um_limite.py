def filtrar_transacoes(transacoes, limite):
    transacoes_filtradas = []

    # Itera sobre cada transação na lista
    for transacao in transacoes:
        # Verifica se o valor absoluto da transação é maior que o limite
        if abs(transacao) > limite:
            # Adiciona a transação à lista filtrada
            transacoes_filtradas.append(transacao)

    # Retorna a lista de transações filtradas
    return transacoes_filtradas


# Entrada do usuário
entrada = "[100, -50, 300, -150], 100"

# Separando a entrada nas transações e limite
entrada_transacoes, limite = entrada.split("],")
entrada_transacoes = entrada_transacoes.strip("[]").replace(" ", "") 
limite = float(limite.strip())  # Converte o limite para float

# Converte as transações em uma lista de inteiros
transacoes = [int(valor) for valor in entrada_transacoes.split(",")]

# Filtra as transações que ultrapassam o limite
resultado = filtrar_transacoes(transacoes, limite)

# Exibe as transações filtradas
print(f"Transações: {resultado}")