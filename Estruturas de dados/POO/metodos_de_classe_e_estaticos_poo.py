class Pessoa:
    def __init__ (self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

# automatizador de idade
#    def saber_idade(self, ano, mes, dia, nome):
#        idade = 2025 - ano
#        return Pessoa(nome, idade)

# método de classe ou método de fábrica
#    @classmethod
#    def saber_idade(cls, ano, mes, dia, nome):
#        idade = 2025 - ano
#        return cls(nome, idade)

# método estático
    @staticmethod
    def saber_idade(idade):
        return idade >= 18

# primeira chamada
# p = Pessoa("Guilherme", 28)

# segunda chamada
# p = Pessoa().saber_idade(1994, 3, 21, "Anastácio")

# terceira chamada - metodo de classe
# p = Pessoa.saber_idade(1975, 2, 27, "Zuzu")

# quarta chamada - método estático
print(Pessoa.saber_idade(18))
print(Pessoa.saber_idade(10))
print(Pessoa.saber_idade(26))

# print(p.nome, p.idade)