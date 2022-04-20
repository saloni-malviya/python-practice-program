#Reverse the string
a=str(input("enter the name:"))
s=len(a)
reverse=""
for i in range(s-1,-1,-1):
    reverse+=a[i]
print(reverse)
