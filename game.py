# Python number guessing game
import random

# Check if the user input is an integer.
def check_if_integer(user_input):
  if isinstance(user_input):
    return user_input
  else:
    while !isinstance(user_input):
      print("You did not enter an integer Try again.")
      user_input = grab_user_input(user_input)
    return user_input

# This number will recieve user input and assign it to number.
def grab_user_input(number):
  number = input("Guess a number from 1 to 10: ")
  return number

def check_if_in_range(num):
  if num > -1 and num < 11:
    return num
  else:
    while num < 0 or num > 11:
      print("The guessed number is out of range. Guess again.")
      num = grab_user_input(num)
    return num
  
number = grab_user_input(number)

# Check if user input is an integer.
number = check_if_integer(number)
number = check_if_in_range(number)

# Generate a random number.
random_integer = random.randint(1, 10)

# Check if the number guessed is greater than, less than, or equal to random_integer.
while number != random_integer:
  if number < random_integer:
    number = input("The number is too low! Guess again: ")
  else if number > random_integer:
    number = input("The number is too high! Guess again: ")
  
if number == random_integer:
  print("You have guessed the number correctly!")
  
  
