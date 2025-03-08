def add(p,q):
    return p+q

def subtract(p,q):
    return p-q

def multiply(p,q):
    return p*q

def division(p,q):
    return p/q

print("please select the operation")
print("a.add")
print("b.subract")
print("c.multiply")
print("d.division") 

choice = input("please enter you choice a/b/c/d")

num1 = int(input("enter the first number"))
num2 = int(input("enter the secound number"))

if choice == 'a':
    print(num1 ,"+",num2, '=', add(num1,num2))

        
elif choice =='b':
        

          print(num1 ,"-", num2,"=", subtract(num1,num2))
elif choice =='c':

     print(num1 ,"*", num2,"=", multiply(num1,num2))

elif choice =='d':

  print(num1 ,"/", num2,"=", division(num1,num2))

else:

  print("this is an invalid input")