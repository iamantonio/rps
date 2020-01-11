# Rock Paper Scissors game by Antonio Vargas
# The game has two players
# In a single round of the game, each player secretly chooses one of the three throws.
# Players reveal their moves at the same time.
# If both pick same throw, no winner
# Else rock beats scissors
# Else paper beats rock
# Else scissors beat paper
# Players can play a single round, or best of any number of rounds.

# !/usr/bin/env python3

import random
import time

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']
"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        while True:
            string = input(f"Your move, type 'Rock', 'Paper, or 'Scissors  :> ")
            if string.lower() not in ('rock', 'paper', 'scissors'):
                print(f"Please enter the correct move!")
            else:
                break
        return string

    def learn(self, my_move, their_move):
        # The game should call each player's move method once in each round, to get that player's move.
        # After each round, it should call the remembering method to tell each player what the other player's move was.
        opponent = their_move
        me = my_move

        print(f"My move: {me}\nOpponent Move: {opponent}")


# A player that always plays 'rock'
class Rock(Player):
    def move(self):
        return 'rock'


# A player that chooses its moves randomly.
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


# A player that cycles through the three moves
class ThreeMoves(Player):
    def move(self):
        return moves[Game.position]


def beats(one, two):
    if one in two:
        return "Tie"
    else:
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))


class Game:
    position = -1  # Iterator to help with the subclass ThreeMoves cycle through moves.

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

        # I want to make sure that the user enters an integer for the number of rounds.
        while True:
            try:
                self.rounds = int(input(f"How many rounds do you want to play?: "))
            except ValueError:  # If user enters anything but an integer make user try again.
                print("Sorry, it must be a number!")
                continue
            if self.rounds < 0:  # If user tries to enter a negative number, have user try again.
                print(f"Sorry, your must pick a positive number!")
                continue
            else:
                break  # User enter correct response!

    def play_round(self):
        # This loop helps reset the game iterator when playing more than 3 rounds.
        if Game.position > 1:
            Game.position = -1  # Resets the iterator
        Game.position += 1  # Increase iterator by 1
        move1 = self.p1.move()
        move2 = self.p2.move()
        self.p1.learn(move1, move2)
        self.keep_score(move1, move2)
        print(f"Current Score\nPlayer 1: {self.p1_score}   Player 2: {self.p2_score}\n")
        # self.p1.learn(move1, move2)
        # self.p2.learn(move2, move1)
        time.sleep(1)

    def play_game(self):
        print("\nGame start!")

        # Helps keep track of the number rounds played
        for game_round in range(self.rounds):
            print(f"Round {game_round + 1}:")
            self.play_round()
        winner = self.announce_winner()  # Runs to find out who the winner is.
        print(f"{winner} WINS!!\nFinal score\nPlayer 1: {self.p1_score}\nPlayer 2: {self.p2_score}\nGame over!")

    # Figures out who the winner is by comparing scores.
    def announce_winner(self):
        if self.p1_score > self.p2_score:
            return 'Player 1'
        else:
            return 'Player 2'

    # The game displays the results after each round, including each player's score.
    # At the end, the final score is displayed.
    def keep_score(self, p1, p2):
        if beats(p1, p2) == "Tie":
            self.rounds += 1
            print(f"Tie!")
        elif beats(p1, p2):
            print(f"{p1} wins!")
            self.p1_score += 1
        else:
            print(f"{p2} wins!")
            self.p2_score += 1


if __name__ == '__main__':
    # I want to make sure that the user enters the correct yes or no response.
    while True:
        play_game = input(f"Do you want to play?: ").lower()
        if play_game.lower() not in ('yes', 'no'):
            print("Please enter either yes or no.")
        else:
            break  # User enters the correct response and starts game.
    if play_game == 'yes':
        game = Game(Player(), RandomPlayer())
        game.play_game()
    else:
        game = Game(RandomPlayer(), RandomPlayer())
        game.play_game()
