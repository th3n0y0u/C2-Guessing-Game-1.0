import random

# Have the computer choose a random number 
number = random.randint(1,10)
# Prompt the user to guess and store their guess in a variable 
guess = int(input("Please input a number between 1-10: "))
# Conditional statements to compare the two numbers
while(number != guess):
  if(number > guess):
      print("Your number is too low!")
  if(number < guess):
      print("Your number is too high!") 
  guess = int(input("Try again: ")) 

print("You have guessed correctly!")