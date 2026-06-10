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

# INI3
'''Given: A string s of length at most 200 letters and four integers a, b, c and d
Return: The slice of this string from indices a through b and c through d
 (with space in between), inclusively. 
 In other words, we should include elements s[b] and s[d] in our slice.
 '''

s = 'BFvw8CPEfio8ZpVljrvDUXMSvorwIK26nOQe3x8Dlkd73naCitellusMyRWJR9YDQZOZSsdrrzNmbCGdFEsVl33DDQ9yarwbrIGkAs8R6ulLxavo37swvEip0apWu3I2xStIDB2MFjFci0kJBzKJkjJotSMwuj4BIvSg3TVPMqnFsH13e4alpestrisWm02'
a = 47
b = 54
c = 178
d =  186
print(s[a:b+1], s[c:d+1])



