import random
def get_choices():
    playerChoice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock","paper","scissors"]
    computerChoice = random.choice(options)

    choices = {"player": playerChoice, "computer": computerChoice}
    return choices

def check_win(player,computer):
    print(f"You chose {player},\ncomputer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose!"
    elif player == "paper":
        if computer == "scissors":
            return "Scissors cut paper! You lose!"
        else:
            return "Paper covers rock! You win!"
    elif player == "scissors":
        if computer == "rock":
            return "Rock smashes scissors! You lose!"
        else:
            return "Scissors cut paper! You win!"
    return [player, computer]

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)