from random import randint

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
	print("Your goal is to guess 3 random numbers between 1 and 5. You will receive two clues to the numbers.\nYou have 3 attempts before you lose the game.\n")

	while True:
		a = randint(1, 5)
		b = randint(1, 5)
		c = randint(1, 5)
		random_sum = a + b + c
		random_product = a * b * c


		print(f"Clue 1: The sum of the numbers is {random_sum}")
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
			score += 1
			print(f"Score: {score}\n")
		else:
			print("\nYOU LOSE!")
			attempts -= 1
			if attempts == 0:
				break
			else:
				print(f"Attempts remaining: {attempts}\n")

main()