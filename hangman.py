from random import choice

def play():
    
    magical_words = choice(["love","faith","hope","luck","demon"])
    guesses = ''
    tries=3

    username = input("Enter player name: ")
    print(f'Welcome {username}, to hangman')

    while tries > 0:
        blanks=0
        for letter in magical_words:
            if letter in guesses:
                print(letter,end='')
            else:
                print("_",end='')
                blanks+=1
        print()

        if blanks == 0:
            print("YOU WON!!")
            break

        guess = input("enter your letter:")
        guesses+=guess

        if guess not in magical_words:
            tries-=1
            print(f'You have {tries} tries left')
        
        if tries==0:
            print("GAME OVER!!")
            break

play()


