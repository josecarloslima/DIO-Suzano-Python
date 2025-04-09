class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} ({self.matricula}) - {self.escola}"

gui = Estudante("Guilherme", 1406)
gi = Estudante("Giovana", 1745)

print(gui)
print(gi)