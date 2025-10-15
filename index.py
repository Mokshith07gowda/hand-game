import random

# Choices
rock = 1
paper = 2
scissors = 3
lizard = 4
spock = 5

choices = {
    rock: "👊 Rock",
    paper: "📃 Paper",
    scissors: "✂️ Scissors",
    lizard: "🦎 Lizard",
    spock: "🖖 Spock"
}

# Rules: what each choice defeats
rules = {
    rock: [scissors, lizard],
    paper: [rock, spock],
    scissors: [paper, lizard],
    lizard: [paper, spock],
    spock: [rock, scissors]
}

# messages 
messages = {
    (rock, scissors): "Rock crushes Scissors!",
    (rock, lizard): "Rock crushes Lizard!",
    (paper, rock): "Paper covers Rock!",
    (paper, spock): "Paper disproves Spock!",
    (scissors, paper): "Scissors cuts Paper!",
    (scissors, lizard): "Scissors decapitates Lizard!",
    (lizard, paper): "Lizard eats Paper!",
    (lizard, spock): "Lizard poisons Spock!",
    (spock, rock): "Spock vaporizes Rock!",
    (spock, scissors): "Spock smashes Scissors!"
}

print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")

# Print menu
print("Choose your option:")
print("1 - 👊 Rock")
print("2 - 📃 Paper")
print("3 - ✂️ Scissors")
print("4 - 🦎 Lizard")
print("5 - 🖖 Spock")

def play():
    user_choice = int(input("\nEnter your choice (1-5): "))
    if user_choice not in choices:
        print("Invalid choice! Please enter a number from 1 to 5.")
        return

    computer_choice = random.randint(1, 5)

    print(f"\nYou chose: {choices[user_choice]}")
    print(f"Computer chose: {choices[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif computer_choice in rules[user_choice]:
        print(f"You win! {messages[(user_choice, computer_choice)]}")
    else:
        print(f"You lose! {messages[(computer_choice, user_choice)]}")

# Run the game
play()
