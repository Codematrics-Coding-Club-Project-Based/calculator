#Calculator:
"""
#MATRIX OPERATION:
print("\n --MENU to choose the operation to be performend--")
print("1) ADDITION")
print("2) SUBTRACTION")
print("3) DIVISION")
print("4) MULTIPLICATION")
choice=input("choose any operation to be performed:(1/2/3/4):")
a=int(input("enter first num:"))
b=int(input("enter second num:"))
if choice=="1":
    print("ADDITION is :",a+b)
    
elif choice=="2":
    print("SUBTRACTION is :",a-b)
    
elif choice=="3":
    print("DIVISION is:",a/b)
      
elif choice=="4":
    print("MULTIPLICATION is :",a*b)
    
else:
    print("INVALID OPTION")   

# factorial calculator:
num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Factorial is not defined for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("Factorial of", num, "is", factorial)   
#POWER CALCULATOR:
num = int(input("Enter a number: "))
num1 = int(input("Enter a power: "))
result=num**num1
print("result is :",result)
#temperature converter (Celsius to Fahrenheit and vice versa):
f=int(input("enter the temperature to convert fahrenheit into celsius:"))	
result= (f-32)*5/9
c=int(input("enter the temperature to convert celsius into fahrenheit :"))
result1=(c*9/5)+32
print("convert fahrenheit into celsius:",result)
print("convert celsius into fahrenheit:",result1)
#Number system converter (binary to decimal, octal to hexadecimal etc and vice versa):
num=int(input("Enter a decimal number: "))
print("decimal to bin:",bin(num))
print("decimal to oct:",oct(num))
print("decimal to hex:",hex(num))
#QUADRATIC EQUATION SOLVER:
import cmath

def solve_quadratic(a, b, c):
    d = cmath.sqrt(b**2 - 4*a*c)
    x1 = (-b + d) / (2*a)
    x2 = (-b - d) / (2*a)
    return x1, x2
#LINEAR EQUATION SOLVER:    
def solve_linear(a, b):
    return -b / a
#PERCENTAGE SOLVER:    
def percentage(part, whole):
    return (part / whole) * 100    
    

"""






    
    
    
    