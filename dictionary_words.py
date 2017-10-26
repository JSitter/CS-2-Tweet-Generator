import sys
import random

def create_sentence(num_of_words):
    '''Create a sentence given number of words in sentence'''
    #Open dictionary
    with open('american') as f:
        word_list = list(f)
    
        word_ct = 0 #Words generated
        sentence = ""

        while word_ct < sentence_length:
            word_ct += 1

            #Get random number and subract 1 to prevent out of bounds error
            rand_int = random.randint(0, len(word_list)) - 1 
            random_word = word_list[rand_int]

            #lowercase and remove newlines from input
            random_word = random_word.strip("\n").lower()
            
            #uppercase first letter of first word
            if word_ct == 1:
                sentence += random_word[0].upper() + random_word[2:]
            #Add Middle Words
            sentence += random_word + " "
            
            #Replace last space with period on last iteration
            if word_ct == sentence_length:
                sentence = sentence[:-1] + "."

        return sentence

#Call function and pass in parameters
if __name__=="__main__":
    sentence_length = int(sys.argv[1])

    print(create_sentence(sentence_length))