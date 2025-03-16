try:
    num1,num2 = eval(input("enter two number,sepearted by a comma:"))
   
    result = num1/num2
    print("result is",result)

except ZeroDivisionError:
    print("division by zero is error")

except SyntaxError:
    print("comma is missing .enter numbers seperated by comma like this 1.2")

except:
    print("wrong input")

else:
    print("no exception")

finally:
    print("this will exceute no matter what")    


   