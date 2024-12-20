# comments in python
# These are single line comments

'''
Another example of multiline comments
using single quotes.
'''

"""
Example with dobule quotes
in python
"""

#docstrings in python

def interval_count_printer(n1, n2):
    """
    This function prints 
    numbers in given numbers range 

    returns:
    numbers
    """
    for i in range(n1, n2):
        print(i)

interval_count_printer(1,11)