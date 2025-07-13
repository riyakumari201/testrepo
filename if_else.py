# Checking Eligiblity of a person
"""
elligible=18
n=int(input("Enter your age "))
if n==elligible:
   print("You can vote")
else:
   print("You cannot vote")
   """
#Finding Greatest number
"""
def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
       return num1
    elif num2>=num1 and num2>=num3:
       return num2
    elif num3>=num1 and num3>=num2:
       return num3
    elif num1==num2 and num1==num3 and num2==num3:
       return 0
n1=int(input("Enter the first number : "))
n2=int(input("Enter the second number : "))
n3=int(input("Enter the third number : "))
Greatest=max_num(n1,n2,n3)
print("The greatest number is", + Greatest)
"""
#Creating a calculator
"""
n1=float(input("Enter the First number : "))
n2=float(input("Enter the second number : "))
oper=input("Enter Operator : ")
if oper=="+":
    print(n1+n2)
elif oper=="-":
    print(n1-n2)
elif oper=="*":
    print(n1*n2) 
elif oper=="/":
    print(n1/n2)
elif oper=="%":
    print(n1%n2)  
else :
    print("INVALID OPERATOR")             
"""
#if..else in a line
a=int(input("Enter the numnber : "))
b=int(input("Enter the second number : "))
print("A") if a>b else print("=") if a==b else print("B")