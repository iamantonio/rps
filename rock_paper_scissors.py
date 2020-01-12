# Rock Paper Scissors game by Antonio Vargas

# !/usr/bin/env python3

import random
import time

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']
opp_move = []
"""The Player class is the parent class for all of the Players
in this game"""


# A player that always plays 'rock'
class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        print(f"{Player.__name__}: {my_move}")


# A human player
class HumanPlayer(Player):
    def move(self):
        while True:
            string = input(f"Your move, type "
                           f"'Rock', "
                           f"'Paper, "
                           f"or 'Scissors  :> ")
            if string.lower() not in ('rock', 'paper', 'scissors'):
                print(f"Please enter the correct move!")
            else:
                break
        return string

    def learn(self, my_move, their_move):
        print(f"{HumanPlayer.__name__}: {my_move}")


# A player that chooses its moves randomly.
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        print(f"{RandomPlayer.__name__}: {my_move}")


# A player that cycles through the three moves
class ThreeMoves(Player):
    def move(self):
        return moves[Game.position]

    def learn(self, my_move, their_move):
        print(f"{ThreeMoves.__name__}: {my_move}")


class CopyCat(Player):
    def move(self):
        if not opp_move:
            return random.choice(moves)
        else:
            print(opp_move[0])
            return opp_move[0]

    def learn(self, my_move, their_move):
        # print("This method got called!")
        opp_move.insert(0, their_move)
        print(f"{CopyCat.__name__}: {my_move}")


def beats(one, two):
    if one in two:
        return "Tie"
    else:
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))


class Game:
    # Iterator to help with the subclass ThreeMoves cycle through moves.
    position = -1

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

        # I want to make sure that the user enters
        # an integer for the number of rounds.
        while True:
            try:
                self.rounds = int(input
                                  (f"How many rounds do you want to play?: "))
            # If user enters anything but an integer make user try again.
            except ValueError:
                print("Sorry, it must be a number!")
                continue

            # If user tries to enter a negative number, have user try again.
            if self.rounds < 0:
                print(f"Sorry, your must pick a positive number!")
                continue

            # User enter correct response!
            else:
                break

    def play_round(self):
        # This loop helps reset the game iterator
        # when playing more than 3 rounds.
        if Game.position > 1:
            Game.position = -1  # Resets the iterator
        Game.position += 1  # Increase iterator by 1
        move1 = self.p1.move()
        move2 = self.p2.move()
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.keep_score(move1, move2)
        print(f"Current Score\n"
              f"Player 1: {self.p1_score}"
              f"Player 2: {self.p2_score}\n")
        time.sleep(.6)

    def play_game(self):
        print("\nGame start!")

        # Helps keep track of the number rounds played
        for game_round in range(self.rounds):
            print(f"Round {game_round + 1}:")
            self.play_round()
        winner = self.announce_winner()  # Runs to find out who the winner is.
        print(f"{winner}\n"
              f"Final score\n"
              f"Player 1: {self.p1_score}\n"
              f"Player 2: {self.p2_score}\n"
              f"Game over!\n")

    # Figures out who the winner is by comparing scores.
    def announce_winner(self):
        if self.p1_score == self.p2_score:
            return 'Tie Game!'
        elif self.p1_score > self.p2_score:
            return 'Player 1 WINS!'
        else:
            return 'Player 2 WINS!'

    # The game displays the results after each round,
    # including each player's score.
    # At the end, the final score is displayed.
    def keep_score(self, p1, p2):
        if beats(p1, p2) == "Tie":
            self.rounds += 1
            print(f"Tie!")
        elif beats(p1, p2):
            print(f"{p1.capitalize()} wins!")
            self.p1_score += 1
        else:
            print(f"{p2.capitalize()} wins!")
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
        while True:
            try:
                select_opponent = int(input("Who do you want to"
                                            "play against?\n"
                                            "1: RandomPlayer\n"
                                            "2: ThreeMoves\n"
                                            "3: AlwaysRock\n"
                                            "4: CopyCat\n"
                                            "5: Quit Game\n"
                                            "Your Choice: "))
            except ValueError:  # If user doesn't enter a integer
                print("You must pick a number.")
                continue
            # If user enters anything outside of 1 - 5
            if select_opponent < 0 or select_opponent > 5:
                print("Pick the correct numbered choice!")
                continue
            else:
                val = int(select_opponent)
                if val == 1:
                    game = Game(HumanPlayer(), RandomPlayer())
                    game.play_game()
                elif val == 2:
                    game = Game(HumanPlayer(), ThreeMoves())
                    game.play_game()
                elif val == 3:
                    game = Game(HumanPlayer(), Player())
                    game.play_game()
                elif val == 4:
                    game = Game(HumanPlayer(), CopyCat())
                    game.play_game()
                # Sends message if user quits the game
                else:
                    print("Thank you for playing!")
                    break

    else:
        game = Game(CopyCat(), ThreeMoves())
        game.play_game()
