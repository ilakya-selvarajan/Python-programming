import Bio.kNN as knn



FL=4

def txt2dim(s):
    """Given a sequence "s", calculate
    its decimal value assuming that A=0 C=1 G=2 T=3
    so eg ACCT is 3*(4**0)+1*(4**1)+1*(4**2)+0*(4**3)
    """
    digits="ACGT"
    res=0
    s=s[::-1] #reverse s
    #print s
    for power,digit in enumerate(s):
        res+=digits.index(digit)*(4**power)
    return res
        

def seq2fv(seq):
    """Given a sequence seq, return a 256-dimensional
    feature vector"""
    l=4
    #print seq
    fv=[0.0]*(4**FL)
    substrings=[]
    for i in range(0,len(seq)-l+1):
        #print seq[i:i+l]
        substrings.append(seq[i:i+l])
        dimension=txt2dim(seq[i:i+l])
        #print dimension
        fv[dimension]=1.0
    #fv=[0 for _ in range(4**FL)]
    
    return fv

def get_data(f_name):
    """Read the data from file_name
    return list of feature vectors, and list of classes"""
    holder2=[]
    vectors=[]
    classes=[]
    file1 = open(f_name, 'rt')
    holder=file1.readlines()
    for lines in holder:
        c,s=lines.strip().split(' | ')
        classes.append(c)
        vectors.append(seq2fv(s))
    #print holder2[0][1]
    #for i in range(0,len(holder2)):
    #    vector1.append(seq2fv(holder2[i][1]))
    #print classes,vectors
    return classes,vectors

seq='AAAATTTT'
#print seq2fv(seq)
tr_cl,tr_vector=get_data('bac_vs_hum_train.vw')
print tr_vector[0]
knn.train(tr_cl,tr_vector,3)
