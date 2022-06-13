"""
    Created on Sun Jun 12 15:25:16 2022
    @author: Laura Bosco Romero
    
    This file is part of my Python from scratch notes.
    Here I do some exercises with lists as a matrix.
"""


# Creating a matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8 ,9]]


def showMatrix(matrix):
    """
        Receives a list of integer lists, and displays it to see it more clearly.
        
        Args:
            matrix
    """
    for row in matrix:
        for elem in row:
            print(elem, end = " ")
        print()


""" Using the function showMatrix() """
print("Our matrix:")
showMatrix(matrix)

# This is how we show a row of the matrix
print("\n")
print("Third row of the matrix:")
print(matrix[2])

# This is how we show how many rows the matrix has
print("\n")
print("Number of rows:")
print(len(matrix))

# This is how we show how many columns the matrix has
print("\n")
print("Number of columns:")
print(len(matrix[0]))


def isMatrix(matrix) -> bool:
    """
        Receives a list of integer lists, and checks if it is valid as a matrix.
        It is valid if all rows have the same number of columns.
        
        Args:
            matrix
        
        Returns:
            bool
    """

    # It would be necessary to verify that position 0 exists
    length = len(matrix[0])
    for row in matrix:
        if(len(row) != length):
            return False
    
    return True


""" Using the function isMatrix() """
print("\n")
print("Is it a matrix?")
print(isMatrix(matrix))


def addMatrices(a, b):
    """
        Receives two matrices (represented as in the previous exercise) and
        return a new matrix with the sum. Before anything, checks that the matrices are
        valid and have the same dimension.
        
        Args:
            matrix
    """
    
    result = []
    
    # Checks if there is an empty matrix
    if(len(a) == 0 or len(b) ==0):
        raise Exception("One of the matrices is empty")
    
    # Checks if there is an invalid matrix
    if(not(isMatrix(a)) or not(isMatrix(b))):
        raise Exception("One of the matrices is invalid")
        
    # Checks that the two matrices have the same number of rows
    if (len(a)!= len(b)):
        raise Exception("The matrices do not have the same number of rows")
        
    # Checks that the two matrices have the same number of columns
    cola = len(a[0])
    colb = len(b[0])
    if (cola!= colb):
        raise Exception("The matrices do not have the same number of columns")
    
    # Adds the matrices and inserts the result into a new matrix
    for i in range(len(a)):
      newRow = []
      for j in range(len(a[0])):
        newRow.append(a[i][j] + b[i][j])  
      result.append(newRow)
    return result


""" Using the function addMatrices() """
matrix1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8 ,9]]

matrix2 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8 ,0]]

print("\n")
print("Result of adding our two matrices:")
print(showMatrix(addMatrices(matrix1, matrix2)))


def searchMaxValue(matrix, axis = 2):
    """
        Receives a matrix and a number that indicates what calculation to do:
        
        If it is 2 (default value), it returns a single number, the largest in the matrix.
        
        If it is 1, it finds the maximum value for each row.
        It returns a vector with as many positions as rows.
        
        If it is 0, it finds the maximum value for each column.
        It returns a vector with as many positions as columns.
        
        Args:
            matrix
            axis
    """
    
    # First, it checks if it is a matrix
    if not(isMatrix(matrix)):
        raise Exception("Invalid matrix")
    
    maxValues = []
    if(axis == 2 or axis == 1):
        # It looks for the maximum row by row
        for row in matrix:
            maxValues.append(max(row))
        if(axis == 1):
            return maxValues
        else:
            return max(maxValues)
    
    if(axis == 0):
        for j in range(len(matrix[0])):
            # It collects the column in a list
            column = [matrix[i][j] for i in range(len(matrix))]
            maxValues.append(max(column))
        return maxValues

""" Using the function searchMaxValue() """
matrix = [[1, 2, 3],          
          [4, 5, 6],
          [7, 8, 9],
          [10, 11, 12]]

print("\n")
print("Largest number in the matrix:")
print("With default axis ->", searchMaxValue(matrix))
print("With axis 2 ->", searchMaxValue(matrix, axis = 2))

print("\n")
print("Maximum value for each row (axis 1):")
print(searchMaxValue(matrix, axis = 1))

print("\n")
print("Maximum value for each column (axis 10):")
print(searchMaxValue(matrix, axis = 0))

print("\n")
print("Function with an invalid matrix:")
print(searchMaxValue([[1, 2, 3,], [1, 2]], axis = 0))
