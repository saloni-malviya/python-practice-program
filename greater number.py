# program to find greater number between the three numbers
a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
if(a==b and b==c and c==a):
    print("both are the same")
elif(a==b and a>c):
    print(a,"and",b,"are the same and",a,"is greater than",c)
elif(a==c and a>b):
    print(a,"and",c,"are the same and",a,"is greater than",b)
elif(b==a and b>c):
    print(a,"and",b,"are the same and",b,"is greater than",c)
elif(b==c and b>a):
    print(b,"and",c,"are the same and",b,"is greater than",a)
elif(c==a and c>b):
    print(c,"and",a,"are the same and",c,"is greater than",b)
elif(c==b and c>a):
    print(c,"and",b,"are the same and",c,"is greater than",a)
elif(a>b and a>c):
    print(a,"is greater than",b,"and",c)
elif(b>c and b>a):
    print(b,"is greater than",c,"and",a)
else:
    print(c,"is greater than",a,"and",b)
