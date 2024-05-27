#!/usr/bin/env python3

def return_evens(num_list):
     evens = [n for n in num_list if n%2 == 0]
     return evens


    

def make_exclamation(sentence_list):
    exclamated_sentences = (sentence + "!" for sentence in sentence_list)
    return exclamated_sentences

print (make_exclamation(["I like computers","I require coffee","Live long and prosper",]))
print (return_evens([1,2,3,4,5,6,7,8,9,0,12]))