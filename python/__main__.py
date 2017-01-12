#11/01/2017

import os, random
import dialogos, funcoes

os.system("color a")
os.system("cls")

texto = ""

dialogo = dialogos.Dialogo()
funcao = funcoes.Funcao()

caracteresIgnorar = "!?.,;:(){}[]/*-+_'\"@#$%&"



while(True):
    texto = ""
    entrada = raw_input(">> ").lower()
    for l in entrada:
        if(l not in caracteresIgnorar):
            texto += l

    if(funcao.checar(texto) != False):
        pass
    elif(dialogo.checar(texto)):
        pass
    else:
        print("VAZIO")

    print("\n")



