import math

class Calculator:
    """
    A simple calculator that can perform various mathematical operations.
    
    Methods
    -------
    add(x, y):
        Adds two numbers and returns the result.
        
    subtract(x, y):
        Subtracts the second number from the first number and returns the result.
        
    multiply(x, y):
        Multiplies two numbers and returns the result.
        
    divide(x, y):
        Divides the first number by the second number and returns the result. If the second number is zero, returns None.
        
    power(x, y):
        Raises the first number to the power of the second number and returns the result.
        
    square_root(x):
        Calculates the square root of the number and returns the result. If the number is negative, returns None.
        
    logarithm(x, base):
        Calculates the logarithm of the number with the given base and returns the result. If the number is negative or the base is invalid, returns None.
        
    factorial(x):
        Calculates the factorial of the number and returns the result. If the number is negative, returns None.
        
    fibonacci(n):
        Generates the n-th number in the Fibonacci sequence and returns the result. If n is negative, returns None.
    """

    def add(self, x, y):
        """Add two numbers and return the result."""
        return x + y

    def subtract(self, x, y):
        """Subtract the second number from the first number and return the result."""
        return x - y

    def multiply(self, x, y):
        """Multiply two numbers and return the result."""
        return x * y

    def divide(self, x, y):
        """
        Divide the first number by the second number and return the result.
        If the second number is zero, returns None.
        """
        try:
            return x / y
        except ZeroDivisionError:
            print("Error: division by zero")
            return None

    def power(self, x, y):
        """Raise the first number to the power of the second number and return the result."""
        return x ** y

    def square_root(self, x):
        """
        Calculate the square root of the number and return the result.
        If the number is negative, returns None.
        """
        try:
            return x ** 0.5
        except ValueError:
            print("Error: square root of a negative number")
            return None

    def logarithm(self, x, base):
        """
        Calculate the logarithm of the number with the given base and return the result.
        If the number is negative or the base is invalid, returns None.
        """
        try:
            return math.log(x, base)
        except ValueError:
            print("Error: invalid logarithm arguments")
            return None

    def factorial(self, x):
        """
        Calculate the factorial of the number and return the result.
        If the number is negative, returns None.
        """
        if x < 0:
            print("Error: factorial of a negative number")
            return None
        elif x == 0:
            return 1
        else:
            return x * self.factorial(x-1)

    def fibonacci(self, n):
        """
        Generate the n-th number in the Fibonacci sequence and return the result.
        If n is negative, returns None.
        """
        if n < 0:
            print("Error: fibonacci sequence index cannot be negative")
            return None
        elif n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)
