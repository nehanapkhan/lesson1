print("select your ride:")
print("1.bike")
print("2.car")

choice = int(input("enter your choice"))

if(choice==1):
    print("what type of bike?")
    print("1.scooty\n")
    print("2.scooter\n")


    choice2 = int(input("enter your second choice"))
    if choice2 == 1:
        print("you have selected scooty")
    else:
        print("you have selected scooter")
elif(choice ==2):
    print("ehat type of care:")
    print("1.sedan")
    print("2.suv")

    choice3 = int(input("enter your choice"))
    if(choice3 ==1):
       print("you have seleted sedan")
    else:
        print("you have selected suv")
else:
    print("worng choice")        
