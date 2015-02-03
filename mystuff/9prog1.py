#Writing the product and price in a file
fileHolder = open("products.txt", "w")
productName=" "
while productName!="":
	productName=raw_input("Enter product name: ")
	if productName!="":
		productPrize=input("Enter price in Euros:")
		fileHolder.write(productName+", "+str(productPrize)+"\n")
print "bye!"
fileHolder.close()
