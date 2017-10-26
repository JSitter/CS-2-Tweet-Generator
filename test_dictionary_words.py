import pytest
import time
import dictionary_words as rand_words

def test_sentence_word_len():
    start_time = int(round(time.time()*1000))
    sentence = rand_words.create_sentence(10)
    end_time = int(round(time.time()*1000))

    print(end_time - start_time)
    assert len(sentence.split(' ')) == 10