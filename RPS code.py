from random import randint

yes = [
    "y", "yes"]
no = [
    "n", "no"]
rock = [
    "rock", "r"]
paper = [
    "paper", "p"]
scissors = [
    "scissors", "s"]

rps = ["Rock", "Paper", "Scissors"]


def main():

    comp_turn = rps[randint(0, 2)]
    user_turn = False

    while not user_turn:

        user_turn = str.lower(input("\nRock, paper or scissors? "))
        if user_turn in rock and comp_turn in rock:
            print("Rock against rock. It's a tie!")
        elif user_turn in rock and comp_turn in scissors:
            print("Rock smashes scissors. You win!")
        elif user_turn in rock and comp_turn in paper:
            print("Paper covers rock. You lose!")

        elif user_turn in scissors and comp_turn in scissors:
            print("Scissors against scissors. It's a tie!")
        elif user_turn in scissors and comp_turn in rock:
            print("Rock smashes scissors. You lose!")
        elif user_turn in scissors and comp_turn in paper:
            print("Scissors cuts paper. You win!")

        elif user_turn in paper and comp_turn in paper:
            print("Paper against paper. It's a tie!")
        elif user_turn in paper and comp_turn in scissors:
            print("Scissors cuts paper. You lose!")
        elif user_turn in paper and comp_turn in rock:
            print("Paper covers rock. You win!")
        else:
            print("Invalid play. Check your spelling!")

        user_turn = False
        comp_turn = rps[randint(0, 2)]


start = input("Hello there! Press 'y' to start, or 'n' to stop. ")
if start.lower() in ["y", "yes"]:
    main()
elif start.lower() in ["n", "no"]:
    print("Hope you can play some other time!")
