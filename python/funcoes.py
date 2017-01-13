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

        file = open("AI/funcoes/abrir/bloco_de_notas.txt", "r")
        self.bloco_de_notas = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/calculadora.txt", "r")
        self.calculadora = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/cmd.txt", "r")
        self.cmd = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/excel.txt", "r")
        self.excel = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/github.txt", "r")
        self.github = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/media_player.txt", "r")
        self.media_player = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/navegador.txt", "r")
        self.navegador = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/netflix.txt", "r")
        self.netflix = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/notepadPlus.txt", "r")
        self.notepadPlus = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/paint.txt", "r")
        self.paint = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/power_point.txt", "r")
        self.power_point = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/python.txt", "r")
        self.python = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/whatsapp.txt", "r")
        self.whatsapp = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/word_office.txt", "r")
        self.word_office = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/youtube.txt", "r")
        self.youtube = file.read().split("\n")
        file.close()


        for e in self.abrir:
            self.chamadas.append(e)

    def checar(self, texto):
        for e in self.chamadas:
            if (e in texto):
                self.executarFuncao(texto)
                return(True)
        else:
            return(False)

    def executarFuncao(self, texto):
        for e in self.abrir:
            if (e in texto):
                print(self.respostas[random.randint(0, len(self.respostas)-1)])

                for ee in self.bloco_de_notas:
                    if(ee in texto):
                        print("Abrindo o Bloco de Notas...")
                        os.system(self.bloco_de_notas[0])
                        break
                for ee in self.calculadora:
                    if(ee in texto):
                        print("Abrindo o Calculadora...")
                        os.system(self.calculadora[0])
                        break
                for ee in self.cmd:
                    if(ee in texto):
                        print("Abrindo o Prompt de Comando...")
                        os.system(self.cmd[0])
                        break
                for ee in self.excel:
                    if(ee in texto):
                        print("Abrindo o Excel...")
                        os.system(self.excel[0])
                        break
                for ee in self.github:
                    if(ee in texto):
                        print("Abrindo o Github...")
                        os.system(self.github[0])
                        break
                for ee in self.media_player:
                    if(ee in texto):
                        print("Abrindo o Windows Media Player...")
                        os.system(self.media_player[0])
                        break
                for ee in self.navegador:
                    if (ee in texto):
                        print("Abrindo o Navegador...")
                        os.system(self.navegador[0])
                        break
                for ee in self.netflix:
                    if(ee in texto):
                        print("Abrindo o Netflix...")
                        os.system(self.netflix[0])
                        break
                for ee in self.notepadPlus:
                    if(ee in texto):
                        print("Abrindo o Notepad++...")
                        os.system(self.notepadPlus[0])
                        break
                for ee in self.paint:
                    if(ee in texto):
                        print("Abrindo o Paint...")
                        os.system(self.paint[0])
                        break
                for ee in self.power_point:
                    if (ee in texto):
                        print("Abrindo o Power Point Office...")
                        os.system(self.power_point[0])
                        break
                for ee in self.python:
                    if (ee in texto):
                        print("Abrindo o Python...")
                        os.system(self.python[0])
                        break
                for ee in self.whatsapp:
                    if (ee in texto):
                        print("Abrindo o Whatsapp...")
                        os.system(self.whatsapp[0])
                        break
                for ee in self.word_office:
                    if (ee in texto):
                        print("Abrindo o Word Office...")
                        os.system(self.word_office[0])
                        break
                for ee in self.youtube:
                    if (ee in texto):
                        print("Abrindo o YouTube...")
                        os.system(self.youtube[0])
                        break

                break


