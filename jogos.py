import forca
import adivinhacao

def escolher_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Advinhação")

    jogo = int(input("Escolha: "))

    if (jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao.jogar()
    else:
        print("Escolha inválida.")

if (__name__ == "__main__"):
    escolher_jogo()