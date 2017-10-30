#!/usr/bin/env python3
import sys

def create_histogram_dictionary(filename):
    '''
        Create Histogram of word frequency in file
    '''
    with open(filename) as f:
        text_lines = list()
        histogram = {}

        
        for line in f.readlines():
            word_list = line.split(" ")
            for word in word_list:
                if word in histogram:
                    histogram[word] += 1
                else:
                    histogram[word] = 1
        return histogram

def create_list_histogram(filename):
    '''
        Create a histogram in a list of lists
    '''
    with open(filename) as f:
        histogram = list()
        
        for line in f.readlines():
            word_list = line.split(' ')
            for word in word_list:
                pass


if __name__ == "__main__":
    default_file_name = 'small_sample_text.txt'

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = default_file_name

    print(create_histogram_dictionary(filename))