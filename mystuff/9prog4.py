#comments
def parseComments(programFile):
	list=[]
	mf = open("average.py", "r")
	allLines = mf.readlines()
	for index, value in enumerate(allLines):
		allLines[index] = value.replace("\n","")
	for line in allLines:
		if line.startswith("#"):
			list.append(line)
	for index, value in enumerate(list):
		list[index] = value.replace("# ","")
		
	return list
	
	

lst = parseComments("average.py")
print lst