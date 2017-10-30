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

def create_tuple_list_histogram(filename):
    '''
        Create a histogram in a list of lists
    '''
    with open(filename) as f:
        histogram = list()
        
        for line in f.readlines():
            word_list = line.split(' ')

            #getting words in document
            for word in word_list:


                #sanitize data
                word = sanitize(word)

                #Get length of histogram array
                index_len = len(histogram)

                #if first run add word to array
                if(index_len < 1):
                    histogram.append((word, 1))
            
                #else do this
                else:
                    index = 0
                    
                    word_found = False
                    
                    #Iterate over histogram
                    while index < index_len:
                        
                        #Check if word has been encountered before
                        if histogram[index][0] == word:
                            #Add one to existing entry
                            histogram[index] = ( word, 1 + histogram[index][1] )
                            word_found = True
                            break

                        #Move to next index
                        index += 1
                                            
                    #Check if word was found
                    if not word_found:
                        histogram.append((word, 1))
        return histogram

def create_list_list_histogram(filename):
    '''
        Create a histogram and return as a list of lists
    '''
    pass

def sanitize(word):
    '''
        Clean words and return *filtered* for content to remove
    '''
    return word

if __name__ == "__main__":
    default_file_name = 'small_sample_text.txt'

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = default_file_name

    print(create_tuple_list_histogram(filename))