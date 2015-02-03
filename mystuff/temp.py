x=[1,5,4,2]
j=0
for i in range( 0,len(x) ):
	minPos = i
	print "i",i
	for j in range(i+1, len(x) ):
		print j,i
		if x[j] < x[minPos]:
			minPos = j
			temp = x[minPos]
			x[minPos] = x[i]
			x[i] = temp
			#print x[i],"swapped with",x[minPos]

print x
print len(x)

