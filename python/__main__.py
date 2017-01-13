#11/01/2017

import os, random
import dialogos, funcaoAbrir

os.system("color a")
os.system("cls")

texto = ""

dialogo = dialogos.Dialogo()
abrir = funcaoAbrir.Abrir()

caracteresIgnorar = " !?.,;:(){}[]/*-+_'\"@#$%&"

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

    if(abrir.checar(texto) != False):
        pass
    elif(dialogo.checar(texto)):
        pass
    else:
        print(emojisLista[random.randint(0, len(emojisLista)-1)])

    print("\n")



