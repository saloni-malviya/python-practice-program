#write a program to check whether number prime or not
n=int(input("enter any number"))
i=2
while(i<=n-1):
    if(n%i==0):
       print("given no is not prime")
       break
    else:
        print("given no is prime")
        break
else:
    print("not a prime")
