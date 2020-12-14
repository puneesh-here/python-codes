a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=input("Enter your choice of operator:")
if c=='+':
    print("the sum is",a+b)
elif c=='-':
    print("the difference is",a-b)
elif c=='*':
    print("the product is",a*b)
elif c=='/':
    print("the quotient is",a/b)
else:
    print("Wrong choice of operator...Try again")