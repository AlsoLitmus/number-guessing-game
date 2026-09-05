# Python number guessing game
import random

def check_if_integer(user_input):
  if isinstance(user_input):
    return
  else:
    print("You did not enter a number from 1 to 10.")
    number = input("Try again: ")
    return


number = input("Guess a number from 1 to 10: ")

# Check if user input is an integer.


# Generate a random number.
random_integer = random.randint(1, 10)

while number != random_integer:
  if number < random_integer:
    number = input("The number is too low! Guess again: ")
  else if number > random_integer:
    number = input("The number is too high! Guess again: ")
  else if number == random_integer:
    print("You have guessed the number correctly!")
  
