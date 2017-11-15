import stochastic_sample as sto
import pytest

def test_probabilities():
    sample = sto.stochastic_sample('small_sample_text.txt', 100000)

    hist = sto.create_histogram(sample.split(" "))
    
    print(hist["blue"]/len(sample.split(" ")))
    #assert hist["blue"]/len(sample.split(" ")) == False

