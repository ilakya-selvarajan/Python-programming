import gzip
from Bio.Cluster import *
from Bio import Phylo


def tonewick(node,tree,words):
    
    nNodes = len(tree) 
    nElements = nNodes + 1 
    neworder = numpy.zeros(nElements)
    #tuple1=()
    list1=[4,5]
    list2=[] 
    
    for i in xrange(len(tree)-1, -1, -1):
           i1 = tree[i].left 
           i2 = tree[i].right
           if i1<=0 and  i2<=0:
                if i1==i2+1 or i1==i2-1:
                    if i2+1==i1:
                        #print (words[i1],words[i2]),i1+1
                        tuple1=(i1,i2)
                        list2.append(tuple1)
                        list3.append(i1+1)
                        clusterids.remove(i1)
                        clusterids.remove(i2)
           if i1>=0 and i2>=0: 
                if i1==i2+1 or i1==i2-1:
                    if i2+1==i1:
                        #print (words[i1],words[i2]),i1+1
                    #print (words[i1],words[i2]),(i1,i2)
                        tuple1=(i1,i2)
                        list2.append(tuple1)
                        list3.append(i1+1)
                        clusterids.remove(i1)
                        clusterids.remove(i2)
             
    
    #print order2
    return list2,list3,clusterids
clusterids = range(-21, 22)
f1=[]
names=[]
list3=[]
    
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
#print data1
list11=data1[0]
for i in range (0,len(list11)):
    dict22[names[i]]=list11[i]

for keys,values in dict22.iteritems():
    try:
        dict23[values].append(keys)
    except KeyError:
        dict23[values] = [keys]

#print dict23

# for keys,values in dict23.iteritems():
    # print "cluster",keys,"=",values

data2=treecluster(data=f3, mask=None, weight=None, transpose=0, dist='e', method='a', distancematrix=None)
data2.scale()

final,number_final,clusterids=tonewick(-21,data2,names)
za=zip(final,number_final)
#print number_final
numbers_final=list(set(number_final) & set(clusterids))
#print numbers_final
final_list=[]
#print final

for tu in final:
    for i in range(0,len(numbers_final)):
        if tu[0]+1==numbers_final[i]:
            #print tu[0]+1
            final_list.append(numbers_final[i])
        
#print final_list
#print zip(final[0],final_list[0])
j=0
for i in number_final:
    
    if i==numbers_final[j]:
        j=j+1
        #print i,numbers_final[j]
        
    else:
        numbers_final.insert(j, 100)
        j=j+1
        #print i,numbers_final[j]
i_final=zip(final,tuple(numbers_final))   
for na in i_final:
    if na[0][0][0]!=100:
        na1[0][0][0]=(names[na[0][0][0]])
 
 