"""
def Display():
    print("Welcome to the python")
Display()

def Display(Name,Age):
    print("Name=",Name,"Age=",Age)
Display(Age=23,Name="Jhon")
Display(Name="Don",Age=22)
"""
"""
car={"name":"ford","brand":"mustang","year":"1964"}
car.clear()
print(car)
"""
"""
from python import divide
a=int(input("Enter your firt number"))
b=int(input("Enter your econd number"))
print("Sum=",divide(a,b))
"""
"""
try:
    a= int(input("enter your first value"))
    b=int(input("enter your 2nd value"))
    if b is 0:
        raise ArithmeticError
    else:
        print("a/b = ",a/b)
except ArithmeticError:
 print("The value of b can't be 0")
 """
"""
import datetime
print(datetime.datetime.now())
import calendar;
cal=calendar.month(2020,3)
print(cal)
import calendar
s=calendar.prcal(2020)
"""
"""
class person:
    def __init__(self,name,age):
     self.name=name
     self.age=age
    def myfunc(self):
     print("Hello this is My Name "+ self.name)
     print("This is my age ", self.age)
p1=person("jhon",36)
p1.myfunc() 
"""