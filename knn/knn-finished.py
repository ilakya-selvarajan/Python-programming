from __future__ import division
import Bio.kNN as knn
import sys
from math import sqrt

V={'A':0,'C':1,'G':2,'T':3}
D=4 #The length of the substrings to be used as features

def feat2num(f):
    """Calculates unique dimension in the feature vector for the
    substring f."""
    f=f[::-1]
    res=0
    for power,c in enumerate(f):
        res+=V[c]*(4**power)
    return V[f[0]]*(4**3)+V[f[1]]*(4**2)+V[f[2]]*4+V[f[3]]

def ex2vec(ex):
    """Turns a single example into a feature vector"""
    res=[0.0 for _ in range(4**D)] #Feature vector, initialize with 0's
    c,feat=ex.split(" | ") #class,example
    for i in range(len(feat)-D+1):
        substr=feat[i:i+D] #substring of length D
        dimension=feat2num(substr) #...translate into a unique dimension
        res[dimension]+=1.0 #...and increase its count by 1
    #print c,res    
    return c,res #returns the class and the feature vector
    
def read_data(f_name):
    """Takes a file name and returns a list of classes and list of feature vectors"""
    vectors=[]
    classes=[]
    with open(f_name,"rt") as f:
        for line in f:
            line=line.rstrip()
            c,v=ex2vec(line)
            classes.append(c)
            vectors.append(v)
    #print classes, vectors        
    return classes,vectors


if __name__=="__main__": #This is only executed if you run the program directly, as opposed to importing it as a module
    correct=0 #counter for the accuracy
    total=0
    cs,vs=read_data("bac_vs_hum_train.vw") #read in the training data
    print cs[0],vs[0]
    classifier=knn.train(vs,cs,3) #let us get us a 3-NN classifieer
    # test_cs,test_vs=read_data("bac_vs_hum_test.vw") #...and read in the test data so we see how we're doing
    # for corr_c,x in zip(test_cs,test_vs):
        # pred_c=knn.classify(classifier,x)
        # if pred_c==corr_c:
            # correct+=1
        # total+=1
        # print "%.2f (%d)  '%s' '%s'"%(correct/total*100,total,pred_c,corr_c)
        
