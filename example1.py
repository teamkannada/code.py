n=int(input("enter any number"))
fib1=0
fib2=1
fib3=1
if n==1 or n==0:
    print("yes fib")
else:
    while(fib3<n): 
        fib3=fib1+fib2
        fib1=fib2
        fib2=fib3
        if (fib3==n):
            print("yes fib")
            break
    else:
        print("NO")
