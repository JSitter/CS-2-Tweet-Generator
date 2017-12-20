#!/usr/bin/env python3
import random

class markov_chain:

    def __init__(self, corpus):
        self.corpus = corpus

    def create(self, sentence_len):
        '''
            Create Markov Chain
        '''
        markov_structure = self.generate_markov_structure()
        sentence = []
        #Choose first word randomly
        rand_int = random.randrange(len(self.corpus))
        sentence.append(self.corpus[rand_int])

        while len(sentence) < sentence_len:
            wrd_hist = markov_structure[sentence[-1]]
            new_word = self.stochastic_sample(wrd_hist)

            sentence.append(new_word)
        sentence_string =  " ".join(sentence)
        sentence_string = sentence_string[0].capitalize() + sentence_string[1:] + "."
        return sentence_string

    def stochastic_sample(self, histogram):
        '''
            Return random word based on weight in histogram
        '''
        random_value = random.random()
        word_prob = 0
        for word in histogram:
            word_prob += histogram[word]/len(histogram)
 
            if random_value <= word_prob:

                return word

    def generate_markov_structure(self):
        #list with word as key and value is histogram of words that follow
        markov_structure = {}
        index = 0
        #loop through corpus
        while index < len(self.corpus):
            #if word has been encountered add next word to histogram

            if self.corpus[index] in markov_structure:
                
                next_word_dict_hist = markov_structure[self.corpus[index]]
                #check for last word and add first word if at end

                if index+1 == len(self.corpus):
                    #check if first word is in and add one if yes
                    if self.corpus[0] in markov_structure[self.corpus[index]]:
                        markov_structure[self.corpus[index]][self.corpus[0]] += 1
                    else:
                        #add first word
                        markov_structure[self.corpus[index]][self.corpus[0]] = 1

                #not at end add next word to histogram
                else:
                    #if next word has been encountered add one to histogram counter
                    if  self.corpus[index+1] in markov_structure[self.corpus[index]]:
                        markov_structure[self.corpus[index]][self.corpus[index+1]]+=1
                    #else add word to histogram
                    else:
                        markov_structure[self.corpus[index]][self.corpus[index+1]] = 1
                        
            #else insert into histogram
            else:
                #if on last word add first word to histogram
                if index+1 == len(self.corpus):
                    markov_structure[self.corpus[index]] = {self.corpus[0]:1}
                #else add next word to histogram
                else:
                    markov_structure[self.corpus[index]] = {self.corpus[index+1]: 1}
            
            index += 1
        return markov_structure

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
   
    #No parameters passed in
    if len(parameters) == 0:
        settings["filename"] = "small_sample_text.txt"
        settings["len"] = 5
    
    #Only filename passed in
    elif len(parameters) == 1:
        settings["filename"] = parameters[0]
        settings["len"] = 5
    else:
        settings["filename"] = parameters[0]
        settings["len"] = int(parameters[1])
    
    #corpus = fw.create_corpus(settings["filename"])
    corpus = fw.create_corpus(settings["filename"])

    mc = markov_chain(corpus)

    print(mc.create(settings["len"]))