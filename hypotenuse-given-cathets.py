import math # You can also use from math import sqrt
            # To avoid the math. prefix

c1 = float(input("Enter the length of the first cathet: "))
c2 = float(input("Enter the length of the second cathet: "))

print("The hypotenuse is", math.sqrt(c1**2 + c2**2))
