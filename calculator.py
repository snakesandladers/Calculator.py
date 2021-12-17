def add(x,y):
     return x + y 
def substract(x,y):
     return x - y
def multiplication(x,y):
     return x * y
def division(x,y):     
    return  x / y 
print ("select operation.")
print("1.add")
print("1.substract")

print("1.multiply")

print("1.division")
choice=input("enter choice 1/2/3/4/5:")
num1=int(input("enter first number :"))
num2=int(input("enter second number:"))
if choice=='1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=='2':
     print(num1,"-", num2,"=",substract(num1,num2))

elif choice=='3':
    print(num1,"*",num2,"=",multiplication(num1,num2))
elif choice=='4':
    print(num1,"/",num2,"=",division(num1,num2))
else:
    print("invalid input")
  
  output:
   enter first number :1
enter second number:5
1 + 5 = 6
