'''
TODAYS DATE: 
March 23rd, 2022

'''

# The array of numbers used to check the input
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# The function for the prime number checker with the input of the user
def prime_checker(number):
# Starts of True
  prime_number = True
  # Checks if the user entered the number 1
  if number == 1:
      # If they did then it's not a prime number and can end the program
    return print("It's not a prime number")
    # A for loop to run through all the tests
  for primer in numbers:
      # If the number module the array of numbers is equal to 0 that means that it divided with no issues AND also check if it's not equal to the same number as the user
      # input
    if number % primer == 0 and number != primer:
        # If this statement is true, then it's not a prime number
        # Set the prime_number variable to False
      prime_number = False
# Checking to see if the if statement changed the value of the variable
  if prime_number is not False:
      # If it did not then it is in fact a prime number
    print("It's a prime number")
    # If it did change it then it's not a prime number
  else:
      # Tell the user that it's not a prime number
    print("It's not a prime number")

# Getting input from the user
n = int(input("Check this number: "))
# Calling the prime number checker function
prime_checker(number=n)

