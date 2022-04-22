#method overloading
class student:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def avg(self,a=None,b=None,c=None):
        average=0
        if(a!=None and b!=None and c!=None):
            average = (a+b+c)/3
        elif(a!=None and b!=None and c==None):
            average = (a+b)/2
        elif(a!=None and b==None and c==None):
            average = a
        else:
             average="No values provided"

        return average

s1=student()
avg1=s1.avg(12,13,14)
avg2=s1.avg(12,13)
avg3=s1.avg(12)
avg4=s1.avg()

print(avg1)
print(avg2)
print(avg3)
print(avg4)
