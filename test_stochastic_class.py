import pytest
import StochasticSampling

def test_Class_Creation():
    assert createSampleClass()

def test_sanitizeText():
    clss = createSampleClass()
    

def createSampleClass():
    return StochasticSampling("small_sample_text.txt", 5)