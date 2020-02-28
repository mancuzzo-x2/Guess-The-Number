import random

cicle = True

random_number = random.randrange(0, 20)

while cicle == True:

        guess = int(input("\nGuess a number between 0 and 20: "))

        if guess == random_number:

                print("\nYou hit the right answer!\n")

                ans = input("\nDo you want to retry?: Press Y for another try or press any other key to quit: ")

                if ans == 'Y' or ans == 'y':

                        cicle = True

                        random_number = random.randrange(0, 20)

                else:

                        cicle = False
                

        elif guess < random_number:

                ans = input("\nYour guess was too low, do you want to retry?: Press Y for another try or press any other key to quit: ")

                if ans == 'Y' or ans == 'y':

                        cicle = True

                else:

                        cicle = False

        elif guess > random_number:

                ans = input("\nYour guess was too high, do you want to retry?: Press Y if you want to make another guess, or press any other key to quit: ")

                if ans == 'Y' or ans == 'y':

                        cicle = True

                else:

                        cicle = False
