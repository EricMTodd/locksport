# Python Standard Library
from random import randint

# Modules
from user import User

class Locksport:
    """Primary class for game engine."""

    def __init__(self):
        """Initialize engine attributes."""
        self.rules = (
            "\n---LOCKSPORT---"
            "\nWelcome to Locksport!"
            "\nYou have three attempts to guess a three digit code."
            "\nYou will be provided two clues:"
            "\nthe sum and product of the digits."
            )
        self.user = None
        self.difficulty = 0
        self.random_code = []
        self.clues = {}

    def set_difficulty(self):
        """Sets the difficulty for this session"""
        while True:
            difficulty_input = input(
                "\n---SET DIFFICULTY---"
                "\nThis will determine the upper bound of possible integers."
                "\nThis number will also determine the amount points"
                "\nyou get for guessing the correct code!"
                "\nEnter a number from 1 to 5: "
                )
            if difficulty_input.isdigit():
                difficulty_integer = int(difficulty_input)
                if 1 <= difficulty_integer <=5:
                    self.difficulty = difficulty_integer
                    break

    def generate_random_code(self):
        """Generates a random code for the current loop."""
        random_code = []
        while len(random_code) < 3:
            random_code.append(randint(1, self.difficulty + 4))
        self.random_code = random_code

    def set_clues(self):
        """Sets the necessary clues to guess the code."""
        clues = {
            'sum': 0,
            'product': 1
            }
        for x in self.random_code:
            clues['sum'] += x
            clues['product'] *= x
        self.clues = clues

    def evaluate_score(self):
        """Evaluates the users guesses against the clues to the code."""
        for x in self.user.guesses:
            self.user.guess_values['sum'] += x
            self.user.guess_values['product'] *= x
        if self.user.guess_values['sum'] == self.clues['sum'] and self.user.guess_values['product'] == self.clues['product']:
            print("\nYou win!")
            self.user.score += self.difficulty
            print(f"Score: {self.user.score}")
        else:
            print("\nYou lose!")
            self.user.attempts_remaining -= 1
            print(f"Attempts remaining: {self.user.attempts_remaining}")
        self.user.guesses = []
        self.user.guess_values = {
            'sum': 0,
            'product': 1
            }

    def play_game(self):
        """Core gameplay loop."""
        print(self.rules)
        self.user = User(self)
        self.set_difficulty()
        while True:
            self.generate_random_code()
            self.set_clues()
            print(
                "\nClues:"
                f"\n1) Sum: {self.clues['sum']}"
                f"\n2) Product: {self.clues['product']}"
                )
            self.user.guess_code()
            self.evaluate_score()
            if self.user.attempts_remaining == 0:
                print("\n---GAME OVER---")
                print(f"\nFinal score: {self.user.score}")
                break
