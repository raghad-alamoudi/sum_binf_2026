# INI2 
'''Given: Two positive integers aand b, each less than 1000.
Return: The integer corresponding to the square of the hypotenuse of the 
right triangle whose legs have lengths a and b.'''
def square_hypotenuse(a, b):
    c = (a ** 2) + (b ** 2)
    return c    
a = 930
b = 926
print(square_hypotenuse(a, b))