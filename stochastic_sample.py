#!/usr/bin/env python3
import sys

def stochastic_sample(filename, sentence_length):
    words = get_words_from_text(filename)
    #num_words = len(words)
    create_histogram(words)
    print(len(words))


def create_histogram(word_list):
    '''
        Create Histogram of word frequency in file
    '''
    histogram = {}

    for word in word_list:
        word = sanitize(word)
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram

def get_words_from_text(filename):
    '''
        Get words from text file
    '''
    with open(filename, 'r') as f:
        text = f.read()

    return text.split(" ")
        
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

    stochastic_sample(filename, sentence_len)
