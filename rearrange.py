import sys
from random import randint

#create a set
words = set()


while (len(words) != len(sys.argv)-1):
    randomNum = randint(1, len(sys.argv)-1)
    words.add(sys.argv[randomNum])

print(" ".join(words))