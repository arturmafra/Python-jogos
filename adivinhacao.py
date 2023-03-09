import random

def jogar_adivinhacao():
    print("*******************************")
    print("Bem-vindo ao jogo de adivinhação")
    print("*******************************")



    numero_secreto = random.randrange (1,101)


    print("Escolha seu nível de dificuldade")
    print("Nível fácil (1) Nível médio (2) Nível difícil (3)")


    nivel = int(input("Defina seu nível: "))

    total_de_tentativas = 5

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5




    for total_de_tentativas in range(1,total_de_tentativas + 1):
        print("rodada: " , total_de_tentativas)
        chute_string = input("Digite o seu número (de 1 a 100): ")
        chute = int(chute_string)
        print("Você digitou " , chute_string)

        acertou = chute == numero_secreto
        errou_para_mais = chute > numero_secreto
        errou_para_menos = chute < numero_secreto

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 a 100 !")
            continue

        if (acertou):
            print("Você acertou!!!")
            break
        else:
            if(errou_para_mais):
                print("O número chutado é maior que o número secreto")
            elif(errou_para_menos):
                print("O número chutado é menor do que o número secreto")

        total_de_tentativas = total_de_tentativas - 1

if(__name__== "__main__"):
    jogar_adivinhacao()




