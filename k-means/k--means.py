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
cluster1=rand_data(1,1,1,1,10)
cluster2=rand_data(5,1,5,1,10)
cluster=cluster1+cluster2
print cluster
print kcluster(cluster,nclusters=2,method='a',dist='e',npass=10)
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
#print f1
f.close()
for f in f1:
    f2=float(f)
print kcluster(f2,nclusters=2,method='a',dist='e')

#print f1
