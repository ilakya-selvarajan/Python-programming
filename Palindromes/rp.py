#palindromes
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

def rp(seq,min_len,max_len):
    length = len(seq)
    list1 = []
    seq_sub= []
    index1=[]
    index2=[]
    seq1=str(seq)
    for i in xrange(length):
        for j in xrange(i,length):
            list1.append(str(seq[i:j + 1]))
    alist=list(set(list1))
    
    for substring in alist:
        if len(substring)>=min_len and len(substring)<=max_len:
            #seq_sub.append(substring)
            reverse=Seq(substring).reverse_complement()
            #rev_comp.append(str(reverse))
            if substring==str(reverse):
                seq_sub.append(substring)
    print seq_sub
    
    for i in range(len(seq_sub)  -1, -1, -1):
        if seq_sub[i].find(seq_sub[i-1])==True:
              print seq_sub[i+1]
              #seq_sub.remove(seq_sub[i-1])
        if seq_sub[i-1].find(seq_sub[i])==True:
            print seq_sub[i]
            #seq_sub.remove(seq_sub[i])
    print seq_sub        
         
           
substrings=[]
my_seq = Seq("TATCGCGATAAACCTAGGTTTCCTCTCTCTACCTAGGTCCCCACCTAGGTCCCACCTAGGTTCCCCGGGGA", IUPAC.unambiguous_dna)
print my_seq.reverse_complement()
rp(my_seq,8,10)
    
    
    
    
    




