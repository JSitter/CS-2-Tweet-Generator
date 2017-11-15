import pytest
from markov_chain import markov_chain as mc
import file_wrangler as fw

def test_markov_against_fish():

    right_answer = {
        "one" : {"fish":1},
        "fish": {"two": 1, "red":1, "blue": 1, "it's":1},
        "two": {"fish":1},
        "red": {"fish":1},
        "blue": {"fish":1},
        "it's": {"one":1}
    }
    corpus = fw.create_corpus('small_sample_text.txt')

    chain = mc(corpus)
    
    print(chain.generate_markov_structure())
    assert chain.generate_markov_structure == right_answer