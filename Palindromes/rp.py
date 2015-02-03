#palindromes
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

def rp(seq,min_len,max_len):
    length = len(seq)
    list1,seq_sub,palindrome,index1,index2 = [], [], [], [], []
    #generate all the substrings from the sequence
    seq1=str(seq)
    for i in xrange(length):
        for j in xrange(i,length):
            list1.append(str(seq[i:j + 1]))
    alist=list(set(list1))
    #retrieving the substrings length >= min_len and length <= max_len 
    for substring in alist:
        if len(substring)>=min_len and len(substring)<=max_len:
            reverse=Seq(substring).reverse_complement()
            #comparing if the substrings are palindromes
            if substring==str(reverse):                             
                index1.append(substring)
                seq_sub.append((len(substring),substring,seq1.find(substring)))
           
    seq_sub1= sorted(seq_sub)
    #Checking for the largest palindromes (eliminating small ones inside the large palindromes)
    for i in range(len(seq_sub1) - 1, -1, -1):
        (len1,str1,idx1)=seq_sub1[i]
        for j in range(0,i):
            (len2,str2,idx2)=seq_sub1[j]
    # Three criterias which the palindromes should pass to be the largest ones
            if (idx2>=idx1) and (idx2<=(idx1+len1)) and ((idx2+len2)<=(idx1+len1)):
                index2.append(str2)
    palindrome= list(set(index1).difference(index2))
    palindrome1,palindrome2=[],[]
    #Finding all the indexes (one palindrome can occur in many regions in the sequence)
    for seq in palindrome:
        for i in range(len(seq1)):
            if seq1.startswith(seq, i):
                palindrome1.append((i,len(seq)))
    #this returns  [(index0,len0),(index1,len1),...].
    return palindrome1   
         
#to print stars below palindromes 
def pretty_print(seq,hits):
    star=[' ']*len(seq)
    print seq
    for first_list in hits:
        first_item=first_list[0]
        second_item=(first_list[1]+first_list[0])
        star[first_item:second_item]='*'*first_list[1]
    print ''.join(star)
    
    
    
substrings=[]
my_seq = Seq("TCCTCTCTCTACCTAGGTCCCCACCTAGGTCCC", IUPAC.unambiguous_dna)
hits= rp(my_seq,8,10)
pretty_print(my_seq,hits)    
    
    
#string1   TCCTCTCTCTACCTAGGTCCCCACCTAGGTCCC    
#string2 for testing:  TATCGCGATAAACCTAGGTTTCCTCTCTCTACCTAGGTCCCCACCTAGGTCCCACCTAGGTTCCCCGGGGA    




