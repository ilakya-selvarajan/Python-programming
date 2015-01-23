from __future__ import division
import random

#Random nucleotide generator
def rnd_seq(l,alphabet):
    return "".join([random.choice(alphabet) for _ in range(l)])

#Random nucleotide generator with given probability
def rnd_seq_prob(l,alphabet,prob):
    pass


print rnd_seq(6,'acgt')

def sub_s_count(seq,l):
    substrings=[]
    gc_content=[]
    string=[]
    dict2={}
    for i in range(0,len(seq)-l+1):
        print seq[i:i+l]
        substrings.append(seq[i:i+l])
    for string in substrings:
        gc_content.append((string.count('g')+string.count('c'))/l)
        dict2[string]=(string.count('g')+string.count('c'))/l
    #zipped_list=zip(substrings,gc_content)
    #print gc_content
    print 'the highest gc content:',max(gc_content)
    for key,value in dict2.items():
        if value==max(gc_content):
            print 'the index of',key,'is',seq.index(key)
    

seq=rnd_seq(25,'acgt')
print seq
sub_s_count(seq,7)
