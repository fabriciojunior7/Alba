import os

class Funcao(object):
    def __init__(self):
        self.chamadas = []
        file = open("AI/funcoes/abrir/__init__.txt", "r")
        self.abrir = file.read().split("\n")
        file.close()

        for e in self.abrir:
            self.chamadas.append(e)

    def checar(self, entrada):
        if(entrada in self.chamadas):
            self.executarFuncao(entrada)
            return(True)
        else:
            return(False)

    def executarFuncao(self, entrada):
        if(entrada in self.abrir):
            os.system("start c:/")


