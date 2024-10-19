def get_input(word):
    name = input(f'Enter a {word} : ')
    return name

print("#########################")
print("## WELCOME TO MAD LIBS ##")
print("#########################\n")
noun_1 = get_input("noun")
noun_2 = get_input("noun")
verb_1 = get_input("verb")
verb_2 = get_input("verb")

print(f'''
    Once upon a time, there was a {noun_1} who loved to {verb_1}. Every day, the {noun_1} would go to the {noun_2} and {verb_2} all day long.
       It was a happy life for the {noun_1}. ''')