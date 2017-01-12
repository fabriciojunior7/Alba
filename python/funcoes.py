import os, random

class Funcao(object):
    def __init__(self):
        #Abrir
        self.chamadas = []
        file = open("AI/funcoes/abrir/__init__.txt", "r")
        self.abrir = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/__respostas__.txt", "r")
        self.respostas = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/navegador.txt", "r")
        self.navegador = file.read().split("\n")
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
                print(self.respostas[random.randint(0, len(self.respostas)-1)])

                for ee in self.navegador:
                    if (ee in texto):
                        print("Abrindo o Navegador...")
                        os.system("start https://www.google.com.br/")
                        break
                for ee in self.paint:
                    if(ee in texto):
                        print("Abrindo o Paint...")
                        os.system("start mspaint.exe")
                        break


