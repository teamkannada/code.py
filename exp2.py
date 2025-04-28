import cmath
import math
a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
d=(b*b)-(4*a*c)
print ("root=",d)
if (d>0):
    print("roots are real & distict")
    p1=-b/(2*a)
    p2=math.sqrt(d)/(2*a)
    x1=p1+p2
    x2=p1-p2
    print("root 1 =",x1)
    print("root 2 =",x2)
elif(d==0):
    print("roots are real and equal")
    x=-b/2*a
    print("root 1 =",x)
    print("root 2 =",x)
else:
    print("roots are real & complex")
    p1=-b/(2*a)
    p2=cmath.sqrt(d)/(2*a)
    x1=complex(p1+p2)
    x2=complex(p1-p2)
    print("root 1 =",x1)
    print("root 2 =",x2)
