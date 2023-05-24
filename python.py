num=int(input("enter the number:"))
flag=0
for i in range(2,num):
	if num%i==0:
	flag=flag+1
if flag>1:
	print("composite number")
else:
	print("prime number")

