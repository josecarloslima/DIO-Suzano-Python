class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def __del__(self):
        print("Removendo a instância da classe.")

    def latir(self):
        print("Au!Au!")

def criar_cachorro():
    c = Cachorro("Bob", "Nalhado", False)
    print(c.nome)


c = Cachorro("Lulu", "caramelo")
c.latir()

print("Programa funcionando!")
del c
print("Programa funcionando!")
print("Programa funcionando!")

# criar_cachorro()
