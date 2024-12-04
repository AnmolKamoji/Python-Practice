# Fill in the blanks to make the is_power_of function return whether the number is a power of the given base. 
# Note: base is assumed to be a positive number. 
# Tip: for functions that return a boolean value, you can return the result of a comparison.

def is_power_of(number, base):
    # Base case: when number is equal to 1.
    if number == 1:
        return True
    # If the number is less than the base, it cannot be a power of the base.
    if number < base:
        return False
    # Recursive case: if number is divisible by base, continue with the division.
    if number % base == 0:
        return is_power_of(number // base, base)
    else:
        return False

# Test cases
print(is_power_of(8, 2))    # Should be True (2^3)
print(is_power_of(64, 4))   # Should be True (4^3)
print(is_power_of(70, 10))  # Should be False (70 is not a power of 10)
