import random

cicle = True

while cicle == True:

        random_number = random.randrange(0, 20)

        guess = int(input("What's your guess?"))

        if guess == random_number:

                print("You hit the right answer!")

        elif guess < random_number:

                ans = input("Your guess was too low, do you want to retry?: Press Y for another try or press any other key to quit.")

                if ans == Y or ans == y:

                        cicle = True

                else:

                        cicle = False

        elif guess > random_number:

                ans = input("Your guess was too high, do you want to retry?: Press Y if you want to make another guess, or press any other key to quit.")

                if ans == Y or ans == y:

                        cicle = True

                else:

                        cicle = False
