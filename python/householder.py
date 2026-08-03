# @filename matrix.py
# @author John (Jack) Bial
# @modified 08/02/2026
# @copyright Public Domain
# @brief Implements Householder operations (Field = C)

from matrices import *

# Performs a left Householder reflection; takes a column vector
# Returns the target vector and the Householder matrix
def left_householder(vector):

    # Calculates the norm of the vector using the inner product
    norm = (vector | vector).sqrt()
    
    # Choose 'alpha' to be the norm with the sign determined by the first vector entry
    if (vector.get(0, 0) >= 0):
        alpha = -norm
    else:
        alpha = norm
    
    # Computes the Householder vector and normalizes it
    dimension = vector.get_rowdim()
    target = Matrix(dimension, 1, vector.get_array())
    for i in range(0, dimension):
        if (i == 0):
            target.set(i, 0, alpha)
        else:
            target.set(i, 0, Complex(0, 0))
    householder_vector = vector - target
    normal_vector = householder_vector * (Complex(1, 0) / (householder_vector | householder_vector).sqrt())

    # Computes the Householder matrix
    uuT = normal_vector * (normal_vector.dagger())
    identity = form_identity(uuT.get_rowdim())
    householder_matrix = identity - (uuT * 2)

    # Returns results
    return householder_matrix, target

# Performs a right Householder reflection; takes a row vector
# Returns the target vector and the Householder matrix
def right_householder(vector):

    # Calculates the norm of the vector using the inner product on the transpose
    transpose = vector.dagger()
    norm = (transpose | transpose).sqrt()
    
    # Choose 'alpha' to be the norm with the sign determined by the first vector entry
    if (vector.get(0, 0) >= 0):
        alpha = -norm
    else:
        alpha = norm
    
    # Computes the Householder vector and normalizes it
    dimension = transpose.get_rowdim()
    target_transpose = Matrix(dimension, 1, transpose.get_array())
    for i in range(0, dimension):
        if (i == 0):
            target_transpose.set(i, 0, alpha)
        else:
            target_transpose.set(i, 0, Complex(0, 0))
    target = target_transpose.dagger()
    householder_vector = transpose - target_transpose
    normal_vector = householder_vector * (Complex(1, 0) / (householder_vector | householder_vector).sqrt())

    # Computes the Householder matrix
    uuT = normal_vector * (normal_vector.dagger())
    identity = form_identity(uuT.get_rowdim())
    householder_matrix = identity - (uuT * 2)

    # Returns results
    return householder_matrix, target

def main():
    A = Matrix(3, 1, [
        [4],
        [3],
        [2]
    ])

    B = Matrix(1, 3, [
        [4, 3, 2]
    ])

    left_householder_matrix, left_target = left_householder(A)
    left_householder_matrix.print()
    left_target.print()

    right_householder_matrix, right_target = right_householder(B)
    right_householder_matrix.print()
    right_target.print()

if __name__ == '__main__':
    main()