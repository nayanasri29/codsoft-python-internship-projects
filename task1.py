print("SIMPLE CALCULATOR")

n1=float(input("Enter first number:"))
n2=float(input("Enter second number:"))

print("Choose an operation: + - * /")
op=input("Enter operation:")
if op=='+':
    print("Sum= ", n1+n2)
elif op=='-':
    print("Difference= ", n1-n2)
elif op=='*':
    print("Product= ", n1*n2)
elif op=='/':
    if n2!=0:
        print("Quotient= ", n1/n2)
    else:
        print("Error:Division with zero isn't possible")
        
else:
    print("Invalid operator!!")
