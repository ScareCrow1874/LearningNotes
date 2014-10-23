bob = "Bob"
cid = "Cid"
age = "14"
year = 1995

print "My age is %r" %age
print "My age is %s" %age
print "The yer is %d " %year
print "people: %s, %s" %(bob, cid)
print "I like",bob, "yea\n\n" #You do not print spaces around the variable?

from sys import argv

script, first, second, third = argv
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third


from os.path import exists
