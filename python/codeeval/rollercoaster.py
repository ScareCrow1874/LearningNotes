"""
To be, or not to be: that is the question.
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles,
And by opposing end them? To die: to sleep.

To Be, Or NoT tO bE: tHaT iS tHe QuEsTiOn.
WhEtHeR 'tIs NoBlEr In ThE mInD tO sUfFeR
ThE sLiNgS aNd ArRoWs Of OuTrAgEoUs FoRtUnE,
Or To TaKe ArMs AgAiNsT a SeA oF tRoUbLeS,
AnD bY oPpOsInG eNd ThEm? To DiE: tO sLeEp.
"""

import sys
from sys import argv

script, filename = argv

with open(filename) as f:
    for line in f:
        chars = list(line) # break the line into characters
        upper = True
        for ch in chars:
            if ch.isalpha(): # check if it is alphabetic (built-in, for str and char)
                if upper:
                    sys.stdout.write(ch.upper())
                    upper = False
                else:
                    sys.stdout.write(ch.lower())
                    upper = True
            else:
                sys.stdout.write(ch)

        
        
