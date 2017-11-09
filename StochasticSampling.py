#!/usr/bin/env python3
import sys
from random import random
import time

class StochasticSample:

    def __init__(self, filename, sentenceLength):
        self.sourceText = self.getStringFromFile(filename)
        self.sourceText = self.santizeText(self.sourceText)
        self.wordList = self.createWordList(self.sourceText)
        print("listogram", self.createListogram(self.wordList))

    def createDictogram(self, wordList):
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

    def createListogram(self, wordList):
        '''
        Create a histogram and return as a list of lists
        '''
        
        histogram = list()
        for word in wordList:
            #Get length of histogram
            histLen = len(histogram)
            print(word)
            #if first run insert into histogram
            if(histLen < 1):
                histogram.append([word, 1])
            #else run normally
            else:
                index = 0
                wordFound = False
                for element in histogram:
                    
                    #If word has been encountered before add to count
                    if element[0] == word:
                        histogram[index][1] += 1
                        wordFound = True
                        break
                    index += 1
                #Check if word was found
                if not wordFound:
                    histogram.append([word, 1]) 
        return histogram  

    def getStringFromFile(self, filename):
        '''
            Get string of words from Text File
        '''
        with open(filename) as f:
            return f.read()
    
    def santizeText(self, sourceText):
        '''
            Santize words
        '''
        acceptedChars = set("'\nabcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        return ''.join(filter(acceptedChars.__contains__, sourceText)).replace("\n", " ").lower()
    
    def createWordList(self, sourceText):
        '''
            Create list of words
        '''
        splitText = sourceText.split(" ")
        #Remove any empty values
        for item in splitText:
            if item == "":
                splitText.pop(splitText.index(item))
        return splitText


if __name__=="__main__":
    defaultFileName = "small_sample_text.txt"

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = defaultFileName
    
    if len(sys.argv) > 2:
        sentenceLen = int(sys.argv[2])
    else:
        sentenceLen = 5
    start_time = int(round(time.time()*1000))
    #Run sampling here
    sample = StochasticSample(defaultFileName, sentenceLen)
    
    #print(sample.wordList)
    end_time = int(round(time.time()*1000))
    print("Ran in {}ms".format(end_time - start_time))