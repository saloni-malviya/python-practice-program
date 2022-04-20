#swap to numbers
print("this script is intevoled to swap the values of two data variable using a third temporary variable")
a=input("enter first integer:")
b=input("enter second integer:")
print("value before swapping")
print("a="+a)
print("b="+b)
a=int(a)
b=int(b)
t=a
a=b
b=t
print("values after swapping")
print("a="+str(a))
print("b="+str(b))
