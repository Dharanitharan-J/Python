a=int(input("Enter first side"))
b=int(input("Enter second side"))
c=int(input("Enter third side"))
if(a+b)>c and (b+c)>a and (c+a)>b:
      print("Triangle is possible")
else:
      print("Triangle is not possible")
