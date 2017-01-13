#11/01/2017

import os, random
import dialogos, funcaoAbrir, funcaoPesquisarGoogle

def main():

    os.system("color a")
    os.system("cls")

    texto = ""

    dialogo = dialogos.Dialogo()
    abrir = funcaoAbrir.Abrir()
    google = funcaoPesquisarGoogle.PesquisarGoogle()

    caracteresIgnorar = " !?.,;:(){}[]/*-+_'\"@#$%&~^"

    #Temporarios
    emojis = open("AI/dialogos/emojisFelizes.txt", "r")
    emojisLista = emojis.read().split("\n")
    emojis.close()



    while(True):
        texto = ""
        entrada = raw_input(">> ").lower()
        print("\n")

        for l in entrada:
            if(l not in caracteresIgnorar):
                texto += l
            elif(l == " "):
                texto += "-"
        texto = "-" + texto + "-"

        if("atualizar" in entrada or "atualize" in entrada):
            main()
        elif(google.checar(texto) != False):
            pass
        elif(abrir.checar(texto) != False):
            pass
        elif(dialogo.checar(texto)):
            pass
        else:
            print(emojisLista[random.randint(0, len(emojisLista)-1)])

        print("\n")




main()



