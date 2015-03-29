#Program to retrieve Informative sites
from Bio import AlignIO
import numpy
holder=open("seq1.fasta","r")

list1=[]
matrix=[]
list2=[]
transposed = []
sequences=holder.readlines()
for seq in range(1,len(sequences),3):
     list1.append(sequences[seq].strip())

for i in range (0,len(list1[0])):   
    if len(set(([x[i] for x in list1])))==2:
        
        list2.append(([x[i] for x in list1]))
        

for i in list2:
    if i.count('G')>(len(list1)/2):
        list2.remove(i)
    if i.count('A')>(len(list1)/2):
        list2.remove(i)
    if i.count('C')>(len(list1)/2):
        list2.remove(i)
    if i.count('T')>(len(list1)/2):
        list2.remove(i)

for i in range(0,len(list2)):
    transposed.append([row[i] for row in list2])

zipped=list(zip(*list2))
j=0
for i in zipped:
    j=j+1
    print j,''.join(str(x) for x in list(i))
    
