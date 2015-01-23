#This one we started on Tuesday 20.1.

from __future__ import division
import random
#alternatives:
#from random import choice
#from random import *


### TASK 1:
## modify the function below such that it takes a third parameter,
## which is a list of probabilities corresponding to the letters of
## the alphabet so rnd_seq(5,"acgt",[0.0,0.5,0.25,0.25]) should
## generate a random sequence of length 5, which has no a's and on
## average about half c's, quarter g's, quarter t's. The probabilities
## of course sum up to 1, so you can assume this in your solution.
##
## TASK 2:
##
## Write a function rnd_seq_matrix(l,alphabet,M) where M is a matrix
## of NxN probabilities (where N is the number of characters in the
## alphabet). The matrix is simply a list of lists. Every row in the
## matrix corresponds to one letter in the alphabet and specifies the
## probability distribution of the next letter.
##
## So calling rnd_seq_matrix(10,"ac",[[0.5,0.5],[0.95,0.05]]) would generate strings
## such that every a is followed by a or c with 50:50 chance, but a c is very unlikely
## to be followed by another c.

def rnd_seq(l,alphabet):
    """Generates a random sequence of length l drawn from alphabet"""
    #One-liner version:
    return "".join([random.choice(alphabet) for _ in range(l)])
    #Longer version of same:
    seq=""
    for i in range(l):
        seq+=random.choice(alphabet)
    return seq

## TASK 3:
##
## Modify the function below to get rid of the parameter w, i.e. you don't care what the
## length of the subsequence is. This will lead to the problem that a single c or g
## have 100% GC content, so you will be getting degenerate solutions. You need to find a way
## to balance the GC content and the length. Be creative in how you approach that. Some possible
## directions were shown on the lecture.

def max_gc_area(seq,w):
    """Finds the subsequence of seq of length w which has the highest GC content.
    In case there are several subsequences with the same GC content, returns the first one"""
    max_gc=None
    max_i=None
    for i in range(len(seq)-w+1):
        sub_seq=seq[i:i+w]
        gc=(sub_seq.count("g")+sub_seq.count("c"))/w
        if max_gc is None or gc>max_gc:
            max_gc=gc
            max_i=i
    assert max_gc is not None
    return max_i




s=rnd_seq(20,"acgt")+"cccca"
print s
print max_gc_area(s,4)

