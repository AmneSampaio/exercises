import random

print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 0
pontos = 1000

print("Por favor, escolha o nível de dificuldade", numero_secreto)
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Digite "))

if   (nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas = 10
elif (nivel == 3):
    total_de_tentativas =  5
else:
    print("Insira um nível válido")


for rodada in range(1,total_de_tentativas+1):
# while(rodada <= total_de_tentativas):

    print("Tentativa {} de {}.".format(rodada, total_de_tentativas))
    chute = int(input("Digite um número entre 1 e 100: "))
    type(chute)
    print("Você digitou", chute)

    if (chute<1 or chute >100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = numero_secreto == chute
    maior = chute>numero_secreto
    menor = chute<numero_secreto

    if (acertou):
        print("Você acertou e fez {} pontos, parabéns!".format(pontos))
        break
    else:
        if(maior):
            print("Seu chute foi maior que o número secreto")
        else:
            print("Seu chute foi menor que o número secreto")
        pontos = pontos - abs(numero_secreto-chute)

print("Você fez {} pontos".format(pontos))
print("O número secreto é", numero_secreto)
print("Foi muito bom jogar com você! Fim do jogo")