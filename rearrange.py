import sys
from random import randint

#create a set
words = set()
index = 0

while (len(words) != len(sys.argv)-1) and index<20:
    randomNum = randint(1, len(sys.argv)-1)
    words.add(sys.argv[randomNum])
    index += 1


print(" ".join(words))