"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    list = []
    for item in items:
        list.append(str(item))
    for i in list:
        count = 0
        for x in list:
            if (str(i) == str(x)):
                # list.remove(x)
                count += 1
        frequencies[i]= count
        # list.remove(i)
    return frequencies
