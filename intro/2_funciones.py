"""
    Created on Sun Jun 12 14:17:32 2022
    @author: Laura Bosco Romero
    
    This file is part of my Python from scratch notes.
    Here I learn to create functions.
"""


def factorial(n):
    """
        Calculate the factorial of a number and shows an
        error message if n is negative
        
        Args:
            n
    """
    
    try:
        n = int(n)
    except:
        print ("The argument has to be a number")
        return

    if( n < 0):
         print ("The number cannot be negative")
         return
    result = 1
    for num in range(2, n + 1):
        result = result * num
    return result


def isPrime(n):
    """
        Returns True if n is prime, False if it is not.
        
        Args:
            n
    """
    
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True


""" Using the functions """
print("Factorial of number 4:")
print(factorial(4))

print("\n")
print("Is 13 a prime number?")
print(isPrime(13))

     
     
     
     
     
     