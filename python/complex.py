# @filename complex.py
# @author John (Jack) Bial
# @modified 06/11/2025
# @copyright Public Domain
# @brief Implements a complex numbers class

# NOTE: I know that a complex type already exists 
# in Python, but I'm writing this for practice
# and honestly I don't like the Python one anyways...

from math import *

# Literally just a bunch of checks to see if an input string represents a complex number
# Parameters 'a' and 'b' are to collect the terms for the complex numbers if valid
def valid_string(string):

    # Initializes 'a' and 'b'
    a = 0.0
    b = 0.0

    # Is the input even a string??
    if type(string) is not str:
        return False, a, b
    
    # Does the string happen to be a real number?
    try:
        a = float(string)
        return True, a, b
    except:
        pass

    # Is the last character an 'i'?
    if string[len(string) - 1] != 'i':
        return False, a, b
    
    ''' Conditions to see if the string is in the correct format '''

    # Array containing 0 to 9
    numerals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # Checks the first term for the complex number

    # Sets the starting index to 1 if the first term is negative
    first = ""
    if string[0] == '-':
        curr_index = 1
        first = first + '-'
    else:
        curr_index = 0

    while (string[curr_index] != ' ') \
        and (string[curr_index] != '+') \
        and (string[curr_index] != '-'):

        curr_char = string[curr_index]
        curr_index = curr_index + 1
        
        # This part accounts for purely imaginary numbers
        if (curr_char == 'i'):
            if len(string) == 1:
                return True, a, 1
            elif (len(string) == 2) and (string[0] == '-'):
                return True, a, -1
            try:
                b = float(first)
                return True, a, b
            except ValueError:
                return False, a, b

        first = first + curr_char

    # Converts the first term to a float if possible and sets 'a' equal to it
    try:
        a = float(first)
    except ValueError:
        return False, a, b
    
    # Checks if the operator portion is valid

    # This variable checks to make sure there is only one operator
    # This also checks if the second term is positive or negative
    operators = []
    while (string[curr_index] not in numerals) and \
            (string[curr_index] != 'i'):
        
        curr_char = string[curr_index]
        curr_index = curr_index + 1

        # Operator, or not?
        if (curr_char == '+') or (curr_char == '-'):
            operators.append(curr_char)
    
    # Not valid if the string has a space but not a single operator
    if len(operators) != 1:
        return False, a, b
    
    # Checks the second term of the complex number
    # First, check if the second term is positive or negative
    if operators[0] == '-':
        second = "-"
    else:
        second = ""

    while string[curr_index] != 'i':
        curr_char = string[curr_index]
        curr_index = curr_index + 1
        second = second + curr_char

    # Converts the second term to a float if possible and sets 'b' equal to it
    if len(second) == 0:
        return True, a, 1
    elif (len(second) == 1) and (second[0] == '-'):
        return True, a, -1
    try:
        b = float(second)
        return True, a, b
    except ValueError:
        return False, a, b

# C = {a + b(i) | a, b in R; i = sqrt(-1)}
# Let 'r' be a complex number with r = a + b(i)
class Complex:
    
    # Constructor method
    def __init__(self, a = 0, b = 0):
        self.a = a
        self.b = b

    # Prints a 'Complex' object (complex number)
    def print(self):

        # Ensures that only '0' is printed if r = 0
        if self.a == 0 and self.b == 0:
            num = "(0)"
            print(num)

        # Ensures that only Re(r) is printed if Im(r) = 0
        elif self.a != 0 and self.b == 0:
            num = f"({round(self.a, 2)})"
            print(num)

        # Ensures that only Im(r) is printed if Re(r) = 0
        elif self.a == 0 and self.b != 0:
            num = f"({round(self.b, 2)}i)"
            print(num)

        # Re(r) != 0 and Im(r) != 0
        else:

            # Only prints i or -i if |Im(r)| = 1
            if abs(self.b) == 1:
                if self.b < 0:
                    num = f"({self.a}-i)"
                else:
                    num = f"({self.a}+i)"
                print(num)

            # All other cases
            else:
                if self.b < 0:
                    num = f"({round(self.a, 2)}-{round(-self.b, 2)}i)"
                else:
                    num = f"({round(self.a, 2)}+{round(self.b, 2)}i)"
                print(num)

    # Casts a 'Complex' object to a 'str'
    def to_string(self):
        # Ensures that only '0' is returned if r = 0
        if self.a == 0 and self.b == 0:
            num = "(0)"
            return num

        # Ensures that only Re(r) is returned if Im(r) = 0
        elif self.a != 0 and self.b == 0:
            num = f"({round(self.a, 2)})"
            return num

        # Ensures that only Im(r) is returned if Re(r) = 0
        elif self.a == 0 and self.b != 0:
            if self.b == 1:
                num = f"(i)"
            elif self.b == -1:
                num = f"(-i)"
            else:
                num = f"({round(self.b, 2)}i)"
            return num

        # Re(r) != 0 and Im(r) != 0
        else:

            # Only adds i or -i if |Im(r)| = 1
            if abs(self.b) == 1:
                if self.b < 0:
                    num = f"({self.a}-i)"
                else:
                    num = f"({self.a}+i)"
                return num

            # All other cases
            else:
                if self.b < 0:
                    num = f"({round(self.a, 2)}-{round(-self.b, 2)}i)"
                else:
                    num = f"({round(self.a, 2)}+{round(self.b, 2)}i)"
                return num
            
    # Finds the conjugate of a complex number
    def conjugate(self):
        return Complex(self.a, -self.b) 

    # Defines the '+' operator for complex numbers
    def __add__(self, other):

        # Ensures that the types of self and other are compatible
        if (type(other) is not Complex) and (type(other) is not int) \
            and (type(other) is not float) and (type(other) is not str):
            return "TYPE ERROR"
        
        # If both addends are 'Complex'
        if type(other) is Complex:
            sum = Complex()
            sum.a = self.a + other.a
            sum.b = self.b + other.b
            return sum
        
        # If 'other' is a 'str'
        elif type(other) is str:
            tuple = valid_string(other)
            valid = tuple[0]
            a = tuple[1]
            b = tuple[2]
            if not valid:
                return "INVALID STRING"
            second_addend = Complex(a, b)
            sum = Complex()
            sum.a = self.a + second_addend.a
            sum.b = self.b + second_addend.b
            return sum

        # If 'other' is an 'int' or a 'float'
        else:
            sum = Complex()
            sum.a = self.a + other
            sum.b = self.b
            return sum
    
    # Defines the '+=' operator for complex numbers
    def __iadd__(self, other):

        # Ensures that the types of self and other are compatible
        if (type(other) is not Complex) and (type(other) is not int) \
            and (type(other) is not float) and (type(other) is not str):
            return "TYPE ERROR"
        
        # If both addends are 'Complex'
        if type(other) is Complex:
            self.a = self.a + other.a
            self.b = self.b + other.b
            return self
        
        # If 'other' is a 'str'
        elif type(other) is str:
            tuple = valid_string(other)
            valid = tuple[0]
            a = tuple[1]
            b = tuple[2]
            if not valid:
                return "INVALID STRING"
            second_addend = Complex(a, b)
            self.a = self.a + second_addend.a
            self.b = self.b + second_addend.b
            return self

        # If 'other' is an 'int' or a 'float'
        else:
            self.a = self.a + other
            self.b = self.b
            return self
    
    # Defines negation for complex numbers
    def __neg__(self):
        neg = Complex()
        neg.a = -self.a
        neg.b = -self.b
        return neg

    # Defines the '-' operator for complex numbers
    def __sub__(self, other):

        # If 'other' is a 'str'
        if type(other) is str:
            tuple = valid_string(other)
            valid = tuple[0]
            a = tuple[1]
            b = tuple[2]
            if not valid:
                return "INVALID STRING"
            subtrahend = Complex(a, b)
            difference = Complex()
            difference.a = self.a - subtrahend.a
            difference.b = self.b - subtrahend.b
            return difference
        
        # All other cases
        return self.__add__(-other)
    
    # Defines the '*' operator for complex numbers
    def __mul__(self, other):

        # Ensures that the types of self and other are compatible
        if (type(other) is not Complex) and (type(other) is not int) \
            and (type(other) is not float) and (type(other) is not str):
            return "TYPE ERROR"
        
        # If 'other' is a 'Complex' object
        if type(other) is Complex:
            product = Complex()
            
            # FOIL
            first = self.a * other.a
            outer = self.a * other.b
            inner = self.b * other.a
            last = -(self.b * other.b)

            product.a = first + last
            product.b = outer + inner
            return product
        
        # If 'other' is a 'str'
        elif type(other) is str:
            tuple = valid_string(other)
            valid = tuple[0]
            a = tuple[1]
            b = tuple[2]
            if not valid:
                return "INVALID STRING"
            second_factor = Complex(a, b)
            product = Complex()

            # FOIL
            first = self.a * second_factor.a
            outer = self.a * second_factor.b
            inner = self.b * second_factor.a
            last = -(self.b * second_factor.b)

            product.a = first + last
            product.b = outer + inner
            return product

        # If 'other' is an 'int' or a 'float'
        else:
            product = Complex()
            product.a = self.a * other
            product.b = self.b * other
            return product
        
    # Defines the '/' operator for complex numbers
    def __truediv__(self, other):
        
        # Ensures that the types of self and other are compatible
        if (type(other) is not Complex) and (type(other) is not int) \
            and (type(other) is not float) and (type(other) is not str):
            return "TYPE ERROR"
        
        # If 'other' is a 'Complex' object
        if type(other) is Complex:
            quotient = Complex()

            # Complex division formula
            quotient.a = ((self.a * other.a) + (self.b * other.b)) / ((other.a ** 2) + (other.b ** 2))
            quotient.b = ((self.b * other.a) - (self.a * other.b)) / ((other.a ** 2) + (other.b ** 2))      
            return quotient

        # If 'other' is a 'str'
        elif type(other) is str:
            tuple = valid_string(other)
            valid = tuple[0]
            a = tuple[1]
            b = tuple[2]
            if not valid:
                return "INVALID STRING"
            divisor = Complex(a, b)
            quotient = Complex()

            # Complex division formula...again
            quotient.a = ((self.a * divisor.a) + (self.b * divisor.b)) / ((divisor.a ** 2) + (divisor.b ** 2))
            quotient.b = ((self.b * divisor.a) - (self.a * divisor.b)) / ((divisor.a ** 2) + (divisor.b ** 2))      
            return quotient
        
        # If 'other' is an 'int' or a 'float'
        else:
            quotient = Complex()
            quotient.a = self.a / other
            quotient.b = self.b / other
            return quotient
        
    # Defines the square root of a complex number
    # Can get either the positive or negative root
    def sqrt(self):
        square_root = Complex()

        # If 'self' is a non-negative real number
        if (self.a >= 0) and (self.b == 0):
            square_root.a = self.a ** (1/2)
            return square_root
        
        # If 'self' is a negative real number
        if (self.a < 0) and (self.b == 0):
            square_root.a == 0
            square_root.b = (-self.a) ** (1/2)
            return square_root
        
        # All other cases, uses the square root formula for complex numbers
        square_root.a = sqrt((sqrt((self.a ** 2) + (self.b ** 2)) + self.a) / 2)
        square_root.b = (self.b / abs(self.b)) * sqrt((sqrt((self.a ** 2) + (self.b ** 2)) - self.a) / 2)
        return square_root
        
    # Defines the '**' operator for complex numbers
    def __pow__(self, power: int):
        if (type(power) is not int) and (power != 1/2):
            return "AAAAAAA too complicated :("
        
        result = Complex(self.a, self.b)

        # '1' as a 'Complex' object
        unit = Complex(1, 0)

        # Any nonzero complex number raised to the 0th is equal to 1
        if power == 0:
            return unit
        
        # Gets the square root if the power is 1/2
        if power == 1/2:
            return result.sqrt()
        
        # Positive exponents
        if power >= 1:
            for i in range(1, power):
                result = result * self
            return result
    
        # Negative exponents
        if power == -1:
            inverse = unit / result
            return inverse
        else:
            for i in range(1, -power):
                result = result * self
            final = unit / result
            return final
        
    # Defines the '==' operator for complex numbers
    def __eq__(self, other):

        # Ensures that the types of self and other are compatible
        if (type(other) is not Complex) and (type(other) is not int) \
            and (type(other) is not float) and (type(other) is not str):
            return "TYPE ERROR"
        
        # If 'other' is a 'Complex' object
        if type(other) is Complex:

            # Checks if the real and imaginary components are equal
            return ((self.a == other.a) and (self.b == other.b))

        # If 'other' is a 'str'
        elif type(other) is str:
            tuple = valid_string(other)
            valid = tuple[0]
            a = tuple[1]
            b = tuple[2]
            if not valid:
                return "INVALID STRING"
            second_number = Complex(a, b)
            
            # Checks if the real and imaginary components are equal
            return ((self.a == second_number.a) and (self.b == second_number.b))
        
        # If 'other' is an 'int' or a 'float'
        else:

            # If we get here, 'other' must be real, so check if 'self' is real
            if self.b != 0:
                return False
            
            return self.a == other
        
    # Defines the '!=' operator for complex numbers
    def __ne__(self, other):

        # Ensures that the types of self and other are compatible
        if (type(other) is not Complex) and (type(other) is not int) \
            and (type(other) is not float) and (type(other) is not str):
            return "TYPE ERROR"
        
        # If 'other' is a 'Complex' object
        if type(other) is Complex:

            # Checks if the real and imaginary components are equal
            return ((self.a != other.a) or (self.b != other.b))

        # If 'other' is a 'str'
        elif type(other) is str:
            tuple = valid_string(other)
            valid = tuple[0]
            a = tuple[1]
            b = tuple[2]
            if not valid:
                return "INVALID STRING"
            second_number = Complex(a, b)
            
            # Checks if the real and imaginary components are equal
            return ((self.a != second_number.a) or (self.b != second_number.b))
        
        # If 'other' is an 'int' or a 'float'
        else:

            # If we get here, 'other' must be real, so check if 'self' is real
            if self.b != 0:
                return True
            
            return self.a != other
        
    # Defines the '>=' operator for complex numbers
    # Only defined for complex numbers that are real
    def __ge__(self, other):

        # Ensures that the types of self and other are compatible
        if (type(other) is not Complex) and (type(other) is not int) \
            and (type(other) is not float) and (type(other) is not str):
            return "TYPE ERROR"
        
        # Ensures that 'self' is real
        if self.b != 0:
            return "UNDEFINED"
        
        # If 'other' is a 'Complex' object
        if type(other) is Complex:

            # Checks if 'other' is real
            if other.b != 0:
                return "UNDEFINED"
            
            # Checks if 'self' is greater than or equal to 'other'
            return self.a >= other.a

        # If 'other' is a 'str'
        elif type(other) is str:
            tuple = valid_string(other)
            valid = tuple[0]
            a = tuple[1]
            b = tuple[2]
            if not valid:
                return "INVALID STRING"
            second_number = Complex(a, b)
            
            # Checks if 'other' is real
            if second_number.b != 0:
                return "UNDEFINED"
            
            # Checks if 'self' is greater than or equal to 'other'
            return self.a >= second_number.a

        # If 'other' is an 'int' or a 'float'
        else:

            # If we get here, 'other' must be real, so check if 'self' is real
            if self.b != 0:
                return False
            
            # Check if 'self' is greater than or equal to 'other'
            return self.a >= other
        
    # Defines the '>' operator for complex numbers
    # Only defined for complex numbers that are real
    def __gt__(self, other):

        # Ensures that the types of self and other are compatible
        if (type(other) is not Complex) and (type(other) is not int) \
            and (type(other) is not float) and (type(other) is not str):
            return "TYPE ERROR"
        
        # Ensures that 'self' is real
        if self.b != 0:
            return "UNDEFINED"
        
        # If 'other' is a 'Complex' object
        if type(other) is Complex:

            # Checks if 'other' is real
            if other.b != 0:
                return "UNDEFINED"
            
            # Checks if 'self' is greater than 'other'
            return self.a > other.a

        # If 'other' is a 'str'
        elif type(other) is str:
            tuple = valid_string(other)
            valid = tuple[0]
            a = tuple[1]
            b = tuple[2]
            if not valid:
                return "INVALID STRING"
            second_number = Complex(a, b)
            
            # Checks if 'other' is real
            if second_number.b != 0:
                return "UNDEFINED"
            
            # Checks if 'self' is greater than 'other'
            return self.a > second_number.a

        # If 'other' is an 'int' or a 'float'
        else:

            # If we get here, 'other' must be real, so check if 'self' is real
            if self.b != 0:
                return False
            
            # Check if 'self' is greater than 'other'
            return self.a > other
        
    # Defines the '<=' operator for complex numbers
    # Only defined for complex numbers that are real
    def __le__(self, other):

        # Ensures that the types of self and other are compatible
        if (type(other) is not Complex) and (type(other) is not int) \
            and (type(other) is not float) and (type(other) is not str):
            return "TYPE ERROR"
        
        # Ensures that 'self' is real
        if self.b != 0:
            return "UNDEFINED"
        
        # If 'other' is a 'Complex' object
        if type(other) is Complex:

            # Checks if 'other' is real
            if other.b != 0:
                return "UNDEFINED"
            
            # Checks if 'self' is less than or equal to 'other'
            return self.a <= other.a

        # If 'other' is a 'str'
        elif type(other) is str:
            tuple = valid_string(other)
            valid = tuple[0]
            a = tuple[1]
            b = tuple[2]
            if not valid:
                return "INVALID STRING"
            second_number = Complex(a, b)
            
            # Checks if 'other' is real
            if second_number.b != 0:
                return "UNDEFINED"
            
            # Checks if 'self' is less than or equal to 'other'
            return self.a <= second_number.a

        # If 'other' is an 'int' or a 'float'
        else:

            # If we get here, 'other' must be real, so check if 'self' is real
            if self.b != 0:
                return False
            
            # Check if 'self' is less than or equal to 'other'
            return self.a <= other
    
    # Defines the '<' operator for complex numbers
    # Only defined for complex numbers that are real
    def __lt__(self, other):

        # Ensures that the types of self and other are compatible
        if (type(other) is not Complex) and (type(other) is not int) \
            and (type(other) is not float) and (type(other) is not str):
            return "TYPE ERROR"
        
        # Ensures that 'self' is real
        if self.b != 0:
            return "UNDEFINED"
        
        # If 'other' is a 'Complex' object
        if type(other) is Complex:

            # Checks if 'other' is real
            if other.b != 0:
                return "UNDEFINED"
            
            # Checks if 'self' is less than 'other'
            return self.a < other.a

        # If 'other' is a 'str'
        elif type(other) is str:
            tuple = valid_string(other)
            valid = tuple[0]
            a = tuple[1]
            b = tuple[2]
            if not valid:
                return "INVALID STRING"
            second_number = Complex(a, b)
            
            # Checks if 'other' is real
            if second_number.b != 0:
                return "UNDEFINED"
            
            # Checks if 'self' is less than 'other'
            return self.a < second_number.a

        # If 'other' is an 'int' or a 'float'
        else:

            # If we get here, 'other' must be real, so check if 'self' is real
            if self.b != 0:
                return False
            
            # Check if 'self' is less than 'other'
            return self.a < other