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

#Function to perform square root
def square_root(number):
    try:
        x = float(number)
    except ValueError:
        print("That isn’t a valid number.")
        raise SystemExit

    if x < 0:
        print("Cannot take the square root of a negative number (real domain).")
        raise SystemExit

    if x == 0 or x == 1:
        print(f"√{x} = {float(x)}")
        raise SystemExit

    # Newton‑Raphson iteration.
    # guess starts at x/2 (a decent generic starting point)
    # stop when the change between successive guesses is < tolerance
    # max_iter protects us from an infinite loop in pathological cases
    tolerance = 1e-12
    max_iter   = 100

    guess = x / 2.0
    iteration = 0

    while iteration < max_iter:
        next_guess = (guess + x / guess) / 2.0   # g_{n+1} = (g_n + x/g_n)/2
        if abs(next_guess - guess) < tolerance:
            guess = next_guess
            break
        guess = next_guess
        iteration += 1
    
    if iteration == max_iter:
    # We didn’t reach the tolerance, but we still have a usable approximation.
        print(f"Reached max iterations ({max_iter}). Approximation may be rough.")
    print(f"√{x} ≈ {guess}")