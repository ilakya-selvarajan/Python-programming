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

#Random nucleotide generator with given probability
def rnd_seq_prob(l,seq,choices):
   total = sum(prob for nucleotide, prob in choices)   #total=1.0 because the prob sum up to 1
   r = random.uniform(0, total)                         #generating a number between 0 and 1
   cutoff = 0
   for nucleotide, prob in choices:
      if cutoff + prob > r:                                   
         return nucleotide
      cutoff += prob

def getseq(length, choices):
    outstring = ""
    for i in range(length):
        outstring += rnd_seq_prob(length, s, choices)       
    return outstring
    
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

def rnd_seq_matrix(l,alphabet,M):
    #total = sum(prob for nucleotide, prob in choices)   #total=1.0 because the prob sum up to 1
   outstring2=''
   current_letter = random.choice(alphabet)
   current_index = alphabet.index(current_letter)
   outstring2+=current_letter
   r1 = random.uniform(0, 1)                         #generating a number between 0 and 1
   cutoff=0
   
   #power_matrix = zip(alphabet,M)
   for i in range(0,l-1):
        for prob in M[current_index]:
            r2 = random.uniform(0, 1)
            if cutoff + prob > r2:  
                
                current_index=M[current_index].index(prob)
                outstring2+=alphabet[M[current_index].index(prob)]
                break
            cutoff += prob
   return outstring2
        
            
  
def rnd_seq(l,alphabet):
    """Generates a random sequence of length l drawn from alphabet"""
    #One-liner version:
    return "".join([random.choice(alphabet) for _ in range(l)])
    #Longer version of same:
    seq=""
    for i in range(l):
        seq+=random.choice(alphabet)
    return seq
    #pass

## TASK 3:
##
## Modify the function below to get rid of the parameter w, i.e. you don't care what the
## length of the subsequence is. This will lead to the problem that a single c or g
## have 100% GC content, so you will be getting degenerate solutions. You need to find a way
## to balance the GC content and the length. Be creative in how you approach that. Some possible
## directions were shown on the lecture.

def max_gc_area(seq):
    length = len(seq)
    list1 = []
    dict2={}
    for i in xrange(length):
        for j in xrange(i,length):
            list1.append(seq[i:j + 1]) 
    alist=list(set(list1))                      #generate all possible combination of the string
    for string in alist:
        score = ((string.count('g')+string.count('c'))**2) / len(string)  #Set a score for each substring
        gc_cont = (string.count('g')+string.count('c'))/len(string)        #calculate the GC% 
        dict2[string] = (score, gc_cont)
        #dict2[string]=(string.count('g')+string.count('c')),(string.count('g')+string.count('c'))/len(string)  #score,GC%
    list2=sorted(dict2.items(), key=lambda x: x[1])                     #substrings sorted based on score
    
    return list2[-1][0],list2[-1][1][0],list2[-1][1][1]                 #returning the substring with highest score and GC%

sample_size = 10   #it comes close to the given probability when the sample size increases
seq_length=5
choice = [('a', 0.0), ('c', 0.5), ('g', 0.25), ('t', 0.25)]
choice2 = [[0.5,0.0,0.25,0.25],[0.0,0.25,0.5,0.25],[0.25,0.25,0.5,0.0],[0.25,0.5,0.0,0.25]]

prob_dict = {}
s=rnd_seq(20,"acgt")+"cccca"
print "\n\n","Randomly generated sequence:",s,"\n\n"

matrix_seq = rnd_seq_matrix(seq_length,'acgt',choice2)

sub_string_highGC=max_gc_area(s)
for sample in range(sample_size):
    str = getseq(seq_length, choice)
    #print(str)
    for char in str:
        try:
            prob_dict[char] += 1
        except KeyError:
            prob_dict[char] = 0

print "Task1:",str,"(One example from the 10 generated sequences)\n\n"
print "Nucleotide probabilities of", sample_size, "generated sequences"

for key in prob_dict:
    print("Nucleotide : %s , Prob: %f" % (key, prob_dict[key]/(sample_size*seq_length)) )
print "\n\n"
print "Task 2:",matrix_seq,"(generated with the prob. matrix)"
print "\n\nTask 3:(GC content of the substring with highest CG%)\n"
print "The substring with highest GC content balanced with its length",sub_string_highGC[0],"with score of",sub_string_highGC[1],"and GC%:",sub_string_highGC[2],"\n\n"