# fibonacci sequence
import math
def ps(k):
    num=int(math.sqrt(k))
    return k==num*num

n=int(input("Enter any number"))
res1=5*n*n+4
res2=5*n*n-4
if ps(res1)==True or ps(res2)==True:
    print("the given number is in fibonacci sequence")
else:
    print("the given number is in not fibonacci sequence")

