""""
for i in range(1,6):
    print(i)
print("End of the program")

print("Number 1 to 10 revers order")
for i in range(10,0,-1):
 print(i,end="")
print("End of the program")

print("The capital letter A to Z")
for i in range(65,91,1):
   print(chr(i),end="")

print("Star petten Diplay")
num=1
x=num
for i in range(1,6,1):
   num=num+1
   for j in range(1,num,1):
    print("*",end="")
   print()
print("End of the Program")

str=""
for row in range(0,7):
   for  col in range(0,7):
        if (((row==0 or row==3 or row==6)and col >1 and col < 5)or(col==1 and(row==1 or row==2 or row==6))or(col==5 and(row==0 or row==4 or row==5))):
           str=str+"*"
        else:
            str=str+" "
   str=str+"\n"
print(str)

def Diplay(Name,age):
   print("Name=",Name,"Age=",age)
Diplay(age=25,Name="john")


sum=0
count=0
while count<=20:
    if count %5 == 0:
     sum=sum+count
    count=count+1
print("The sum of number ", sum,(chr (sum)))



str=""
for row in range(0,7):
   for  col in range(0,7):
        if (((row==0 or row==3 or row==6)and col >1 and col < 5)or(col==1 and(row==1 or row==2 or row==6))or(col==5 and(row==0 or row==4 or row==5))):
           str=str+"*"
        else:
            str=str+" "
   str=str+"\n"
print(str)
"""
def summation(a,b):  
    return a+b  
def multiplication(a,b):  
    return a*b;  
def divide(a,b):  
    return a/b;  
