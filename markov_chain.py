#!/usr/bin/env python3
from random import random

class markov_chain:

    def __init__(self, corpus):
        self.corpus = corpus

    def create(self, sentence_len):
        '''
            Create Markov Chain
        '''
        pass

    def createHistogram(self, wordList):
        '''
            Create Dictionary Histogram of word freqency
        '''
        histogram = {}
        for word in wordList:
            if word in histogram:
                histogram[word] += 1
            else:
                histogram[word] = 1

        return histogram    


if __name__=="__main__":

    import sys
    import file_wrangler as fw
    settings = {}
    parameters = sys.argv[1:]

    print(len(parameters))
    #No parameters passed in
    if len(parameters) == 0:
        settings["filename"] = "small_sample_text.txt"
        settings["len"] = 5
    
    #Only filename passed in
    elif len(parameters) == 1:
        settings["filename"] == parameters[0]
        settings["len"] == 5
    else:
        settings["filename"] = parameters[0]
        settings["len"] = parameters[1]
    
    print(fw.create_corpus(settings["filename"]))