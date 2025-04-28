n=int(input("enter a number:"))
sum=0
if n==0:
    print("0 is not a natural number")
else:
    while n>0:
        sum=sum+n
        n=n-1
    print("sum of n Natural number is",sum)

    
