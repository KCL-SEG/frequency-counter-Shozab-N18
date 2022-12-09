"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    list = items
    for i in list:
        count = 0
        for x in list:
            if (i == x):
                list.remove(x)
                count += 1
        frequencies.update(i,count)
        list.remove(i)
    return frequencies
