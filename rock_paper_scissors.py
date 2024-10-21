import random
class RPS():
    def __init__(self):
        print("Welcome to RPS 9000!!")

        self.moves = {'rock':'🪨','paper':'📃','scissors':'✂️'}
        self.valid_moves = list(self.moves.keys())

    def play_game(self):
        user_move = input("rock | paper | scissors : ").lower()
        system_move = random.choice(self.valid_moves)

        if user_move == 'exit':
            print("thanks for playing...")
            exit()
        
        if user_move not in self.valid_moves:
            print("invlaid move")
            return self.play_game()
        
        self.display_game(user_move,system_move)
        self.check_game(user_move,system_move)
        
    def display_game(self,user_move,system_move):
        print("******")
        print(f'User : {self.moves[user_move]}')
        print(f'System: {self.moves[system_move]}')
        print("******")

    def check_game(self,user_move,system_move):
        if user_move == system_move:
            print("it's a tie")
        elif user_move == 'rock' and system_move == 'scissors':
            print("User wins")
        elif user_move =='scissors' and system_move == 'paper':
            print("User wins")
        elif user_move == 'paper' and system_move == 'rock':
            print("user wins")
        else:
            print("System Wins")

if __name__ == '__main__':
    rps = RPS()

    while True:
        rps.play_game()