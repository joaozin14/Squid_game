import random
import os

def pedra_papel_tesoura():
    while True:
        print("Seja bem vindo ao squid game, vamos jogar! \n")

        escolhas = ["pedra", "papel", "tesoura"]
        escolha_usuario = input("Qual sua jogada? (Pedra, Papel ou Tesoura): ").lower()

        if escolha_usuario not in escolhas:
            print("Jogue pedra, papel ou tesoura")
            return
        
        computer_choice = random.choice(escolhas)
        print(f"O computador escolheu {computer_choice}!\n")

        if escolha_usuario == computer_choice:
            print("Deu empate!\n")
        elif escolha_usuario == "pedra" and computer_choice == "tesoura" or \
        escolha_usuario == "papel" and computer_choice == "pedra" or \
        escolha_usuario == "tesoura" and computer_choice == "papel":
            print("O jogador ganhou!\n")
        else:
            print("O computador ganhou!\n")
        
        continuar = input("Deseja jogar novamente?(S/N): ").lower()
        if continuar == "s":
            pedra_papel_tesoura()
        if continuar == "n":
            print("Até mais!")
            break

pedra_papel_tesoura()