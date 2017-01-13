import os, random

class PesquisarGoogle(object):
    def __init__(self):
        self.chamadas = []
        file = open("AI/funcoes/pesquisarGoogle/__init__.txt", "r")
        self.pesquisarGoogle = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/__respostas__.txt", "r")
        self.respostas = file.read().split("\n")
        file.close()

        for e in self.pesquisarGoogle:
            self.chamadas.append(e)

    def checar(self, texto):
        for e in self.chamadas:
            if (e in texto):
                self.executarFuncao(e, texto)
                return(True)
        else:
            return(False)

    def executarFuncao(self, e, texto):
        google = "https://www.google.com.br/search?q="
        novoE = []
        novoTexto = []
        pops = []
        pesquisa = ""
        imagemDaPesquisa = ""

        for l in texto:
            novoTexto.append(l)
        for l in e:
            novoE.append(l)
        for i in range(len(e)):
            if(novoTexto[i] == novoE[i]):
                pops.append(i)
        pops = pops[::-1]
        for i in pops:
            novoTexto.pop(i)
        for i in range(len(novoTexto)):
            if(novoTexto[i] == "-"):
                novoTexto[i] = "+"
                imagemDaPesquisa += " "
            if(i < len(novoTexto)-1):
                pesquisa += novoTexto[i]
                if(novoTexto[i] != "+"):
                    imagemDaPesquisa += novoTexto[i]

        print(self.respostas[random.randint(0, len(self.respostas) - 1)])
        print("Pesquisando por: %s" % imagemDaPesquisa)
        google += pesquisa
        os.system("start %s" % google)
