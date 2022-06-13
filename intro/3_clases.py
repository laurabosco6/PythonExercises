"""
    Created on Sun Jun 12 14:32:29 2022
    @author: Laura Bosco Romero
    
    This file is part of my Python from scratch notes.
    Here I learn to create classes with parameters and functions.
"""


class Person:
    """ Person class definition """
  
    def __init__(self, name, age, telephones, email1, email2):
        self.name = name
        self.age = age
        self.telephones = telephones
        self.emails = dict()
        self.emails['personal'] = email1
        self.emails['work'] = email2

    def __str__(self):
        return self.name

    # Can be used with any of these functions
    # https://docs.python.org/3/library/functions.html
    
    def __len__(self):
        return len(self.name)
    
    def __getitem__(self, key):
        # return self.telefonos[key]
        return self.emails[key]


""" Using the Person class """
# Creating a person using the class
p = Person("Ana", 20, ["222", "333"], "personalvalue", "workvalue")

# This is how we show the person
print("Person:")
print(p)

# This commented print is for the commented getitem
# print(p[1])

# This is how we show the personal number
print("\n")
print("Personal number:")
print(p['personal'])

# This is how we show the length of the person's name
print("\n")
print("Length of person's name:")
print(len(p))


class Fraction():
    """ Class to represent fractions """
    
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)
    
    def add(self, f2):
        result = Fraction(1, 1)
        result.numerator = self.numerator * f2.denominator +  f2.numerator * self.denominator
        result.denominator = self.denominator * f2.denominator
        return result


""" Using the Fraction class """
f1 = Fraction(2, 3)
f2 = Fraction(1, 4)
r = f1.add(f2)

print("\n")
print("Result of adding fractions:")
print(r)

