def add(x,y):
    return (x+y)
def sub(x,y):
    return (x-y)
def mul(x,y):
    return (x*y)
def div(x,y):
    return (x/y)
c=0
while c!=6:
    print("\n1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.exit")
    c=int(input("enter your choice"))
    if c==1:
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        r=add(a,b)
        print(r)
    if c==2:
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        r=sub(a,b)
        print(r)
    if c==3:
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        r=mul(a,b)
        print(r)
    if c==4:
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        r=div(a,b)
        print(r)
    if c==5:
        exit()
    
        

