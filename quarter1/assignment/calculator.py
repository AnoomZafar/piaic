num1=0
num2=0
op=" "
op=input("enter an operator +,-,*,/: ")
num1=int(input("enter 1st number: "))
num2=int(input("enter 2nd number: "))
if op =="+":
    sum=num1+num2
    print("sum of 2 numbers: ",sum)
elif op =="-":
    sub=num1-num2
    print("subtraction of 2 numbers: ",sub)
elif op =="*":
    mult=num1*num2
    print("multiplication of 2 numbers: ",mult)
elif op =="/":
    div=num1/num2
    print("division of 2 numbers: ",div)
elif op !="+" and op !="-" and op !="*" and op !="/":
    print("please enter the correct operator")