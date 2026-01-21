from random import randint

def select_difficulty():
    """Allows the player to select their desired difficulty."""
	print("Enter a number from 1 to 5. This will determine the upper bound of possible values in the numbers you have to guess. It will also determine the number of points you're assigned for correctly guessing the solution.\n")

	while True:
		difficulty = input("Select difficulty: ")
		if difficulty == "exit":
			return "exit"
		else:
			try:
				if int(difficulty) < 1 or int(difficulty) > 5:
					print("Please select a number from 1 to 5.\n")
				else:
					return int(difficulty) + 4
			except ValueError:
				print("Please enter an integer")

def get_x():
	"""Gets player input for the first guess."""
	while True:
		x = input("First number: ").strip()
		if x == "exit":
			return "exit"
		else:
			try:
				return int(x)
			except ValueError:
				print("Please enter an integer.")

def get_y():
	"""Gets player input for the second guess."""
	while True:
		y = input("Second number: ").strip()
		if y == "exit":
			return "exit"
		else:
			try:
				return int(y)
			except ValueError:
				print("Please enter an integer.")

def get_z():
	"""Gets player input for the third guess."""
	while True:
		z = input("Third number: ").strip()
		if z == "exit":
			return "exit"
		else:
			try:
				return int(z)
			except ValueError:
				print("Please enter an integer.")


def main():
	"""The Primary logic of the game."""
	score = 0
	attempts = 3
	print("Your goal is to guess 3 random numbers between 1 and 5. You will receive two clues to the numbers.\nYou have 3 attempts before you lose the game.\nEnter 'exit' at any time to quit the program.\n")

	difficulty = select_difficulty()
	if difficulty == "exit":
		return

	while True:
		a = randint(1, difficulty)
		b = randint(1, difficulty)
		c = randint(1, difficulty)
		random_sum = a + b + c
		random_product = a * b * c


		print(f"\nClue 1: The sum of the numbers is {random_sum}")
		print(f"Clue 2: The product of the numbers is {random_product}\n")


		x = get_x()
		if x == "exit":
			break
		y = get_y()
		if y == "exit":
			break
		z = get_z()
		if z == "exit":
			break
		guessed_sum = x + y + z
		guessed_product = x * y * z

		if random_sum == guessed_sum and random_product == guessed_product:
			print("\nYOU WIN!")
			score += difficulty - 4
			print(f"Score: {score}")
		else:
			print("\nYOU LOSE!")
			attempts -= 1
			if attempts == 0:
				break
			else:
				print(f"Attempts remaining: {attempts}\n")

main()