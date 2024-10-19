import random

def roll_dice(val):
    if val <= 0: #dice rolls cannot be less than 0
        raise ValueError
    
    rolls = []
    for i in range(val):
        rand_roll = random.randint(1,6)
        rolls.append(rand_roll) # inserting each roll value to roll list

    return rolls

def main():
    while True:
        try:
            user_input = input("enter how many dices to rolls:")
            if user_input.lower() == "exit":
                print("User exited the program")
                break
            dice_rolls = roll_dice(int(user_input)) # prints out dic rolls
            print(*dice_rolls, sep = "|") #
            print(f'The sum of the rolls is {sum(dice_rolls)}')# prints out sum of dice rolls

        except ValueError:
            print("Please enter valid number")
        
main()
