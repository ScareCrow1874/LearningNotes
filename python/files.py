from sys import argv # allow arguments on command line

script, filename = argv # two arguments

txt = open(filename)

print "First we will erase %r:" % filename
print "Press CTRL-C to stop it! Press RETURN to continue"

# read the input after the string "? " (this can be whatever you want)
raw_input("? ");

print "Opening the file..."
target = open(filename, 'r+') # open the file in read-write mode
# pay attention to where the pointer is at initially

'''
Pay attention:

Since you are using 'r+' mode, initially the file pointer will be at the start. If you do target.read(), the pointer will be moved to the end of the file. At that time if you truncate(), nothing will happen because there is no text after the pointer
'''

print "Here are your contents:"
print target.read()

print "---"
print "Truncating the file. Goodbye!"
target.truncate()

print "Now enter 3 lines"
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "Now writing your lines..."
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "Close the file"
target.close()
