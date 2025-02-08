actual_cost = float(input("please enter the actual product price:"))
sale_amount = float(input("please enter sales amount:"))

if(sale_amount>actual_cost):
    amount = sale_amount-actual_cost
    print("the profit is",amount)
else:

    print("no profit")