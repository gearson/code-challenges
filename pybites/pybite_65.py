#%%
import itertools
import os
import urllib.request
import string
import random

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])
#%%

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}

#%%
draw = 'd r t e k k e'.split()

def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    words = [''.join(combi)
             for combi in _get_permutations_draw(draw)]  
    valid_words = [word for word in words if word in dictionary]
    print(list(valid_words))


def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""       
    for i in range(1, len(draw)+1):
        yield from list(itertools.permutations(draw,i))

get_possible_dict_words(draw)

#%%
# def get_possible_dict_words(draw):
#     """Get all possible words from a draw (list of letters) which are
#        valid dictionary words. Use _get_permutations_draw and provided
#        dictionary"""
#     permutations = [''.join(word).lower()
#                     for word in _get_permutations_draw(draw)]
#     return set(permutations) & set(dictionary)


# def _get_permutations_draw(draw):
#     """Helper to get all permutations of a draw (list of letters), hint:
#        use itertools.permutations (order of letters matters)"""
#     for i in range(1, 8):
#         yield from list(itertools.permutations(draw, i))

# #%%
