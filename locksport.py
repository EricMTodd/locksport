#########################
#       Locksport       #
# Author: Eric M. Todd  #
# Last updated: 2/5/26  #
#########################

# Python Standard Library
from random import randint

# Modules
from user import User

class Locksport:
    """Primary class for game engine."""

    def __init__(self):
        """Initialize engine attributes."""
        self.user = None
        self.difficulty = None
        self.random_code = []
        self.clues = {}

    def set_user(self):
        """Sets the current user for this session"""
        self.user = User()

    def set_difficulty(self):
        """Sets the difficulty for this session"""
        while True:
            difficulty_input = input("Enter a number from 1 to 5: ")
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

    def play_game(self):
        """Core gameplay loop."""

        # Perform intial setup
        self.set_difficulty()
        self.generate_random_code()
        self.set_clues()

        # Provide clues to the user
        print(
            "\nYour goal is to guess a randomly generated three digit code."
            "\nYour only clues are the sum and the product of the three numbers."
            f"\nSum: {self.clues['sum']}"
            f"\nProduct: {self.clues['product']}"
            )


Locksport().play_game()