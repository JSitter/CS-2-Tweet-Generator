import sys
from random import randint
import time
import collections

def create_anagram(word):
    with open("american") as f:
        word_list = list(f)

        #hashy_dict = collections.defaultdict(list)
        #letter_hashy = set(collections.Counter())

        # for c in word_list[763]:
        #     letter_hashy.add(c)
        # print(word_list[763])
        # print(letter_hashy)

        # use Default Dict to store words according to hash
        anagram_words = collections.defaultdict(list)

        for word in word_list:
            cleaned_word = word.strip("\n")
            #Create list of characters along with char count
            charlist = collections.Counter(list(cleaned_word))
            wordkey = ""
            #go over characters in order by most common
            #Add chars to wordkey
            for ch in charlist.most_common():
                wordkey += ch[0] + str(ch[1])

            anagram_words[wordkey] = word
        print(wordkey)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        start_time = int(round(time.time()*1000))
        create_anagram(sys.argv[1])
        end_time = int(round(time.time()*1000))
        print("Finished in {}ms".format(end_time - start_time))
    else:
        print("No value passed in for anagram word")