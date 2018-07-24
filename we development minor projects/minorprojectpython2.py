name=0
age=0
def create():
    with open('emp.txt','w') as f:
        name=input("\n enter name:")
        f.write(name+'\n')
        age=input("enter age: ")
        f.write(age+'\n')
def display():
    with open('emp.txt','r') as f:
        print("\n name:",f.readline())
        print("age: ",f.readline())
create()
display()
