import random

class GTNum:

	def __init__(self, range = 20, guess = 0):

		self.range = range
		self.guess = guess

	def Set_range(self):

		self.range = input("Insert an integer >= 0: ")

	def Set_guess(self):

		self.guess = input("\nGuess a number between 0 and " + str(self.range) + ": ")

	def Get_guess(self):

		return self.guess

	def Get_range(self):

		return self.range

	def GTC(self):

		rn = random.randrange(0, self.range)

		if self.guess == rn:

			return 0

		elif self.guess < rn:

			return -1

		else:

			return 1

	def GTN(self):

		print("Define a range from 0 to N.")

		self.Set_range()
		self.Set_guess()

		range = self.Get_range()
		guess = self.Get_guess()

		while True:

			compare = self.GTC()

	        	if compare == 0:

        	        	print("\nYou hit the right answer!\n")
				ans = raw_input("\nDo you want to retry?\nPress Y for yes or N for no: ")

				if ans == "Y" or ans == "y":

					guess = self.Set_guess()
					continue

				else:

					break

	        	elif compare == -1:

	                	print("\nYour guess was too low...")
				ans = raw_input("\nDo you want to retry?\nPress Y for yes or N for no: ")

                                if ans == "Y" or ans == "y":

                                        guess = self.Set_guess()
                                        continue 

                                else:

                                        break

        		else:

                		print("\nYour guess was too high...")
				ans = raw_input("\nDo you want to retry?\nPress Y for yes or N for no: ")

                                if ans == "Y" or  ans == "y":

                                        guess = self.Set_guess()
                                        continue 

                                else:

                                        break

		return;


x = GTNum()
x.GTN()
