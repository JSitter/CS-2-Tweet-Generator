#!/usr/bin/env python3
import random

class nth_markov_chain:
    def __init__(self, corpus):
        self.corpus = corpus
    
    def create_chain(self, nth_order):
        