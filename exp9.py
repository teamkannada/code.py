n=int(input("enter the size of list"))
print("enter ",n, "elements")
list=[]
for i in range(n):
    list.append(int(input()))
print("before sorting",list)
for j in range(n):
    min=list[j]
    for k in range(j+1,n):
        if min>list[k]:
            min=list[k]
            temp=list[j]
            list[j]=list[k]
            list[k]=temp
            print(list)
print("after sorting")    
print(list)
    