import sys
import random

def create_sentence(num_of_words):
    '''Create a sentence given number of words in sentence'''
    with open('american') as f:
        word_list = list(f)
    
        word_ct = 0 #Words generated
        sentence = ""

        while words < sentence_length:
            words += 1
            rand_int = random.randint(0, len(word_list))
            random_word = word_list[rand_int]
            #uppercase first letter of first word
            # if words == 1:
            #     sentence += random_word

            sentence += word_list[rand_int] + " "
        return sentence

#Call function and pass in parameters
if __name__= "__main__":
    sentence_length = int(sys.argv[1])

    print(create_sentence(sentence_length))