def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b

a=float(input("Enter a number :"))
b=float(input("Enter another number :"))
method =input("Select Method :\n1.Add\n2.Subtract\n3.Divide\n4.Multiply ")
if method== "1":
    print(a+b)
elif method== "2":
    print(a-b)
elif method== "3":
    print(a/b)
elif method== "4":
    print(a*b)
else:
    print("Error try again")

    
        
        
