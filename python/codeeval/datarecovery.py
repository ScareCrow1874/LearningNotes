"""
Data Recovery:

Your friends decided to make a fun of you. They've installed a script to your computer which shuffled all of the words within a text. It was a joke, so they've left hints for each sentence which allow you to easily rebuild your data. The challenge is to write a program which reconstructs each sentence out of a set of words, you need to find out how to use a given hint and print out the original sentences. 

Notice: there will be at most one index that is missing in the number list, otherwise the puzzle is insolvable
"""

import sys
from sys import argv

script, filename = argv

def sumRange(a, b):
    result = 0
    for i in range(a,b):
        result += i
    return result

with open(filename) as infile:
    for line in infile:
        mix = line.split(';')
        words = mix[0].split(' ')
        order = mix[1].split(' ')        
        
        sentence = [None] * len(words) # this is constructing a list of fixed length
        trick = sumRange(0, len(words))
        for k in range(0, len(order)):
            sentence[int(order[k])-1] = words[k]
            trick -= int(order[k])-1
            
        if len(words) > len(order):
            last = words[-1] # last element
            sentence[trick] = last

        result = ""
        for w in sentence:
            result += w + " "
        result = result.strip()
        print result
