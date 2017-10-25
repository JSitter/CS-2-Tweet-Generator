import sys
import random


with open('american') as f:
    word_list = list(f)


sentence_length = int(sys.argv[1])
words = 0

while words < sentence_length:
    words += 1
    rand_int = random.randint(0, len(word_list))
    