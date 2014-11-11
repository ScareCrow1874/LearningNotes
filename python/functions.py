from sys import argv

def read_words():
    '''This function lets user input words'''
    words = raw_input('> (separate with space) ');
    return words.split(' ');

def dum_loop(max):
    '''prints all numbers till max'''
    for i in range(0, max):
        print i

words = read_words();
print sorted(words)
dum_loop(20)
