try:
    num=float(input("enter numerator"))
    denum=float(input("enter denominator"))
    result=num/denum
except ZeroDivisionError:
    print("error:denominator cannot be zero!")
except ValueError:
    print("Error:please enter vaild number!")
else:
    print(f"result: {result}")