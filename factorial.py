#create a program to find the factorial of a user defined integer
n=int(input("enter the number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
    print("The factorial of",n,"is",fact)
    
