# Solicita la entrada de usuario para el juego piedra papel o tijera
# Genera la elección de la máquina de forma aleatoria
# Compara la elección del usuario con la de la máquina y determina el resultado
# Permita que el ususario juegue las veces que quiera hasta que decida salir
# LLeva un regristro de la puntuacion y muestra el resultado al final del juego

import random

def get_computer_choice():
    # Genera aleatoriamente una elección para la computadora
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    # Solicita la elección del usuario y la valida
    while True:
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def determine_winner(user_choice, computer_choice):
    # Determina el ganador basado en las reglas del juego
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1
        
        # Preguntar al usuario si quiere jugar otra ronda
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    
    # Mostrar la puntuación final
    print(f"\nFinal Score - You: {user_score} | Computer: {computer_score}")
    print("Thanks for playing!")

# Iniciar el juego
if __name__ == "__main__":
    play_game()