#Program to retrieve Informative sites
holder=open("sequences.txt","r")

# list1=[]
# sequences=holder.readlines()
# for seq in range(1,len(sequences),3):
    # list1.append(sequences[seq].strip())
# for i in range (0,len(list1[0])):    
    # if len(set(([x[i] for x in list1])))==2:
        # print ([x[i] for x in list1])

# from Bio import AlignIO
# alignment = AlignIO.read("sequences.txt", "fasta")
# print alignment[0]

from Bio.Align.Applications import MuscleCommandline
 
cmdline = MuscleCommandline(input="sequences.txt", out="efgr-family.aln", clw=True)
cmdline()