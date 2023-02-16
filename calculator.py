"""
Calculator library containing basic math operations.
"""
import sys
#functions
def add(first_term, second_term):
 	return first_term + second_term
 
def subtract(first_term, second_term):
  return first_term - second_term

# Read user's choice
choice = sys.argv[1]

# Read input numbers
num1 = float(sys.argv[2])
num2 = float(sys.argv[3])

# Check user's choice and perform the corresponding operation
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

else:
   print("Invalid input")
