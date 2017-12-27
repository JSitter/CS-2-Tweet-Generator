#!/usr/bin/env python3
import random
import time
import pprint


class MarkovChain:

    def __init__(self, corpus):
        '''
            TODO: Create Nth Order Chain
            TODO: Create 2nd Order chain first
        '''

        self.markov_structure = self.generate_second_order_markov_structure(corpus)

    def walk(self, steps):
        '''
            TODO: Return N step random walk
        '''
        #take first step
        markov_keys = list(self.markov_structure.keys())

        #get random first token
        word = markov_keys[random.randint(0, len(markov_keys)-1)]
        sentence = word

        #take additional steps
        for _ in range(1,steps):
            second_hist = self.markov_structure[word]
            word = self.stochastic_sample(second_hist)
            if not word:
                word = markov_keys[random.randint(0, len(markov_keys)-1)]
            sentence = sentence + " " + word
        
        return sentence
        


    def stochastic_sample(self, histogram):
        '''
            Return random word based on weight in histogram
        '''
        random_value = random.random()
        word_prob = 0
        if len(histogram) > 0:
            for type_tuple in histogram:
                word_prob += type_tuple[1]/len(histogram)
    
                if random_value <= word_prob:

                    return type_tuple[0]
        else:
            return False

    def generate_second_order_markov_structure(self, corpus):
       
        #list with word as key and value is word histogram
        markov_structure = {}
        corpus_length = len(corpus)
        
        #Corpus too small for 2nd order chain -- return error
        if corpus_length < 3:
            return 1

        following_token_position = 1

        for token in corpus:

            #if not at end of corpus
            if following_token_position < corpus_length:
                second_token = corpus[following_token_position]

                #look in markov structure for first token in digram
                if token in markov_structure:
                
                    second_hist = markov_structure[token]
                    
                    self.add_to_histogram(second_token, second_hist)

                    if second_token not in markov_structure:
                        markov_structure[second_token] = []

                else:
                    #if token not in markov structure add it
                    markov_structure[token] = [(second_token, 1)]

                    if second_token not in markov_structure:
                        markov_structure[second_token] = []

                following_token_position += 1
        
        return markov_structure

    def add_to_histogram(self, word, histogram):
        found = False
        index = 0
        if len(histogram) == 0:
            histogram.append((word, 1))

        for value in histogram:
            if value[0] == word:
                found = True
                new_value = (word, value[1] + 1)
                histogram[index] = new_value
            index += 1
        
        if not found:
            histogram.append((word, 1))
        
        return histogram

if __name__=="__main__":

    pseudo_corpus = [
        ("Always", "decide", "whether", "a", "class's", "methods", "and", "instance", "variables", "collectively", "attributes", "should", "be", "public", "or", "non-public"),
        ( "If", "in", "doubt", "choose", "non-public", "it's", "easier", "to", "make", "it", "public", "later", "than", "to", "make", "a", "public", "attribute", "non-public"),
        ( "Public", "attributes", "are", "those", "that", "you", "expect", "unrelated", "clients", "of", "your", "class", "to", "use", "with", "your", "commitment", "to", "avoid", "backward", "incompatible", "changes"),
        ( "Non-public", "attributes", "are", "those", "that", "are", "not", "intended", "to", "be", "used", "by", "third", 'parties', "you", "make", "no", "guarantees", "that", "non-public", "attributes", "won't", "change", "or", "even", "be", "removed"),
        ( "We", "don't", "use", "the", "term", "private", "here", "since", "no", "attribute", "is", "really", "private", "in", "Python", "without", "a", "generally", "unnecessary", "amount", "of", "work"),
        ( "Another", "category", "of", "attributes", "are", "those", "that", "are", "part", "of", "the", "subclass", "API", "often", "called", "protected", "in", "other", "languages"),
        ( "Some", "classes", "are", "designed", "to", "be", "inherited", "from", "either", "to", "extend", "or", "modify", "aspects", "of", "the", "class's", "behavior"),
    ]

    
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
    
    # #corpus = fw.create_corpus(settings["filename"])
    # mc = markov_chain(corpus)
    # print(mc.create(settings["len"]))

    print("Loading Corpus...")
    start_time = int(round(time.time()*1000))
    corpus = fw.create_corpus(settings["filename"])
    end_time = int(round(time.time()*1000))
    print("\nFinished in {}ms.".format(end_time-start_time))
    
    print("Creating Markov Chain...")
    start_time = int(round(time.time()))
    #Create markovchain datastructure in memory
    markov_chain = MarkovChain(corpus) 
    end_time = int(round(time.time()))
    print("\nMarkov chain generated in {}s.".format(end_time-start_time))

    start_time = int(round(time.time()*1000))
    sentence = markov_chain.walk(settings["len"])
    end_time = int(round(time.time()*1000))
    print("\nGenerated sentence in {}ms.".format(end_time-start_time))

    print(sentence)

