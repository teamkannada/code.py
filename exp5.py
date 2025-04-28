#check a given number is prime or not
def is_p(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i == 0:
           return False
    return True

key=int(input("enter number to check wheter it's prime number or not"))
if is_p(key):
    print(f"{key}is a prime number")
else :
    print(f"{key}is a not prime number")