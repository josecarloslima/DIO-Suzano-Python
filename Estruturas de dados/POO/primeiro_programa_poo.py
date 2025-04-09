# caracteristicas: cor, modelo, ano e valor
# comportamentos: buzinar, parar e correr

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Briiimmmm... Briiimmmm")

    def parar(self):
        print("Bicicleta parando...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vruuummm!")

b1 = Bicicleta("vermelha", "mountan bike", 2022, 600) 
b1.buzinar()
b1.correr()
b1.parar()

# podemos acessar os atribtus de forma simples unindo variável ao atributo
print(b1.ano, b1.cor, b1.modelo, b1.valor)