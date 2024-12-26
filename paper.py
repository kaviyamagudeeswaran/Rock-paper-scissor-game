import random

def game():
    while True:
        Ramu = input("Enter a choice (rock, paper, scissors): ").lower()
        while Ramu not in ["rock", "paper", "scissors"]:
            Ramu = input("Invalid input. Enter a choice (rock, paper, scissors): ").lower()

        choices = ["rock", "paper", "scissors"]
        Raju = random.choice(choices)
        print(f"\nRamu {Ramu}, Raju {Raju}.\n")

        if Ramu  ==  Raju :
            print(f"Both players selected {Ramu}. ooh Both are Equal!")
        elif Ramu == "rock":
            if Raju == "scissors":
                print("Rock smashes scissors! Ramu wins!")
            else:
                print("Paper covers rock! Raju wins.")
        elif Ramu  == "paper":
            if  Raju == "rock":
                print("Paper covers rock! Ramu wins!")
            else:
                print("Scissors cuts paper! Raju wins.")
        elif Ramu == "scissors":
            if Raju== "paper":
                print("Scissors cuts paper! Ramu wins!")
            else:
                print("Rock smashes scissors! Raju wins.")

        play_again = input("Play again? (yes/no): ").lower()
        while play_again not in ["yes", "no"]:
            play_again = input("Invalid input. Play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    game()
