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
                index1.append(substring)
                seq_sub.append((len(substring),substring,seq1.find(substring)))
                
    
    seq_sub1= sorted(seq_sub)
    print seq_sub1
    for i in range(len(seq_sub1) - 1, -1, -1):
        (len1,str1,idx1)=seq_sub1[i]
        for j in range(0,i):
            (len2,str2,idx2)=seq_sub1[j]
            #print strstr1
            if (idx2>=idx1) and (idx2<=(idx1+len1)) and ((idx2+len2)<=(idx1+len1)):
                index2.append(str2)
    print list(set(index1).difference(index2))
    # for i in range(0,len(seq_sub)-1):
        # if seq_sub[i].find(seq_sub[i+1])!=True:
            # print i,i+1
            # if seq_sub[i+1].find(seq_sub[i])!=True:
                # index2.append(seq_sub[i])
    # for seq in seq_sub:
        # if seq
            # #seq_sub.remove(seq_sub[i])
    # print index2        
         
           
substrings=[]
my_seq = Seq("TATCGCGATAAACCTAGGTTTCCTCTCTCTACCTAGGTCCCCACCTAGGTCCCACCTAGGTTCCCCGGGGA", IUPAC.unambiguous_dna)
print my_seq.reverse_complement()
rp(my_seq,8,10)
    
    
    
    
    




