num1= int(input("enter the first number:"))
num2=int(input("enter the second number:"))
operation =input("enter operation (+,-,*,/): ")
if operation=='+':
    print("reslut: ",num1+num2)
elif operation=='-':
    print("reslut: ",num1-num2)
elif operation=='*':
    print("reslut: ",num1*num2)
elif operation=='/':
    if num2 !=0:
        print("result: ",num1/num2)
    else:
        print("Error:division by '0' not allowed")
else:
    print("envalid operation")