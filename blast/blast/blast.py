import sys
from Bio.Blast import NCBIWWW,NCBIXML
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

# ### THE TASK:

# We are back to the example in the KNN topic. This time, the idea is to run the sequences
# from bac_vs_hum_test.vw through BLAST and establish the source organism like that.
# So we want to go through the file, one sequence at a time, blast it, and dig the organism out.

# The simpler (but MUCH slower) way will be to run blast online. The other way will be run blast locally,
# as I showed in the lecture.

# Please finish this program until you are able to verify that the organism hits are indeed correct, ie
# that whenever a line in the .vw file has "-1" as the class, you successfully identify the sequence
# as EColi and whenever it says "1", you identify it as a human.

# Have fun!

#local_blast() and online_blast() do same thing, but through different means

def local_blast(i,s):
    record = SeqRecord(Seq(s,IUPAC.IUPACUnambiguousDNA()),id=str(i))
    SeqIO.write([record],"tmp.fasta","fasta") #We need to write the sequence into a fasta file so we can run blast on it locally
    #mydb is my local blast database produced using makeblastdb as shown on the lecture
    #outfmt=5 asks for the XML output
    #the rest is I guess kinda self-explanatory
    cline=NcbiblastnCommandline(cmd="blastn",out="%d.xml"%i,db="mydb",outfmt=5,query="tmp.fasta") #assemble the command line
    cline() #..and run it

def online_blast(i,s):
    """
    Runs BLAST online on sequence s and saves the result into a file called i.xml
    i is the number of the sequence and s is a string with the sequence
    """
    record = SeqRecord(Seq(s,IUPAC.IUPACUnambiguousDNA()),id=str(i))
    result_handle = NCBIWWW.qblast("blastn", "nr", record.format("fasta")) #Run blast online, this will take a while, check out the use of "format"
    with open("%d.xml"%i,"wt") as f: #..and save the output into an XML file
        f.write(result_handle.read())
        f.flush()
    print i,".xml file written",


def dig_organism(i,c):
    """
    given an id, open the appropriate XML file and dig the organism out
    """

    with open("%d.xml"%i) as f:
        brec = NCBIXML.read(f) #Read a single blast record
        a=brec.alignments[0] #The first hit will suffice - it's the best hit
        str1="Escherichia coli"
        str2="Homo sapiens"
        if a.hit_def.find(str1)==0:
            print c,str1
            lines=c,str1
            #result.write(c)
            result.write(str(lines))
            result.write("\n")
        if a.hit_def.find(str2)==0:
            print c,str2
            lines=c,str2
            result.write(str(lines))
            result.write("\n")
        if a.hit_def.find(str2)!=0 and a.hit_def.find(str1)!=0:
            if a.hit_def[0]=='H':
                print c,str2
                lines=c,str2
                result.write(str(lines))
                result.write("\n")
            if a.hit_def[0]=='E':
                print c,str1
                lines=c,str1
                result.write(str(lines))
                result.write("\n")
         #the organism is in here somewhere

def blast(N):
    #Run online blast on first N rows in the bac_vs_hum_test.vw
    with open("bac_vs_hum_test.vw") as f:
        for i,line in enumerate(f):
            if i==N:
                break #we're done
            line=line.strip()
            c,s=line.split(" | ")
            #online_blast(i,s)
            dig_organism(i,c)
        
    
N=4
result=open("result.txt","w")
blast(N) #run this only once, you'll get the XMLs and then you can simply use them
#dig_organism(0,-1)
#dig_organism(1,1)
#holder=[]
result.close()

index=input("Blast was run for three sequences. Try 0-3")
f1=open("result.txt","r")
holder=f1.readlines()
while index<0 or index>4:
    index=input("please try to access xml file between 0 to 3")
while index>=0 and index<=3:
    print holder[index]
    index=input("Press e to exit or 0-3")
    if index<0 or index>4:
        index=input("please try to access xml file between 0 to 3")
    else:
        exit


f1.close()