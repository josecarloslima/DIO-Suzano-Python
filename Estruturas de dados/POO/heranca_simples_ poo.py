class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor 
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def Ligar_motor(self):
        print("Ligando o motor!")


class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim,' if self.carregado else 'Não,'} estou carregado")

moto = Motocicleta("preta", "DEM-0666", 2)
moto.Ligar_motor()

celta = Carro("azul", "GEM-1406", 4)
celta.Ligar_motor()
# celta.carregado()

scania = Caminhao("adesivado", "VAI-4554", 16, True)
scania.Ligar_motor()
scania.esta_carregado()
print(scania.cor)