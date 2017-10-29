#!/usr/bin/env python3

import sys
def create_histogram(filename):
    '''
        Create Histogram of word frequency in file
    '''
    with open(filename) as f:
        text_lines = list()
        histogram = {}

        
        for line in f.readlines():
            word_list = line.split(" ")
            for word in word_list:
                word = word
                if word in histogram:
                    histogram[word] += 1
                else:
                    histogram[word.strip(" \n")] = 1
        return histogram



if __name__ == "__main__":
    default_file_name = 'small_sample_text.txt'

    if len(sys.argv) > 1:
        hist = create_histogram(sys.argv[1])
    else:
        hist = create_histogram(default_file_name)

    print(hist)