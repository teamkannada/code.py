num=[]
n=int(input("enter the how many number ypu want to enter"))
print("enter the number of .list")
for i in range(n):
    num.append(int(input()))
print("the numbers are",num)
key=int(input("enter the number to find=== "))
found=False
for i in num:
    if i==key:
        found=True
        break
if found==True:
    print("the number",key,"is found")
else:
    print("the number",key,"is not found")
