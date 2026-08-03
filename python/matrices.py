# @filename matrix.py
# @author John (Jack) Bial
# @modified 08/02/2026
# @copyright Public Domain
# @brief Implements a matrix class (Field = C)

from polynomial import *
from copy import deepcopy

class Matrix:

    # Constructor method
    def __init__(self, rowdim = 0, coldim = 0, matrix = []):
        self.rowdim = rowdim
        self.coldim = coldim

        # Checks if the 'matrix' grid is valid
        if matrix != []:
            for i in range(0, rowdim):
                for j in range(0, coldim):
                    if (type(matrix[i][j]) is not int) \
                    and (type(matrix[i][j]) is not float) \
                    and (type(matrix[i][j]) is not str) \
                    and (type(matrix[i][j]) is not Complex):
                    
                        return "MATRIX CONTAINS INVALID TYPE(S)"

                    # Casts 'int's and 'float's to 'Complex'
                    if (type(matrix[i][j]) is int) or (type(matrix[i][j]) is float):
                        item = Complex(matrix[i][j], 0)
                        matrix[i][j] = item

                    # Handles string representations for complex numbers
                    if type(matrix[i][j]) is str:
                        tuple = valid_string(matrix[i][j])
                        valid = tuple[0]
                        if not valid:
                            return "MATRIX HAS INVALID STRING(S)"
                        
                        a = tuple[1]
                        b = tuple[2]
                        item = Complex(a, b)
                        matrix[i][j] = item

        self.matrix = matrix

    # Getter method for a matrix entry
    def get(self, i, j):
        value = self.matrix[i][j]
        return value

    # Setter method for a matrix entry
    def set(self, i, j, value):
        self.matrix[i][j] = value

    # Getter method for a matrix's row dimension
    def get_rowdim(self):
        value = self.rowdim
        return value

    # Getter method for a matrix's column dimension
    def get_coldim(self):
        value = self.coldim
        return value

    # Getter method for a matrix's array representation
    def get_array(self):
        array = deepcopy(self.matrix)
        return array

    # Checks if the matrix is a square matrix
    def is_square(self):
        if self.rowdim == self.coldim:
            return True
        return False
    
    # Prints out a 'Matrix' object
    def print(self):
        for i in range(0, self.rowdim):
            row = ""
            for j in range(0, self.coldim):
                if j == 0:
                    row += '[' 
                if j == self.coldim - 1:
                    entry = f"{self.matrix[i][j].to_string()}"
                    row += entry
                    row += ']'
                else:
                    entry = f"{self.matrix[i][j].to_string()}"
                    row += entry
                    row += " "
            print(row)
    
    # Calculates the transpose of a matrix
    def transpose(self):
        matrix_transpose = Matrix(self.coldim, self.rowdim, [])

        # Kind of appends rows and columns in the reverse order...
        for i in range(0, self.coldim):
            matrix_transpose.matrix.append([])
            for j in range(0, self.rowdim):
                matrix_transpose.matrix[i].append(self.matrix[j][i])
        return matrix_transpose
    
    # Calculates the conjugate transpose of a matrix
    def dagger(self):
        A_dagger = Matrix(self.coldim, self.rowdim, [])

        # Kind of appends rows and columns in the reverse order...
        for i in range(0, self.coldim):
            A_dagger.matrix.append([])
            for j in range(0, self.rowdim):
                A_dagger.matrix[i].append(
                    Complex((self.matrix[j][i]).a, -(self.matrix[j][i].b))
                    )
        return A_dagger

    # Calculates the trace of a matrix
    def trace(self):

        # Uhh we kind of can't get the trace of a non-square matrix...
        if not self.is_square():
            return "ERROR: Not a square matrix!"
        
        # Adds the diagonal terms to get the trace of the matrix
        matrix_trace = 0
        for i in range(0, self.rowdim):
            matrix_trace = matrix_trace + self.matrix[i][i]
        return matrix_trace
    
    # Recursive helper method for calculating the determinant of a matrix
    def determinant_helper(self, dimension, matrix):

        # Base case for a 2 x 2 matrix
        if dimension == 2:
            return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        
        # Recursive case
        determinant = 0
        for i in range(0, dimension):

            # Gets the [i]th minor of the matrix
            minor = []
            for j in range(1, dimension):
                minor.append([])
                for k in range(0, dimension):
                    if k != i:
                        minor[j - 1].append(matrix[j][k])

            # Determines whether the subproblem should be added or subtracted
            if i % 2 == 0:
                determinant += matrix[0][i] * (self.determinant_helper(dimension - 1, minor))
            else:
                determinant -= matrix[0][i] * (self.determinant_helper(dimension - 1, minor))             
        return determinant

    # Calculates the determinant of a matrix
    def determinant(self):

        # If the matrix isn't square, we can't get any such determinant
        if not self.is_square():
            return "ERROR: Not a square matrix!"
        
        # The determinant of a 1 x 1 matrix is just its entry
        if self.rowdim == 1:
            return self.matrix[0]
        
        # Otherwise call and return the helper method
        return self.determinant_helper(self.rowdim, self.matrix)
    
    # Determines if a matrix is invertible using the Invertibility Theorem
    def is_invertible(self):
        
        # All invertible matrices are square
        if not self.is_square():
            return False
        
        # det(A) = 0 for all singular matrices A in M_n
        if self.determinant() == 0:
            return False
        
        # The rest of the Invertibility Theorem statements are equivalent
        return True
    
    # Defines the '+' operator for matrices
    def __add__(self, other):

        # Checks if the two addends have the same dimensions
        if (self.rowdim != other.rowdim) or (self.coldim != other.coldim):
            return "DIMENSION ERROR"
        
        # Checks if we are actually adding two matrices together
        if type(other) is not Matrix:
            return "TYPE ERROR"
        
        # Iterates through the addends and adds each entry together to get the sum
        sum = Matrix(self.rowdim, self.coldim, [])
        for i in range(0, self.rowdim):
            sum.matrix.append([])
            for j in range(0, self.coldim):
                sum.matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
        return sum
    
    # Defines negation for matrices
    def __neg__(self):

        # Literally just iterates through the matrix and negates every entry
        neg = Matrix(self.rowdim, self.coldim, [])
        for i in range(0, self.rowdim):
            neg.matrix.append([])
            for j in range(0, self.coldim):
                neg.matrix[i].append(-self.matrix[i][j])
        return neg
    
    # Defines the '-' operator for matrices
    def __sub__(self, other):
        return self.__add__(-other)

    # Defines the '*' operator for matrices
    def __mul__(self, other):

        # Checks if the matrix is being multiplied by a compatible data type
        if (type(other) is not Matrix) \
            and (type(other) is not int) \
            and (type(other) is not float) \
            and (type(other) is not Complex):
            return "TYPE ERROR"
        
        # Deals with the case of a matrix being multiplied by a scalar
        if (type(other) is int) \
            or (type(other) is float) \
            or (type(other) is Complex):
            product = Matrix(self.rowdim, self.coldim, deepcopy(self.matrix))
            for i in range (0, product.rowdim):
                for j in range(0, product.coldim):
                    product.matrix[i][j] = product.matrix[i][j] * other
                    # product.matrix[i][j] = other * product.matrix[i][j]
            return product
        
        # Checks if the factor dimensions work for matrix multiplication
        if self.coldim != other.rowdim:
            return "DIMENSION ERROR"
        
        # Performs Euclidean Inner Products on the two factors to get the product's entries
        product = Matrix(self.rowdim, other.coldim, [])
        for i in range(0, self.rowdim):
            product.matrix.append([])
            for j in range(0, other.coldim):
                entry = Complex()
                for k in range(0, self.coldim):
                    entry += (self.matrix[i][k]) * (other.matrix[k][j])
                product.matrix[i].append(entry)
        return product
    
    # Defines the '==' operator for matrices
    def __eq__(self, other):

        # A matrix can only be equal to another matrix...
        if type(other) is not Matrix:
            return False
        
        return self.matrix == other.matrix
    
    # Defines the '|' operator to compute an inner product
    def __or__(self, other):

        # Inner products for matrices...require two matrices
        if type(other) is not Matrix:
            return "TYPE ERROR"
        
        # The dimensions of each matrix must match
        if (self.rowdim != other.rowdim) \
        or (self.coldim != other.coldim):
            return "DIMENSION ERROR"
        
        # If each matrix is in F^n, use the Euclidean Inner Product
        if self.coldim == 1:
            return euclidean_ip(self, other)
        
        # If the matrices are not in F^n, use the Frobenius Inner Product
        else:
            return frobenius_ip(self, other)
        
    # Gets the eigenvalues of a matrix
    def get_eigenvalues(self):

        # Again, ya need a square matrix...
        if not self.is_square():
            return "ERROR: Not a square matrix!"
        
        # Turns the diagonal of the matrix into (a - x) terms
        characteristic = Matrix(self.rowdim, self.coldim, deepcopy(self.matrix))
        for i in range(0, characteristic.rowdim):
            diagonal = Polynomial(1, [characteristic.matrix[i][i], -1])
            characteristic.matrix[i][i] = diagonal

        # Gets the characteristic polynomial with the determinant
        char_poly = characteristic.determinant()

        # Returns the eigenvalues (roots) of the characteristic polynomial
        return char_poly.get_roots()
    
    # Does a type 1 elementary row operation on rows 'x' and 'y'
    def type_1(self, x, y):
        row_x = list(self.matrix[x])
        row_y = list(self.matrix[y])
        self.matrix[x] = row_y
        self.matrix[y] = row_x

    # Does a type 2 elementary row operation on row 'x' with a real scalar
    def type_2(self, scalar, x):
        row_x = list(self.matrix[x])
        for i in range(0, len(row_x)):
            row_x[i] = scalar * row_x[i]
        self.matrix[x] = row_x

    # Does a type 3 elementary row operation on row 'y' with row 'x' and a real scalar
    def type_3(self, scalar, x, y):
        row_x = list(self.matrix[x])
        for i in range(0, len(row_x)):
            row_x[i] = scalar * row_x[i]
        row_y = list(self.matrix[y])
        for i in range(0, len(row_y)):
            row_y[i] = row_y[i] + row_x[i]
        self.matrix[y] = row_y

    # Checks if a given row is a zero row
    def is_zero_row(self, row_num):
        for i in range(0, self.coldim):
            if self.matrix[row_num][i] != 0:
                return False
        return True
    
    # Takes a matrix down to Row Echelon Form
    def ref(self, rows_done):

        # Checks if the matrix is already in REF
        if rows_done == self.rowdim:
            return self
        
        # Initializes the starting state
        first_column = 0
        first_row = -1

        # Finds the first non-zero column
        for j in range(0, self.coldim):
            
            # Finds the row with the first non-zero entry 
            for i in range(rows_done, self.rowdim):
                if self.matrix[i][j] != 0:
                    first_row = i
                    break
            
            # Checks if the entire column is zeros or not
            if first_row >= rows_done:
                break
            first_column += 1  
        
        # Calls REF again with the current row done if all columns are zero
        if first_column == self.coldim:
            self.ref(rows_done + 1)
        else:
            non_zero_entry = self.matrix[first_row][first_column]

            # Moves the first non-zero entry to the first row
            if first_row != rows_done:
                self.type_1(rows_done, first_row)

            # Makes the first non-zero entry equal to one if not so already
            if non_zero_entry != 1:
                unit = Complex(1, 0)
                self.type_2((unit / non_zero_entry), rows_done)
            
            # Makes all the entries beneath that leading one equal to zero
            for i in range(rows_done + 1, self.rowdim):
                value = self.matrix[i][first_column]
                if value != 0:
                    self.type_3(-value, first_row, i)
            
            # Calls REF again after the row is done
            self.ref(rows_done + 1)

    # Takes a matrix in Row Echelon Form down to Reduced Row Echelon Form
    def rref(self):

        # Takes the matrix to REF
        self.ref(0)

        row_num = self.rowdim - 1
        for i in range(row_num, 0, -1):

            # Checks if the matrix is in R_n
            if row_num == 0:
                return self
            
            # Moves on if the current row is a zero row
            if self.is_zero_row(i):
                row_num -= 1
                continue

            # Finds the index for the leading one
            leading_one_index = 0
            while self.matrix[i][leading_one_index] == 0.0:
                leading_one_index += 1

            # Performs type 3 operations to get all entries above the leading one equal to zero
            for j in range(i - 1, -1, -1):
                if self.matrix[j][leading_one_index] != 0.0:
                    value = self.matrix[j][leading_one_index]
                    self.type_3(-value, i, j)  
        return self          

    
    # Uses the methods above to find the pseudoinverse of a matrix
    def pseudoinverse(self):

        # The number '1' as a 'Complex' object
        unit = Complex(1, 0)

        # Gets the super special A-dagger-A matrix :)
        AtA = self.dagger() * self

        # Identity matrix to use for the eigenbasis of A-dagger-A
        identity = Matrix(AtA.rowdim, AtA.coldim, [])
        for i in range(0, self.rowdim):
            identity.matrix.append([])
            for j in range(0, AtA.coldim):
                identity.matrix[i].append(Complex(0, 0))
        for i in range(0, AtA.rowdim):
            identity.matrix[i][i] = Complex(1, 0)

        # Eigenvalues for A-dagger-A
        eigenvalues = AtA.get_eigenvalues()
        eigenvalues.sort()
        eigenvalues.reverse()

        # Positive singular values for A (A-dagger as well)
        non_zero_singulars = []
        for eigenvalue in eigenvalues:
            eigenvalue.print()
        for i in range(0, len(eigenvalues)):
            singular_value = (eigenvalues[i]).sqrt()
            if singular_value != 0:
                non_zero_singulars.append(singular_value)
        non_zero_singulars.sort()
        non_zero_singulars.reverse()

        # Sigma matrix

        S = Matrix(len(non_zero_singulars), len(non_zero_singulars), [])
        for i in range(0, len(non_zero_singulars)):
            S.matrix.append([])
            for j in range(0, len(non_zero_singulars)):
                S.matrix[i].append(Complex(0, 0))
        for i in range(0, len(non_zero_singulars)):
            S.matrix[i][i] = non_zero_singulars[i]
        
        # Gets the inverse of the Sigma matrix
        S_inv = Matrix(len(non_zero_singulars), len(non_zero_singulars), deepcopy(S.matrix))
        for i in range(len(non_zero_singulars)):
            for j in range(len(non_zero_singulars)):
                if S_inv.matrix[i][j] != 0:
                    S_inv.matrix[i][j] = (unit / S_inv.matrix[i][j])

        # Gets the orthonormal eigenbasis for the 'U' and 'V' matrices
        eigenbasis = []
        for i in range(0, len(eigenvalues)):
            thing = AtA - (identity * eigenvalues[i])
            basis = kernel_basis(thing)
            for vector in basis:
                eigenbasis.append(vector)
        orthonormalize(eigenbasis)
        for eigenvector in eigenbasis:
            eigenvector.print()

        # U matrix

        Ut = Matrix(len(non_zero_singulars), self.rowdim, [])
        for i in range(0, len(non_zero_singulars)):
            eigenvector = Matrix(eigenbasis[i].rowdim, 1, [])
            for j in range(0, eigenbasis[i].rowdim):
                eigenvector.matrix.append([eigenbasis[i].matrix[j][0]])
            column = (self * eigenvector) * (unit / non_zero_singulars[i])
            row = column.dagger()
            Ut.matrix.append(row.matrix[0])
        U = Ut.dagger()

        # V matrix

        Vt = Matrix(len(non_zero_singulars), self.coldim, [])
        for i in range(0, len(non_zero_singulars)):
            eigenvector = Matrix(eigenbasis[i].rowdim, 1, eigenbasis[i].matrix)
            row = eigenvector.dagger()
            Vt.matrix.append(row.matrix[0])
        V = Vt.dagger()

        # Calculating the pseudoinverse

        psinv = (V * S_inv) * Ut
        V.print()
        print()
        S_inv.print()
        print()
        Ut.print()
        return psinv
    
'''
VARIOUS VECTOR AND BASIS OPERATIONS
'''

# Forms an identity matrix of the desired dimension
def form_identity(dimension):
    identity = Matrix(dimension, dimension, [])
    for i in range(0, dimension):
        identity.matrix.append([])
        for j in range(0, dimension):
            if (i == j):
                identity.matrix[i].append(Complex(1, 0))
            else:
                identity.matrix[i].append(Complex(0, 0))
    return identity

# Finds the basis for the kernel of a matrix
def kernel_basis(matrix):

    # Gets the matrix into RREF
    matrix.rref()
    
    # This procedure is only for 2 x 2 matrices :(
    # ...apparently the general procedure is an NP-hard problem, so yeah.

    if (matrix.is_zero_row(0)) and (matrix.is_zero_row(1)):
        basis = [Matrix(2, 1, [[Complex(1, 0)], 
                               [Complex(0, 0)]]),
                 Matrix(2, 1, [[Complex(0, 0)], 
                               [Complex(1, 0)]])
        ]
        return basis
    elif (not matrix.is_zero_row(0)) and (not matrix.is_zero_row(1)):
        basis = [Matrix(2, 1, [[Complex(0, 0)], 
                               [Complex(0, 0)]])
        ]
        return basis
    
    # Bottom row must be a zero row if we get here
    elif (matrix.matrix[0][0] != 0) and (matrix.matrix[0][1] != 0):
        basis = [Matrix(2, 1, [[-matrix.matrix[0][1]], 
                               [Complex(1, 0)]])
        ]
        return basis
    elif (matrix.matrix[0][0] == 0) and (matrix.matrix[0][1] == 1):
        basis = [Matrix(2, 1, [[Complex(1, 0)], 
                               [Complex(0, 0)]])
        ]
        return basis
    else:
        basis = [Matrix(2, 1, [[Complex(0, 0)], 
                               [Complex(1, 0)]])
        ]
        return basis

# Implements the Euclidean Inner Product
def euclidean_ip(v, w):

    product = v.dagger() * w
    return product.matrix[0][0]

# Implements the Frobenius Inner Product
def frobenius_ip(A, B):

    product = A.dagger() * B
    return product.trace()

# Determines if a basis is orthogonal or not
def is_orthogonal(basis):
    for v in basis:
        for w in basis:
            if v == w:
                continue
            if (v | w) != 0:
                return False
    return True

# Implements the Gram-Schmidt Procedure
def gram_schmidt(basis):
    for i in range(1, len(basis)):
        new_vector = basis[i]
        for j in range(0, i):
            new_vector = new_vector - (basis[j] * \
            ((basis[j] | basis[i]) / (basis[j] | basis[j])))
        basis[i] = new_vector

# Orthonormalizes a basis with the Gram-Schmidt Procedure
def orthonormalize(basis):

    # Performs Gram-Schmidt if the basis is not already orthogonal
    if not (is_orthogonal(basis)):
        gram_schmidt(basis)

    # Just finds the norm of each basis vector and makes it unit
    for i in range(0, len(basis)):
        norm_squared = (basis[i] | basis[i])
        norm = norm_squared.sqrt()
        for k in range(0, len(basis[i].matrix)):
            if norm != 0:
                basis[i].matrix[k][0] = basis[i].matrix[k][0] / norm