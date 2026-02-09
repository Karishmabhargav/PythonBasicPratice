'''Snake Water Gun Game
Snake vs Water = Snake wins
Water vs Gun = Water wins
Gun vs Snake = Gun wins
s=Snake
w=Water
g=Gun'''
import random
print("Welcome to the Snake Water Gun Game")
print("Enter s for Snake, w for Water and g for Gun")
print("if you want to quit the game, enter q")
items=['s','w','g']
while True:
    Computer=random.choice(items)
    user_input=input("Enter your choice: ")
    if user_input not in ['s','w','g','q']:
        print("Invalid input, please try again")
        continue
    if user_input=='q':
        print("Thanks for playing!")
        break
    if user_input==Computer:
        print("It's a tie")
    elif user_input=='s' and Computer=='w':   
        print("You win!")
    elif user_input=='w' and Computer=='g':
        print("You win!")
    elif user_input=='g' and Computer=='s':
        print("You win!")
    else:
        print("Computer chose", Computer)
        print("Computer wins!")
