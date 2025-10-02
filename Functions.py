#Function to perform addition of two numbers
def add(number1, number2): 
    return (number1 + number2) 
  
#Function to perform subtraction of two numbers
def subtract(number1, number2): 
    return (number1 - number2)
  
#Function to perform multiplication of two numbers 
def multiply(number1, number2): 
    return (number1 * number2) 
  
#Function to perform division of two numbers 
def divide(number1, number2): 
    return (number1 / number2)

#Function to perform modulus remainder
def mod(number1, number2):
    return (number1 % number2)

#Function too perform x to the y power
def exponent(number1, number2):
    ans = 1
    for _ in range(0,number2):
        ans *= number1
    return ans

#Function to perform factorial
def factorial(number):
    ans = 1
    if number < 0:
        ans = number
        print("Please enter a non-negative number")
        return
    elif number == 0:
        for i in range(1, number + 1):
            ans = ans * i
        print(f"The factorial of 0 is {ans}")
    else:
        for i in range(1, number + 1):
            ans = ans * i
        print(f"The factorial of {number} is {ans}")
    return ans