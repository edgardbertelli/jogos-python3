import random

def jogar():

    mensagem_boas_vindas()

    palavra_secreta = carregar_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    tentativas = 0

    while (not enforcou and not acertou):
        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_letra_acertada(palavra_secreta, chute, letras_acertadas)
        else:
            tentativas += 1

        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()
        

def mensagem_boas_vindas():
    print("**********************************")
    print("**Bem-vindo(a) ao jogo da Forca!**")
    print("**********************************")

def carregar_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def pede_chute():
    return input("Qual letra? >> ").strip().upper()

def marca_letra_acertada(palavra_secreta, chute, letras_acertadas):
        index = 0
        for letra in palavra_secreta:
            if (chute == letra):
                letras_acertadas[index] = letra
            index += 1

def imprime_mensagem_vencedor():
    print("PARABÉNS! Você ganhou!")

def imprime_mensagem_perdedor():
    print("Você perdeu.")

if (__name__ == "__main__"):
    jogar()