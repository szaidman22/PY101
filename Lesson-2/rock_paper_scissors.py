import random

OPPONENTS = {'1': ["Martha", "(~˘▾˘)~"],
             '2': ["Alphonse", "◉_◉"],
             '3': ["HoneyBun", "ʕ♥ᴥ♥ʔ"],
             '4': ["Bamboozle", "(°o•)"],
             '5': ["Moo Deng", "⊂(◉‿◉)つ"]
}

CHOICE_LOOKUP = {"rock": ["r",["scissors", "lizard"]],
                "paper": ["p", ["rock","spock"]],
                "scissors": ["sc",["paper","lizard"]],
                "lizard": ["l",["paper" , "spock"]],
                "spock": ["sp,",["rock","scissors"]]
}

# prompt prefix
def prompt(message):
    print(f"===> {message}")

def get_player_name():
    prompt(f"Welcome to {', '.join(CHOICE_LOOKUP.keys())}!")
    return input("===> Please enter your name: ")

def get_opponent_name_face():
    prompt("Choose your opponent (enter number):")

    for key, value in OPPONENTS.items():
        prompt(f"{key}) {value[0]}: {value[1]}")

    opponent_key = input("Opponent Selection: ")

    while opponent_key not in OPPONENTS:
        opponent_key = input("Please enter a valid numeric choice to "
                                "choose your opponent: ")

    prompt(f"Your opponent is: {OPPONENTS[opponent_key][0]} ")

    return OPPONENTS[opponent_key][0], OPPONENTS[opponent_key][1]

def get_valid_choice():
    prompt("That's not a valid choice.\n"
            f"Please enter one: {', '.join(CHOICE_LOOKUP.keys())}")
    return input().casefold()

def get_player_choice():
    prompt(f"Choose one: {', '.join(CHOICE_LOOKUP.keys())}")
    player_choice = input().casefold()

    while player_choice[0] == "s" and len(player_choice) == 1:
        player_choice = get_valid_choice()

    while player_choice[0] == "s" and player_choice[1] not in ["c","p"]:
        player_choice = get_valid_choice()

    while player_choice[0] not in [choice[0].casefold() for choice in CHOICE_LOOKUP.keys()]:
        player_choice = get_valid_choice()

    for key, item in CHOICE_LOOKUP.items():
        if player_choice.startswith(item[0]):
            player_choice = key

    match player_choice[0]:
        case 'r':
            return "rock"
        case 'p':
            return "paper"
        case "l":
            return "lizard"
        case _ :
            match player_choice[0:2]:
                case "sp":
                    return "spock"
                case "sc":
                    return "scissors"

    return player_choice

def print_rps_results(player_choice, opponent_choice):

    prompt(f"{PLAYER_NAME} ~~~~~> {player_choice}")
    prompt(f"{OPPONENT_NAME} ~~~~~> {opponent_choice}")

    if opponent_choice in CHOICE_LOOKUP[player_choice][1]:
        prompt(f"**** {PLAYER_NAME} wins! **** :)")
    elif player_choice in CHOICE_LOOKUP[opponent_choice][1]:
        prompt(f"{OPPONENT_NAME} wins {OPPONENT_FACE}")
    else:
        prompt("It's a tie!")

PLAYER_NAME = get_player_name()

OPPONENT_NAME, OPPONENT_FACE = get_opponent_name_face()

while True:

    player_choice = get_player_choice()
    opponent_choice = random.choice([key for key in CHOICE_LOOKUP.keys()])
    print_rps_results(player_choice, opponent_choice)

    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt("That's not a valid choice")

    if answer[0] == 'n':
        break
