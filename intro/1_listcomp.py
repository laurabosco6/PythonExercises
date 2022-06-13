"""
    Created on Sun Jun 12 15:08:45 2022
    @author: Laura Bosco Romero
    
    This file is part of my Python from scratch notes.
    Here I learn list comprehension.
"""


# Creating two different lists
a = [1, 2, 3]
b = [2, 4, 5]

# Creating a new list with the squared numbers of the 'a' list:
aSquared = [x*x for x in a]

print("Squared numbers of 'a' list:")
print(aSquared)

# Creating a new list with the result of adding the two lists:
sum = [x + y for x,y in zip(a,b)]

print("\n")
print("Result of adding squares:")
print(sum)
