import gzip
from Bio.Cluster import *
from Bio import Phylo


f1=[]
names=[]
def tonewick(node,tree,words):
    order1,order2=[],[]
    nNodes = len(tree) 
    nElements = nNodes + 1 
    neworder = numpy.zeros(nElements)
    clusterids = numpy.arange(nElements)    
    for i in range(nNodes): 
           i1 = tree[i].left 
           i2 = tree[i].right 
           
           while i1 < 0: 
                i1 = i1+1
                i1 = tree[i].left 
           else: 
               order2.append(words[i1])
               print words[i1], words[i1-1]
           # if i2 < 0: 
               # order2 = nodeorder[-i2-1] 
               # count2 = nodecounts[-i2-1] 
           # else: 
               # order2 = node[i2] 
               # count2 = 1 
    print order2
    
f = gzip.open('words.txt.gz', 'rb')
file_content = f.readlines()
for files in file_content:
    f2=[]
    file1= files.strip("\n")
    
    w,v=file1.split("\t")
    #v=int(v)
    names.append(w)
    numbers=v.split(" ")
    f2.append(numbers)
    f1.append(f2)

f.close()
f3=[]
for fst in f1:
    for snd in fst:
        f3.append(map(float, snd))

      
            
dict22={}  
dict23={}        
data1=kcluster(f3,nclusters=7,method='a',dist='e')
print data1
list11=data1[0]
for i in range (0,len(list11)):
    dict22[names[i]]=list11[i]


for keys,values in dict22.iteritems():
    try:
        dict23[values].append(keys)
    except KeyError:
        dict23[values] = [keys]

#print dict23

for keys,values in dict23.iteritems():
    print "cluster",keys,"=",values

data2=treecluster(data=f3, mask=None, weight=None, transpose=0, dist='e', method='a', distancematrix=None)
data2.scale()
print data2
print data2[0].left
print len(data2)
tonewick(-21,data2,names)
