#!/usr/bin/env python3


def return_evens(num_list):
    new_list = [num for num in num_list if num % 2 == 0] 
    return (new_list)

def make_exclamation(sentence_list):
    new_sentence = [f"{sentence}!" for sentence in sentence_list if sentence != None]
    return (new_sentence)