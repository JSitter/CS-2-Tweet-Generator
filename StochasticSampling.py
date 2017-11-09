#!/usr/bin/env python3
import sys
from random import random
import time

class StochasticSample:

    def __init__(filename, sentence_lenth):
        self.sourceText = 

    def createDictogram(word_list):
        '''
            Create Histogram of word freqency
        '''
        pass
    
    def getWordsFromText(filename):
        '''
            Get words from Text File
        '''
        pass
    
    def santizeText(word_list):
        '''
            Santize words
        '''
        pass
    

if __name__=="__main__":
    defaultFileName = "small_sample_text.txt"

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = default_file_name
    
    if len(sys.argv) > 2:
        sentence_len = int(sys.argv[2])
    else:
        sentence_len = 5
    start_time = int(round(time.time()*1000))
    #Run sampling here
    
    end_time = int(round(time.time()*1000))
    print("Ran in {}ms".format(end_time - start_time))