#write a program to find out the maximum no between three numbers
x=int(input("enter first number:"))
y=int(input("enter second number:"))
z=int(input("enter third number:"))
if(x>y and x>z):
    print(x,"is greater than",y,"and",z)
elif(y>x and y>z):
    print(y,"is greater than",x,"and",z)
else:
    print(z,"is greater than",x,"and",y)
