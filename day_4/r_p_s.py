import random
choice = ["rock", "paper", "scissors"]
user = input("Enter choice: ")
if user not in choice :
    user = input("Invalid choice! choose again: ")
computer = random.choice(choice)

if user == computer :
    print("It's a tie!")
elif user == "rock" :
    if computer == "paper" :
        print("You lose!")
    else :
        print("You win!")
elif user == "paper" :
    if computer == "rock" :
        print("You win!")
    else :
        print("You lose!")
elif user == "scissors" :
    if computer == "rock" :
        print("You lose!")
    else :
        print("You win!")

print(f"Your choice {user}, computer choose {computer}")
'''
p1,p2="rock","scissors"
if p1==p2:
    print("It's a tie!")
elif (p1=="rock" and p2=="scissors") or (p1=="scissors" and p2=="paper") or (p1=="paper" and p2=="rock"):
    print("Player 1 wins!")
else:
    print("Player 2 wins!")
    '''

