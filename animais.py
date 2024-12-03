from abc import ABC, abstractmethod

class Animais(ABC):
    def __init__(self, nome, idade):
        self.__nome=nome
        self.__idade=idade

    def getNome(self):
        return self.__nome
    def getIdade(self):
        return self.__idade
    
    def setNome(self):
        return self.__nome
    def setIdade(self):
        return self.__idade
    
    @abstractmethod
    def mostrar(self):
        pass