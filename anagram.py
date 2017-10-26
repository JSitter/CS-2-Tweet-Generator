import sys
from random import randint
import time

def create_anagram(word):
    pass

if __name__ == "__main__":
    if len(sys.argv) > 1:
        start_time = int(round(time.time()*1000))
        create_anagram(sys.argv[1])
        end_time = int(round(time.time()*1000))
        print("Finished in {}ms".format(end_time - start_time))
    else:
        print("No value passed in for anagram word")