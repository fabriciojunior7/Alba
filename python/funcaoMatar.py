import os

class Matar(object):
    def __init__(self):
        self.chamadas = []
        file = open("AI/funcoes/matar/__init__.txt", "r")
        self.matar = file.read().split("\n")
        file.close()

        for e in self.matar:
            self.chamadas.append(e)

    def checar(self, texto):
        for e in self.chamadas:
            if (e in texto):
                self.executarFuncao(texto)
                return(True)
        else:
            return(False)

    def executarFuncao(self, texto):
        os.system("taskkill /F /IM utorrent.exe /T")
        os.system("taskkill /F /IM Dropbox.exe /T")
        os.system("taskkill /F /IM OneDrive.exe /T")
        os.system("taskkill /F /IM nvtray.exe /T")