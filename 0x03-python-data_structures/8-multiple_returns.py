#!/usr/bin/python3

def multiple_returns(sentence):
    sentence_tuple = ()
    if len(sentence) == 0:
        sentence_tuple = None
    else:
        sentence_tuple = len(sentence), sentence[0]
    return sentence_tuple
