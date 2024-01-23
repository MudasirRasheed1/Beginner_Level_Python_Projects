from random import choice
from sys import exit

class RockPaper:
    def __init__(self):
        self.moves_dict = {'rock':'🪨', 'paper':'📜', 'scissors':'✂️', 'lizard':'🦎', 'spock':'🦾'}
        print('\nWelcome to this game of Rock, Paper, Scissors, Lizard and Spock\nYou can quit at any time by typing "quit"')
        print("In this game computer will choose a move then you will choose a move, you will win if your move beats the computer's move,\n otherwise you will lose")
        self.moves = list(self.moves_dict.keys())
    def play(self):
        user_move = input('\nEnter your move: ').lower()
        if user_move == 'quit':
            exit()
        if user_move not in self.moves:
            print('\nInvalid move')
            return self.play()
        computer_move = choice(self.moves)

        if user_move == computer_move:
            print('\n\nYou and the computer both chose', self.moves_dict[user_move])
            print('Tie')
        elif user_move == 'rock':
            if computer_move == 'scissors' or computer_move == 'lizard':
                print(f"\n\nComputer's move {self.moves_dict[computer_move]}")
                print(f"Your move {self.moves_dict[user_move]}")
                print('You win')
            else:
                print(f"\n\nComputer's move {self.moves_dict[computer_move]}")
                print(f"Your move {self.moves_dict[user_move]}")
                print('You lose')
        elif user_move == 'paper':
            if computer_move == 'rock' or computer_move == 'spock':
                print(f"\n\nComputer's move {self.moves_dict[computer_move]}")
                print(f"Your move {self.moves_dict[user_move]}")
                print('You win')
            else:
                print(f"\n\nComputer's move {self.moves_dict[computer_move]}")
                print(f"Your move {self.moves_dict[user_move]}")
                print('You lose')
        elif user_move == 'scissors':
            if computer_move == 'paper' or computer_move == 'lizard':
                print(f"\n\nComputer's move {self.moves_dict[computer_move]}")
                print(f"Your move {self.moves_dict[user_move]}")
                print('You win')
            else:
                print(f"\n\nComputer's move {self.moves_dict[computer_move]}")
                print(f"Your move {self.moves_dict[user_move]}")
                print('You lose')
        elif user_move == 'lizard':
            if computer_move == 'paper' or computer_move == 'spock':
                print(f"\n\nComputer's move {self.moves_dict[computer_move]}")
                print(f"Your move {self.moves_dict[user_move]}")
                print('You win')
            else:
                print(f"\n\nComputer's move {self.moves_dict[computer_move]}")
                print(f"Your move {self.moves_dict[user_move]}")
                print('You lose')
        elif user_move == 'spock':
            if computer_move == 'rock' or computer_move == 'scissors':
                print(f"\n\nComputer's move {self.moves_dict[computer_move]}")
                print(f"Your move {self.moves_dict[user_move]}")
                print('You win')
            else:
                print(f"\n\nComputer's move {self.moves_dict[computer_move]}")
                print(f"Your move {self.moves_dict[user_move]}")
                print('You lose')

object = RockPaper()
while True:
    object.play()
            
            