import random

cicle = true

while cicle == true:

	random_number = random.randrange(0, 20)

	guess = int(input("What's your guess?"))

	if guess == random_number:

		print("You hit the right answer!")

	else if guess < random_number:

		ans = input("Your guess was too low, do you want to retry?: Press Y for another try or press any other key to quit.")

		if ans == Y or ans == y:

			cicle = true

		else:

			cicle = false

	else:

                ans = input("Your guess was too high, do you want to retry?: Pre>

                if ans == Y or ans == y:

                        cicle = true

                else:

                        cicle = false


return
