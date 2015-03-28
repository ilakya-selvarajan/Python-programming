import random
from Bio.Cluster import *
import gzip

def rand_data(mx,my,stdx,stdy,N):
    my_list=[]
    
    for i in range(0,N):
        list1=[]
        x=random.gauss(mx,stdx)
        y=random.gauss(my,stdy)
        #print x,y
        list1.append(x)
        list1.append(y)
        #value=zip(listx,listy)
        my_list.append(list1)
    return my_list
    
f1=[]
names=[]
cluster1=rand_data(1,1,1,1,10)
cluster2=rand_data(5,1,5,1,10)
cluster=cluster1+cluster2
#print cluster
#print kcluster(cluster,nclusters=2,method='a',dist='e',npass=10)
f = gzip.open('words.txt.gz', 'rb')
file_content = f.readlines()
for files in file_content:
    f2=[]
    file1= files.strip("\n")
    
    w,v=file1.split("\t")
    names.append(w)
    numbers=v.split(" ")
    f2.append(numbers)
    f1.append(f2)
#print f1
f.close()
f3=[]
for fst in f1:
    for snd in fst:
        f3.append(map(float, snd))
        
            
            #print trd
dict22={}  
dict23={}    
kcluster = kcluster(f3,nclusters=7,method='a',dist='e')
print kcluster[0]
list11=kcluster[0]
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
