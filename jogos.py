import adivinhacao
import forca



print("***********************")
print("***Escolha seu jogo!***")
print("***********************")

print("Adivinhação (1) || Forca (2)")

jogo = int(input("Digite o número do jogo que deseja jogar: "))

if(jogo == 1):
    print("Jogando Advinhação...")
    adivinhacao.jogar_adivinhacao()
elif(jogo == 2):
    print("Jogando Forca...")
    forca.jogar()

