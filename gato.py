from animais import Animais

class Gato(Animais):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.__raca=raca

    def getRaca(self):
        return self.__raca
    
    def setRaca(self):
        return self.__raca
    
    def mostrar(self):
        return (f"O gato tem o nome: {self.getNome()}, sua idade: {self.getIdade()} e seu raça: {self.getRaca()}")
