a=int(input("Enter your level:"))
b=int(input("Enter your level that you have to Go:"))
i=a
if a==b:
    print("the numbers are equal") 
while i<=b:
    c=(i**2)
    print(c,'')
    i+=1   
else:
    print("")
    print("You are in your next level")    