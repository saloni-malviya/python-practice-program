#if else statement user defined
#write a program to check whether the no even or odd
a=int(input("enter the number"))

c=a%2
print(c)

if(a==0):
      print("no is neither even or odd")
elif(a%2==0):
    print("no is even")
else:
    print("no is odd")
