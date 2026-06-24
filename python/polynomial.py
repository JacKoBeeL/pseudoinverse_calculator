# @filename polynomial.py
# @author John (Jack) Bial
# @modified 06/11/2025
# @copyright Public Domain
# @brief Implementation of a polynomial class (Field = C)

from complex import *

class Polynomial:

    # Constructor method
    def __init__(self, degree = 0, contents = []):
        self.degree = degree

        # Checks if the 'contents' array is valid
        if contents != []:
            for i in range(0, degree + 1):
                if (type(contents[i]) is not int) \
                and (type(contents[i]) is not float) \
                and (type(contents[i]) is not str) \
                and (type(contents[i]) is not Complex):
                
                    return "CONTENTS CONTAIN INVALID TYPE(S)"

                # Casts 'int's and 'float's to 'Complex'
                if (type(contents[i]) is int) or (type(contents[i]) is float):
                    item = Complex(contents[i], 0)
                    contents[i] = item

                # Handles string representations for complex numbers
                if type(contents[i]) is str:
                    tuple = valid_string(contents[i])
                    valid = tuple[0]
                    if not valid:
                        return "CONTENTS HAVE INVALID STRING(S)"
                    
                    a = tuple[1]
                    b = tuple[2]
                    item = Complex(a, b)
                    contents[i] = item

        self.contents = contents

    # Prints a 'Polynomial' object        
    def print(self):
        string = ""
        for i in range(0, self.degree + 1):

            # Deals with the polynomial's constant term
            if i == 0:
                if (self.contents[0].a != 0) or (self.contents[0].b != 0):
                    if 0 == self.degree:
                        string += f"{self.contents[0].to_string()}"
                    else:
                        string += f"{self.contents[0].to_string()} + "
            
            # Deals with the polynomial's linear term
            elif i == 1:
                if (self.contents[1].a != 0) or (self.contents[1].b != 0):
                    if 1 == self.degree:
                        string += f"{self.contents[1].to_string()}x"
                    else:
                        string += f"{self.contents[1].to_string()}x + "
            
            # Deals with the polynomial's leading term
            elif i == self.degree:
                if (self.contents[self.degree].a != 0) \
                    or (self.contents[self.degree].b != 0):
                    
                    string += f"{self.contents[self.degree].to_string()}x^{i}"

            # Deals with all other terms for the polynomial
            else:
                if (self.contents[i].a != 0) or (self.contents[i].b != 0):
                    string += f"{self.contents[i].to_string()}x^{i} + "
        
        # Prints out the final string
        print(string)
    
    # Defines the '+' operator for polynomials
    def __add__(self, other):

        # Checks if the two items being added together are compatible
        if (type(other) is not Polynomial) and (type(other) is not int) \
            and (type(other) is not float) and (type(other) is not str) \
            and (type(other) is not Complex):
            return "TYPE ERROR"
        
        # Deals with the case of two polynomials being added together
        if type(other) is Polynomial:
            addend_1_contents = list(self.contents)
            addend_2_contents = list(other.contents)
            addend_1 = Polynomial(self.degree, addend_1_contents)
            addend_2 = Polynomial(other.degree, addend_2_contents)

            # Creates a new polynomial to be the sum of the two addends
            sum = Polynomial(max(addend_1.degree, addend_2.degree), [])

            # Ensures the dimensions of each of the addends' arrays are the same
            if (addend_1.degree < addend_2.degree):
                for i in range(addend_1.degree, addend_2.degree):
                    addend_1.contents.append(Complex(0, 0))
            elif (addend_1.degree > addend_2.degree):
                for i in range(addend_2.degree, addend_1.degree):
                    addend_2.contents.append(Complex(0, 0))

            # Iterates through each addend and adds the terms together        
            for i in range(0, sum.degree + 1):
                sum.contents.append(addend_1.contents[i] + addend_2.contents[i])
            while sum.contents[sum.degree] == 0:
                sum.contents.pop(sum.degree)
                sum.degree = sum.degree - 1
            return sum
        
        # Deals with the case of a polynomial and a constant added together
        else:

            # If we have a string representation of a complex number
            if type(other) is str:
                tuple = valid_string(other)
                valid = tuple[0]
                if not valid:
                    return "CONTENTS HAVE INVALID STRING(S)"
                
                a = tuple[1]
                b = tuple[2]
                second_addend = Complex(a, b)
                sum_contents = list(self.contents)
                sum = Polynomial(self.degree, sum_contents)
                sum.contents[0] += second_addend
                return sum
            
            # Other cases of a constant
            sum_contents = list(self.contents)
            sum = Polynomial(self.degree, sum_contents)
            sum.contents[0] += other
            return sum
    
    # Defines negation for polynomials
    def __neg__(self):
        neg = Polynomial(self.degree, [])
        for i in range(0, self.degree + 1):
            neg.contents.append(-self.contents[i])
        return neg
        
    # Defines the '-' operator for polynomials
    def __sub__(self, other):
        return self.__add__(-other)
    
    # Defines the '*' operator for polynomials
    def __mul__(self, other):

        # Checks if the two items being multiplied together are compatible
        if (type(other) is not Polynomial) and (type(other) is not int) \
            and (type(other) is not float) and (type(other) is not str) \
            and (type(other) is not Complex):
            
            return "TYPE ERROR"
        
        # Deals with the case of two polynomials being multiplied together
        if type(other) is Polynomial:

            # Defines a new polynomial object for the product of the two factors
            product = Polynomial(self.degree + other.degree, [])
            for i in range(product.degree + 1):
                product.contents.append(Complex(0, 0))
            for i in range(0, self.degree + 1):
                for j in range(0, other.degree + 1):
                    element = self.contents[i] * other.contents[j]

                    # Uses rules of exponents to determine the degree of the [i][j]th term
                    element_power = i + j
                    product.contents[element_power] += element
            return product
        
        # Deals with the case of a polynomial and a constant being multiplied together
        else:

            # If we have a string representation of a complex number
            if type(other) is str:
                tuple = valid_string(other)
                valid = tuple[0]
                if not valid:
                    return "CONTENTS HAVE INVALID STRING(S)"
                
                a = tuple[1]
                b = tuple[2]
                second_factor = Complex(a, b)
                product = Polynomial(self.degree, [])
                for i in range(0, product.degree + 1):
                    product.contents.append(self.contents[i] * second_factor)
                return product

            # Other cases of a constant
            product = Polynomial(self.degree, [])
            for i in range(0, product.degree + 1):
                product.contents.append(self.contents[i] * other)
            return product
    
    # Finds the roots of a polynomial
    # This only works for polynomials of degree at most 2
    def get_roots(self):
        if self.degree > 2:
            return "Uhh, we're not gonna talk about that..."
        
        # Polynomials of degree 0 have no defined roots
        if self.degree == 0:
            return "CONSTANT POLYNOMIAL, NO ROOTS"
    
        # Solves a linear polynomial for its root
        if self.degree == 1:
            root = [(-self.contents[0]) / self.contents[1]]
            return root
        
        # Uses the quadratic formula to find the roots of a quadratic polynomial
        else:
            a = self.contents[2]
            b = self.contents[1]
            c = self.contents[0]
            root_1 = ((-b) + ((b ** 2) - (a * c) * 4).sqrt()) / (a * 2)
            root_2 = ((-b) - ((b ** 2) - (a * c) * 4).sqrt()) / (a * 2)
            roots = [root_1, root_2]
            return roots
        
if __name__ == '__main__':
    poly1 = Polynomial(1, [2, "3+3i"])
    poly2 = Polynomial(1, [0, "3i"])
    poly3 = poly1 + poly2
    poly4 = Polynomial(2, [4, -4, 1])
    poly3.print()
    roots = poly4.get_roots()
    for root in roots:
        root.print()