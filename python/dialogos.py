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

    def checar(self, entrada):
        if(entrada in self.chamadas):
            self.falar(entrada)
            return(True)
        else:
            return(False)

    def falar(self, entrada):
        if (entrada in self.saudacoesEntradas):
            print(self.saudacoesSaidas[random.randint(0, len(self.saudacoesSaidas) - 1)])