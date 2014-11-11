"""
CodeEval - Fizz Buzz

Players generally sit in a circle. The first player says the number “1”, and each player says next number in turn. However, any number divisible by X (for example, three) is replaced by the word fizz, and any divisible by Y (for example, five) by the word buzz. Numbers divisible by both become fizz buzz. A player who hesitates, or makes a mistake is eliminated from the game.

Write a program that prints out the final series of numbers where those divisible by X, Y and both are replaced by “F” for fizz, “B” for buzz and “FB” for fizz buzz. 
"""

import sys
from sys import argv


script, filename = argv

with open(filename) as infile:
    for line in infile:
        numbers = line.split(' ')
        x = int(numbers[0])
        y = int(numbers[1])
        count = int(numbers[2])

        #count
        for i in range (1, count+1):
            if i % x == 0:
                sys.stdout.write("F")
            if i % y == 0:
                sys.stdout.write("B")
            if i % y != 0 and i % x != 0:
                sys.stdout.write(str(i))
            
            #no trailing space
            if i != count:
                sys.stdout.write(" ")
        
        #nextline
        sys.stdout.write("\n")

