import os

class Funcao(object):
    def __init__(self):
        #Abrir
        self.chamadas = []
        file = open("AI/funcoes/abrir/__init__.txt", "r")
        self.abrir = file.read().split("\n")
        file.close()
        file = open("AI/funcoes/abrir/paint.txt", "r")
        self.paint = file.read().split("\n")
        file.close()


        for e in self.abrir:
            self.chamadas.append(e)

    def checar(self, texto):
        for e in self.chamadas:
            if (e in texto):
                self.executarFuncao(texto)
                return (True)
        else:
            return(False)

    def executarFuncao(self, texto):
        for e in self.abrir:
            if (e in texto):
                for ee in self.paint:
                    if(ee in texto):
                        os.system("start mspaint.exe")


