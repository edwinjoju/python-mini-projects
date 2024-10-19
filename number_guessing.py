#random library
import random

system_no = random.randint(1,10) #gives random number from 1 to 10
print("enter a number from 1 to 10 ")
count=0
while True: # executes until breaks
    count+=1
    try:
        user_no = int(input(">")) #gets user's no.
    except ValueError as e:
        print("please enter a valid number.")
        continue

    if user_no > system_no: 
        print("guess lower...")
    elif user_no < system_no:
        print("guess higher...")
    else:
        print("you guessed right!")
        print(f'You had {count} guesses')
        break