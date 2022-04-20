#create a program to print the fibonacci series
n=int(input("enter the length of fibonacci series:"))
p1=0
p2=1
i=0
print("fibonacci sequence")
while i<n:
    print(p1)
    sum=p1+p2
    p1=p2
    p2=sum
    i+=1
    
