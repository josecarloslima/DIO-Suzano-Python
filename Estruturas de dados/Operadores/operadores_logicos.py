saldo = 1000
saque = 200
limite = 100

print(saldo>=saque and saque<=limite)
print(not saque<=limite)
print((saldo>=saque or saque<=limite) and (not saque<=limite))

conta_normal_com_saldo = saldo>=saque or saque<=limite
conta_especial_com_saldo = not saque<=limite
calculo = conta_normal_com_saldo or conta_especial_com_saldo
print(calculo)

print("----------")
print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)
print(not True)
print(not False)