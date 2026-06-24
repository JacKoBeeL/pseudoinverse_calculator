# @filename pseudo_inverse.py
# @author John (Jack) Bial
# @modified 05/26/2025
# @copyright Public Domain
# @brief Implements SVD and the pseudo inverse of a matrix

'''
WORK IN PROGRESS!!!
'''

# Imports the 'Matrix' and 'Polynomial' classes needed for SVD
from polynomial import *
from matrices import *

# Main driver function for calculating the pseudoinverse of a matrix
def main():
    # # Non-invertible matrix example
    # A = Matrix(3, 2, [
    #     [0, 1],
    #     [1, 0],
    #     [1, 1]
    # ])

    # # Non-invertible square matrix example
    # A = Matrix(2, 2, [
    #     ["10-5i", 0],
    #     [0, 0]
    # ])    

    # Invertible matrix example
    A = Matrix(2, 2, [
        [1, 0],
        [3, 4]
    ])

    # Identity matrices
    I_2 = Matrix(2, 2, [
        [1, 0],
        [0, 1]
    ])

    I_3 = Matrix(3, 3, [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])

    # Calculates the pseudoinverse of a matrix 'A'
    A_psinv = A.pseudoinverse()

    # Printing out the pseudoinverse

    print()
    print("** INPUT MATRIX ** \n A = ")
    A.print()

    print()
    print("** MOORE-PENROSE INVERSE ** \n A_psinv = V * S^{-1} * U^T = ")
    A_psinv.print()

    print()

    return 0

if __name__ == "__main__":
    main()