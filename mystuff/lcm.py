

  
def LCM(firstNumber,SecondNumber):
 k=0
 for i in range(1,SecondNumber+1):
  for j in range(1,firstNumber+1):
   if i*firstNumber==j*SecondNumber:
    k=k+1
    if k==1:
     print i*firstNumber