#opertaors in python
"""
Arithmatic Operators
+   Addition
-   Substraction
*   Multiply
/   Divide
//  floor divide
%   modulus(Reminder)
**  Exponential
"""

print(10+6)
print(10-6)
print(10*6)
print(10**6)
print(10//6)
print(10%6)
print(10/6)

'''
Comparison Operators
==  Equal To
!=  Not Equal To
>   Greater Than
<   Less Than
>=  Greater than or equal to
<=  less than or equal to

Returns the value in Boolean that is True or False
'''

print(10==5)
print(10>5)
print(10<5)
print(10>=5)
print(10<=5)

"""
Logical Operators

and Returns true if both the conditions are true
or  Returns True if one of the statement is true
not Reverses the condition
"""
age1 = 20
age2 = 18

if age1 or age2 == 1:
    print("OK")
else:
    print("Yooo")

if age1 and age2 == 20:
    print("Done")
else:
    print("Chal phutt")

if age1 + age2 and age1 - age2 == 200:
    print("Neh")
else:
    print("Yupsio")

