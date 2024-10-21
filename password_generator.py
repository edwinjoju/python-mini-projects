import string
import secrets

#check uppercase
def check_upper(password):
    for char in password:
        if char.isupper():
            return True
    return False

#check symbols
def check_symbol(password):
    for char in password:
        if char in string.punctuation:
            return True
    return False

def generate_password(length,upper,symbol):

    combination = string.ascii_lowercase+string.digits # combination contain a to z & 0 to 9

    if upper: #if upper is true adds uppercase to combination
        combination+=string.ascii_uppercase

    if symbol:#if symbol is true adds symbols to combination
        combination+=string.punctuation

    combination_length=len(combination)

    new_password=''

    for x in range(length): #randomly takes value from combination and adds to new_password
        new_password+=combination[secrets.randbelow(combination_length)]

    return new_password

if __name__=='__main__':
    for x in range(6):
        password = generate_password(5,symbol=True, upper=True)
        print(f'{password} | Upper:{check_upper(password)} | Symbol:{check_symbol(password)}')