import random


def game():
    Player = input("Choose Rock, Paper or Scissor: ")
    Co = ["Rock", "Paper", "Scissor"]
    Computer = ''.join(random.choice(Co))
    print(f"Computer Choose: {Computer}")

    if Player == "Rock" and Computer == "Rock":
        print("Draw")

    elif Player == "Rock" and Computer == "Paper":
        print("Computer Win")

    elif Player == "Rock" and Computer == "Scissor":
        print("Player Win")

    elif Player == "Paper" and Computer == "Paper":
        print("Draw")

    elif Player == "Paper" and Computer == "Rock":
        print("Player Win")

    elif Player == "Paper" and Computer == "Scissor":
        print("Computer Win")

    elif Player == "Scissor" and Computer == "Paper":
        print("Player Win")

    elif Player == "Scissor" and Computer == "Rock":
        print("Computer Win")

    elif Player == "Scissor" and Computer == "Scissor":
        print("Draw")


game()

for _ in range(1000):
    game()
