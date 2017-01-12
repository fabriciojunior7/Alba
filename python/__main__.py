#11/01/2017

import os, random
import dialogos, funcoes

os.system("color a")
os.system("cls")

dialogo = dialogos.Dialogo()
funcao = funcoes.Funcao()



while(True):
    entrada = raw_input(">> ").lower()

    if(funcao.checar(entrada) != False):
        pass
    elif(dialogo.checar(entrada)):
        pass
    else:
        print("VAZIO")



