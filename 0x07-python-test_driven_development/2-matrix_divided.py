#!/usr/bin/python3
"""Defines a matrix division function"""

def matrix_divided(matrix, div):
    """Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): num to divide
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix which is result of the division.
    """

    if not isinstance(div, (int,float)):
        raise TypeError("div must be a number")
    
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    for row in matrix:
        if not isinstance(row, list) or len(row == 0):
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for n in row:
            if not isinstance(n, (int,float)):
                 raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(n / div, 2) for n in row] for row in matrix]
   
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
