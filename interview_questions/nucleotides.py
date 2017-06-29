"""
Generate all possible nucleotides of length K from the DNA alphabet. You are
not allowed to use any imports.

What is the time complexity of the algorithm?
"""


def all_seqs(K, string):
    alphabet = 'ATGC'

    if K == 0:
        return string
    else:
        return all_seqs(K-1, string + alphabet[0]), \
               all_seqs(K-1, string + alphabet[1]), \
               all_seqs(K-1, string + alphabet[2]), \
               all_seqs(K-1, string + alphabet[3])


all_seqs(6, '')
