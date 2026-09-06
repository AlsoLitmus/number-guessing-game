# Python number guessing game
import random

# This number will recieve user input and assign it to number.
def grab_user_input(number):
  number = input("Guess a number from 1 to 10: ")
  return number

def check_if_in_range(num):
  if int(num) > -1 and int(num) < 11:
    return num
  else:
    while int(num) < 0 or int(num) > 11:
      print("The guessed number is out of range. Guess again.")
      num = grab_user_input(num)
    return num

def convert_to_integer(num):
  try:
    num = int(num)
  except ValueError:
    print("You did not enter an integer. Try again.")
    num = grab_user_input(num)
  return num

number = ""
number = grab_user_input(number)
number = check_if_in_range(number)

# Generate a random number.
random_integer = random.randint(1, 10)

# Check if the number guessed is greater than, less than, or equal to random_integer.
while number != int(random_integer):
  number = convert_to_integer(number)
  if int(number) < random_integer:
    number = input("The number is too low! Guess again: ")
    number = convert_to_integer(number)
    number = check_if_in_range(number)
  elif number > int(random_integer):
    number = input("The number is too high! Guess again: ")
    number = convert_to_integer(number)
    number = check_if_in_range(number)

if number == int(random_integer):
  print("You have guessed the number correctly!")
  
  
