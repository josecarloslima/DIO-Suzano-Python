class Conta:
    def __init__(self, num_agencia, saldo=0):
        self._saldo = saldo
        self.num_agencia = num_agencia

    def depoistar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

# note que se eu quero acessar o valor privado, eu preciso de um método, então se até agora eu não tenho um métoo para lidar com _saldo, eu devo criar um.

    def mostrar_saldo(self):
        return self._saldo

conta = Conta("001", 100)
conta.depoistar(100)
conta.sacar(50)
print(conta.num_agencia)

#agora sim, com o método criado posso chamar o valor privado

print(conta.mostrar_saldo())