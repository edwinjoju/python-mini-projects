#random library
import random

print("####################################\n")
print("## Welcome to Number Guessing game ##")
print("\n####################################")

system_no = random.randint(1,10) #gives random number from 1 to 10
print("enter a number from 1 to 10 ")

count=0
while True: # executes until breaks
    print(f' {4-count} guesses left')
    if count>3:
        print("sorry...guess are over")
        print('''
__   __            _           _   
\ \ / /           | |         | |  
 \ V /___  _   _  | | ___  ___| |_ 
  \ // _ \| | | | | |/ _ \/ __| __|
  | | (_) | |_| | | | (_) \__ \ |_ 
  \_/\___/ \__,_| |_|\___/|___/\__|                              

        ''')
        break
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
        print(f''' 
__   __            _    _             _ 
\ \ / /           | |  | |           | |
 \ V /___  _   _  | |  | | ___  _ __ | |
  \ // _ \| | | | | |/\| |/ _ \| '_ \| |
  | | (_) | |_| | \  /\  / (_) | | | |_|
  \_/\___/ \__,_|  \/  \/ \___/|_| |_(_)

        ''')
        print(f'You had {count} guesses')
        break

print("%%%%%%%%%%%%%%%%%%%%%%%")
print("Thank you for playing")
print("%%%%%%%%%%%%%%%%%%%%%%%")