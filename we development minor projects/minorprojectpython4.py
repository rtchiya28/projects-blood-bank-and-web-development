class error(Exception):
    """base class for other exceptions"""
    pass
class NotNumberException(error):
    """raise when age is not a number"""
    pass
name=0
age=0
name=input("enter the name:")
try:
    age=input("enter the age:")
    if (isinstance(age,int)):
        print("no exception")
    else:
        raise NotNumberException('age is not number')
except NotNumberException:
    print("exception resolved")
print("completed")
