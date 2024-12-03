from animais import Animais

class Cachorro(Animais):
    def __init__(self, nome, idade, porte):
        super().__init__(nome, idade)
        self.__porte=porte

    def getPorte(self):
        return self.__porte
    
    def setPorte(self):
        return self.__porte
    
    def mostrar(self):
        return (f"O cachorro tem o nome: {self.getNome()}, sua idade: {self.getIdade()} e seu porte: {self.getPorte()}")
    