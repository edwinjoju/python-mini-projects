import string
import secrets

def check_upper(password):
    for char in password:
        if char.isupper():
            return True
    return False

def check_symbol(password):
    for char in password:
        if char in string.punctuation:
            return True
    return False

def generate_password(length,symbol,uppercase):
    combination =string.ascii_lowercase+string.digits

    if symbol:
        combination+=string.punctuation
    
    if uppercase:
        combination+=string.ascii_uppercase

    combination_length = len(combination)
    new_password=''

    for x in range(length):
        new_password+=combination[secrets.randbelow(combination_length)]
    
    return new_password

if __name__ == '__main__':
    for x in range(6):
        password = generate_password(length=5,symbol=True,uppercase=True)
        print(f'{password} | uppercase: {check_upper(password)} | symbol: {check_symbol(password)}')