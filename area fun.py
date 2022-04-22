#program to area of circle and area of rectangle in function overloading
class A:
    def area(self,r=None,l=None):
        if(r!=None and l==None):
            ar=22/7*r*r
            return ar
        elif(r!=None and l!=None):
            ar=r*l
            return ar
        else:
            print("No provide values")

a1=A()
area1=a1.area(2,5)
print("area of rectangle",area1)
area2=a1.area(3)
print("area of circle",area2)
            
