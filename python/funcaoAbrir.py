import os, random

class Abrir(object):
    def __init__(self):
        #Abrir
        self.chamadas = []
        file = open("AI/funcoes/abrir/__init__.txt", "r")
        self.abrir = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/__respostas__.txt", "r")
        self.respostas = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/programas/bloco_de_notas.txt", "r")
        self.bloco_de_notas = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/programas/calculadora.txt", "r")
        self.calculadora = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/sites/cinema_partage.txt", "r")
        self.cinema_partage = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/programas/cmd.txt", "r")
        self.cmd = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/sites/cube_timer.txt", "r")
        self.cube_timer = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/pastas/disco_local.txt", "r")
        self.disco_local = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/pastas/downloads.txt", "r")
        self.downloads = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/programas/dropbox.txt", "r")
        self.dropbox = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/programas/editor_do_registro.txt", "r")
        self.editor_do_registro = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/sites/email.txt", "r")
        self.email = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/programas/excel.txt", "r")
        self.excel = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/sites/facebook.txt", "r")
        self.facebook = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/programas/fsx.txt", "r")
        self.fsx = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/programas/gerenciador_de_tarefas.txt", "r")
        self.gerenciador_de_tarefas = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/sites/github.txt", "r")
        self.github = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/sites/gmail.txt", "r")
        self.gmail = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/sites/google_maps.txt", "r")
        self.google_maps = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/sites/habbo_br.txt", "r")
        self.habbo_br = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/sites/habbo_us.txt", "r")
        self.habbo_us = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/pastas/imagens.txt", "r")
        self.imagens = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/pastas/lixeira.txt", "r")
        self.lixeira = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/programas/lupa.txt", "r")
        self.lupa = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/programas/media_player.txt", "r")
        self.media_player = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/sites/mercado_livre.txt", "r")
        self.mercado_livre = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/pastas/meus_documentos.txt", "r")
        self.meus_documentos = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/programas/narrador.txt", "r")
        self.narrador = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/sites/navegador.txt", "r")
        self.navegador = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/sites/netflix.txt", "r")
        self.netflix = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/programas/notepadPlus.txt", "r")
        self.notepadPlus = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/programas/painel_de_controle.txt", "r")
        self.painel_de_controle = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/programas/paint.txt", "r")
        self.paint = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/pastas/pasta_dropbox.txt", "r")
        self.pasta_dropbox = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/programas/power_point.txt", "r")
        self.power_point = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/programas/pycharm.txt", "r")
        self.pycharm = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/programas/python.txt", "r")
        self.python = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/sites/tradutor.txt", "r")
        self.tradutor = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/programas/teclado_virtual.txt", "r")
        self.teclado_virtual = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/programas/utorrent.txt", "r")
        self.utorrent = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/sites/whatsapp.txt", "r")
        self.whatsapp = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/programas/word_office.txt", "r")
        self.word_office = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/programas/wordpad.txt", "r")
        self.wordpad = file.read().split("\n")
        file.close()

        file = open("AI/funcoes/abrir/sites/youtube.txt", "r")
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
                for ee in self.cinema_partage:
                    if(ee in texto):
                        print("Abrindo o Cinema do Partage...")
                        os.system(self.cinema_partage[0])
                        break
                for ee in self.cmd:
                    if(ee in texto):
                        print("Abrindo o Prompt de Comando...")
                        os.system(self.cmd[0])
                        break
                for ee in self.cube_timer:
                    if(ee in texto):
                        print("Abrindo o CubeTimer...")
                        os.system(self.cube_timer[0])
                        break
                for ee in self.disco_local:
                    if(ee in texto):
                        print("Abrindo os Disco C:\...")
                        os.system(self.disco_local[0])
                        break
                for ee in self.downloads:
                    if(ee in texto):
                        print("Abrindo os Downloads...")
                        os.system(self.downloads[0])
                        break
                for ee in self.dropbox:
                    if(ee in texto):
                        print("Abrindo o Dropbox...")
                        os.system(self.dropbox[0])
                        break
                for ee in self.editor_do_registro:
                    if(ee in texto):
                        print("Abrindo o Editor do Registro...")
                        os.system(self.editor_do_registro[0])
                        break
                for ee in self.email:
                    if(ee in texto):
                        print("Abrindo o Hotmail...")
                        os.system(self.email[0])
                        break
                for ee in self.excel:
                    if(ee in texto):
                        print("Abrindo o Excel...")
                        os.system(self.excel[0])
                        break
                for ee in self.facebook:
                    if(ee in texto):
                        print("Abrindo o Facebook...")
                        os.system(self.facebook[0])
                        break
                for ee in self.fsx:
                    if(ee in texto):
                        print("Abrindo o Flight Simulator X...")
                        os.system(self.fsx[0])
                        break
                for ee in self.gerenciador_de_tarefas:
                    if(ee in texto):
                        print("Abrindo o Gerenciador de Tarefas...")
                        os.system(self.gerenciador_de_tarefas[0])
                        break
                for ee in self.github:
                    if(ee in texto):
                        print("Abrindo o Github...")
                        os.system(self.github[0])
                        break
                for ee in self.gmail:
                    if(ee in texto):
                        print("Abrindo o Gmail...")
                        os.system(self.gmail[0])
                        break
                for ee in self.google_maps:
                    if(ee in texto):
                        print("Abrindo o Google Mapas...")
                        os.system(self.google_maps[0])
                        break
                for ee in self.habbo_br:
                    if(ee in texto):
                        print("Abrindo o Habbo Hotel...")
                        os.system(self.habbo_br[0])
                        break
                for ee in self.habbo_us:
                    if(ee in texto):
                        print("Abrindo o Habbo Hotel Americano...")
                        os.system(self.habbo_us[0])
                        break
                for ee in self.imagens:
                    if(ee in texto):
                        print("Abrindo as Suas Imagens...")
                        os.system(self.imagens[0])
                        break
                for ee in self.lixeira:
                    if(ee in texto):
                        print("Abrindo a Lixeira...")
                        os.system(self.lixeira[0])
                        break
                for ee in self.lupa:
                    if(ee in texto):
                        print("Abrindo a Lupa...")
                        os.system(self.lupa[0])
                        break
                for ee in self.media_player:
                    if(ee in texto):
                        print("Abrindo o Windows Media Player...")
                        os.system(self.media_player[0])
                        break
                for ee in self.mercado_livre:
                    if(ee in texto):
                        print("Abrindo o Mercado Livre...")
                        os.system(self.mercado_livre[0])
                        break
                for ee in self.meus_documentos:
                    if(ee in texto):
                        print("Abrindo os Seus Documentos...")
                        os.system(self.meus_documentos[0])
                        break
                for ee in self.narrador:
                    if (ee in texto):
                        print("Abrindo o Narrador...")
                        os.system(self.narrador[0])
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
                for ee in self.painel_de_controle:
                    if(ee in texto):
                        print("Abrindo o Painel de Controle...")
                        os.system(self.painel_de_controle[0])
                        break
                for ee in self.paint:
                    if(ee in texto):
                        print("Abrindo o Paint...")
                        os.system(self.paint[0])
                        break
                for ee in self.pasta_dropbox:
                    if(ee in texto):
                        print("Abrindo a Pasta do Dropbox...")
                        os.system(self.pasta_dropbox[0])
                        break
                for ee in self.power_point:
                    if (ee in texto):
                        print("Abrindo o Power Point Office...")
                        os.system(self.power_point[0])
                        break
                for ee in self.pycharm:
                    if (ee in texto):
                        print("Abrindo o Pycharm...")
                        os.system(self.pycharm[0])
                        break
                for ee in self.python:
                    if (ee in texto):
                        print("Abrindo o Python...")
                        os.system(self.python[0])
                        break
                for ee in self.tradutor:
                    if (ee in texto):
                        print("Abrindo o Google Tradutor...")
                        os.system(self.tradutor[0])
                        break
                for ee in self.teclado_virtual:
                    if (ee in texto):
                        print("Abrindo o Teclado Virtual...")
                        os.system(self.teclado_virtual[0])
                        break
                for ee in self.utorrent:
                    if (ee in texto):
                        print("Abrindo o uTorrent...")
                        os.system(self.utorrent[0])
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
                for ee in self.wordpad:
                    if (ee in texto):
                        print("Abrindo o WordPad...")
                        os.system(self.wordpad[0])
                        break
                for ee in self.youtube:
                    if (ee in texto):
                        print("Abrindo o YouTube...")
                        os.system(self.youtube[0])
                        break

                break


