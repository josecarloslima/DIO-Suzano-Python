from datetime import datetime

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE_OPERACOES = 10
transacoes_do_dia = [] #lista para armazenas as transações diárias
data_atual = datetime.now().date() # guarda a data do dia atual

while True:
    opcao = input(menu)

    # liberando opção de saída "q"
    if opcao == "q":
        print("Saindo... Obrigado por usar nosso sistema!")
        break # encerramento do programa

    # atualiza a data e verifica se já é um "novo dia", se for reseta a transação
    if datetime.now().date() != data_atual:
        data_atual = datetime.now().date()
        transacoes_do_dia.clear()
        numero_saques = 0 

    # verificação do limite diário
    if len(transacoes_do_dia) > LIMITE_OPERACOES:
        print("Operação não realizada. Você atingiu o limite de 10 operações diárias. Por favor aguarde novo dia.")
        continue

    if opcao == "d":
        valor =float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            data_hora_deposito = datetime.now()
            extrato += f"Depósito: R$ {valor:9.2f}   Horário:{data_hora_deposito: %d/%m/%Y %H:%M}\n"
            transacoes_do_dia.append(data_hora_deposito) # registro de depósito
        
        else:
            print("Operação falhou! Valor depoistado inválido!")
        
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")
            
        elif excedeu_limite:
            print("Operação falhou! Limite de saque diário excedido.")
            
        elif excedeu_saques:
            print("Operação falhou! Quantidade de saques diários excedido.")
            
        elif valor > 0:
            saldo -= valor
            data_hora_saque = datetime.now()
            extrato += f"Saque:    R$ {valor:9.2f}   Horário:{data_hora_saque: %d/%m/%Y %H:%M}\n"
            numero_saques += 1
            transacoes_do_dia.append(data_hora_saque) # registro de saque        

        else:
            print("Operação falhou! Valor informado inválido.")
        
    elif opcao == "e":
        print("\n---------- EXTRATO ----------")
        print("Não foram realizadas movikentações." if not extrato else extrato)
        print(f"\nsaldo: R$ {saldo:.2f}")
        print(f"Data atual: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        print("-----------------------------")
        
    else:
        print("Operação Inválida, por favor selecione novamente a opção desejada.")
