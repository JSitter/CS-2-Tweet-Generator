#!/usr/bin/env python3
import sys

def stochastic_sample(sample_text_filename, len):
    print(get_words_from_text(sample_text_filename))

def get_words_from_text(filename):
    '''
        Get words from text file
    '''
    with open(filename, 'r') as f:
        text = f.read()

    return text.split(" ")

def create_histogram_dictionary(filename):
    '''
        Create Histogram of word frequency in file
    '''
    with open(filename) as f:
        text_lines = list()
        histogram = {}

        #Get all words in file
        for line in f.readlines():
            word_list = line.split(" ")
            for word in word_list:
                word = sanitize(word)
                #Check if word has been encountered before
                if word in histogram:
                    #Add one to existing entry
                    histogram[word] += 1
                else:
                    #Else create new entry
                    histogram[word] = 1
        return histogram
        
def sanitize(word):
    '''
        Clean words and return *filtered* for content to remove
    '''
    if word == "\n":
        word = "*filtered*"
    
    word = word.strip(".,:\n").lower()
    
    return word

if __name__ == "__main__":
    default_file_name = 'small_sample_text.txt'

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = default_file_name
    
    if len(sys.argv) > 2:
        sentence_len = sys.argv[2]
    else:
        sentence_len = 5

    print(stochastic_sample(filename, sentence_len))
