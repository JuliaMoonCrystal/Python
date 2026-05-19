import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header():
    print("=" * 30)
    print("      PEDRA, PAPEL E TESOURA")
    print("=" * 30)

def get_user_choice():
    while True:
        print("\nEscolha sua jogada:")
        print("[ 1 ] PEDRA")
        print("[ 2 ] PAPEL")
        print("[ 3 ] TESOURA")
        print("[ 0 ] SAIR")
        
        choice = input("Sua opção: ")
        
        if choice in ['1', '2', '3', '0']:
            return int(choice)
        else:
            print("\nOpção inválida! Tente novamente.")

def play():
    options = {1: "PEDRA", 2: "PAPEL", 3: "TESOURA"}
    
    user_score = 0
    computer_score = 0
    
    while True:
        clear_screen()
        show_header()
        print(f"PLACAR: VOCÊ {user_score} X {computer_score} COMPUTADOR")
        
        user_move = get_user_choice()
        
        if user_move == 0:
            print("\nObrigado por jogar! Até a próxima.")
            break
            
        computer_move = random.randint(1, 3)
        
        print("\nJO...")
        time.sleep(0.5)
        print("KEN...")
        time.sleep(0.5)
        print("PO!!!")
        time.sleep(0.3)
        
        print("\n" + "-" * 20)
        print(f"Você jogou: {options[user_move]}")
        print(f"Computador jogou: {options[computer_move]}")
        print("-" * 20)
        
        # Win/Loss logic
        if user_move == computer_move:
            print("\n>> EMPATE! <<")
        elif (user_move == 1 and computer_move == 3) or \
             (user_move == 2 and computer_move == 1) or \
             (user_move == 3 and computer_move == 2):
            print("\n>> VOCÊ VENCEU! <<")
            user_score += 1
        else:
            print("\n>> O COMPUTADOR VENCEU! <<")
            computer_score += 1
            
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    play()
