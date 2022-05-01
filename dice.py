import random

min = 1
max = 6

roll_input = input("Roll? yes or no: ")
roll = "yes"

while roll == "yes" or roll == "y":
    print("Rolling The Dices...")
    print("The Values are :")
    
    print(random.randint(min, max))
    
    print(random.randint(min, max))
    
    roll = input("Roll the Dices Again? ") 
