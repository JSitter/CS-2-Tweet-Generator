#!/usr/bin/env python3
import sys

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
                #Check if word has been encountered before
                if word in histogram:
                    #Add one to existing entry
                    histogram[word] += 1
                else:
                    #Else create new entry
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

            #getting words in document
            for word in word_list:
                pass
                #Check if word has been encountered before
                    #Add one to existing entry
                #Else create new entry

def create_tuple_list_histogram(filename):
    '''
        Create a histogram and return as a list of tuples
    '''
    pass

if __name__ == "__main__":
    default_file_name = 'small_sample_text.txt'

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = default_file_name

    print(create_histogram_dictionary(filename))