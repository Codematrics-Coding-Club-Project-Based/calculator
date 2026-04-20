#Calculator:
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