
import random

CHOICES = ['rock', 'paper', 'scissors']

# prompt prefix
def prompt(message):
    print(f"===> {message}")

def get_player_name():
    prompt("Welcome to rock, paper, scissors!")
    return input("===> Please enter your name: ")

def get_player_choice():
    prompt(f"Choose one: {', '.join(CHOICES)}")
    player_choice = input()

    while player_choice not in CHOICES:
        prompt("That's not a valid choice.\n"
            f"Please enter one: {', '.join(CHOICES)}")
        player_choice = input()
    
    return player_choice

def print_rps_results(player_choice, oponent_choice):

    global PLAYER_NAME, OPONENT_NAME

    prompt(f"{PLAYER_NAME} ~~~~~> {player_choice}")
    prompt(f"{OPONENT_NAME} ~~~~~> {oponent_choice}")

    if ((player_choice == "rock" and oponent_choice == "scissors") or
        (player_choice == "paper" and oponent_choice == "rock") or
        (player_choice == "scissors" and oponent_choice == "paper")):
        prompt(f"**** {PLAYER_NAME} wins! **** :)")
    elif ((player_choice == "rock" and oponent_choice == "paper") or
        (player_choice == "paper" and oponent_choice == "scissors") or
        (player_choice == "scissors" and oponent_choice == "rock")):
        prompt(f"{OPONENT_NAME} wins :(")
    else:
        prompt("It's a tie!")


PLAYER_NAME = get_player_name()

OPONENT_NAME = "Computer"

while True:

    player_choice = get_player_choice()
    oponent_choice = random.choice(CHOICES)
    print_rps_results(player_choice, oponent_choice)

    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break
        else:
            prompt("That's not a valid choice")

    if answer[0] == 'n':
        break