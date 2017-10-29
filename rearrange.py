import sys
from random import randint
def randomize_words(words):
    #create a set
    words = set()

    while (len(words) != len(sys.argv)-1):
        randomNum = randint(1, len(sys.argv)-1)
        words.add(sys.argv[randomNum])

    print(" ".join(words))