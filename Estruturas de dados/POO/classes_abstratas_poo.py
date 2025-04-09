from abc import ABC, abstractmethod, abstractproperty

class Controle_Remoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class Controle_TV(Controle_Remoto):
    def ligar(self):
        print("Lingando a TV...")
        print("TV ligada")
    
    def desligar(self):
        print("Desligando a TV...")
        print("TV desligada")
    
    @property
    def marca(self):
        return "LG"

class Controle_Portao(Controle_Remoto):
    def ligar(self):
        print("Abrindo o portão...")
        print("Portão aberto")
    
    def desligar(self):
        print("Fechando o portão...")
        print("Portão fechado")
    
    @property
    def marca(self):
        return "BRAVOX"

controle = Controle_TV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = Controle_Portao()
controle.ligar()
controle.desligar()
print(controle.marca)
