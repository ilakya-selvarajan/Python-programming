#palindromes
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

def rp(seq,min_len,max_len):
    length = len(seq)
    list1,seq_sub,palindrome,index1,index2 = [], [], [], [], []
    
    seq1=str(seq)
    for i in xrange(length):
        for j in xrange(i,length):
            list1.append(str(seq[i:j + 1]))
    alist=list(set(list1))
    
    for substring in alist:
        if len(substring)>=min_len and len(substring)<=max_len:
            reverse=Seq(substring).reverse_complement()
            if substring==str(reverse):
                index1.append(substring)
                seq_sub.append((len(substring),substring,seq1.find(substring)))
           
    
    seq_sub1= sorted(seq_sub)
    #print seq_sub1
    for i in range(len(seq_sub1) - 1, -1, -1):
        (len1,str1,idx1)=seq_sub1[i]
        for j in range(0,i):
            (len2,str2,idx2)=seq_sub1[j]
            #print strstr1
            if (idx2>=idx1) and (idx2<=(idx1+len1)) and ((idx2+len2)<=(idx1+len1)):
                index2.append(str2)
    palindrome= list(set(index1).difference(index2))
    palindrome1=[]
    for seq in palindrome:
        palindrome1.append((seq1.find(seq),len(seq)))
    return palindrome1   
         
 
def pretty_print(seq,hits):
    star=['']*len(seq)
    print seq
    #for i in range(hits:
    #star.insert(8:18,'*')
    print ' '.join(star)
    print hits
 
substrings=[]
my_seq = Seq("TCCTCTCTCTACCTAGGTCCCCACCTAGGTCCC", IUPAC.unambiguous_dna)
hits= rp(my_seq,8,10)
pretty_print(my_seq,hits)    
    
    
    
#string2 for testing:  TATCGCGATAAACCTAGGTTTCCTCTCTCTACCTAGGTCCCCACCTAGGTCCCACCTAGGTTCCCCGGGGA    




