import gzip
from Bio.Cluster import *
f1=[]

def tonewick(tree):
    pass

f = gzip.open('words.txt.gz', 'rb')
file_content = f.readlines()
for files in file_content:
    f2=[]
    file1= files.strip("\n")
    
    w,v=file1.split("\t")
    #v=int(v)
    numbers=v.split(" ")
    f2.append(numbers)
    f1.append(f2)

f.close()
f3=[]
for fst in f1:
    for snd in fst:
        f3.append(map(float, snd))

      
            
            #print trd
#print f3       
data1=kcluster(f3,nclusters=3,method='a',dist='e')

data2=treecluster(data=f3, mask=None, weight=None, transpose=0, dist='e', method='m', distancematrix=None)
print data2
