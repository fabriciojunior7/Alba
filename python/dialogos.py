import sys, os, random

class Dialogo(object):
    def __init__(self):
        self.chamadas = []
        file = open("AI/dialogos/saudacoesEntradas.txt", "r")
        self.saudacoesEntradas = file.read().split("\n")
        file.close()
        file = open("AI/dialogos/saudacoesSaidas.txt", "r")
        self.saudacoesSaidas = file.read().split("\n")
        file.close()

        for e in self.saudacoesEntradas:
            self.chamadas.append(e)

    def checar(self, texto):
        for e in self.chamadas:
            if (e in texto):
                self.falar(texto)
                return (True)

        return(False)

    def falar(self, texto):
        for e in self.saudacoesEntradas:
            if (e in texto):
                print(self.saudacoesSaidas[random.randint(0, len(self.saudacoesSaidas) - 1)])
                break