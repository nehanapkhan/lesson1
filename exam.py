medical_cause = input("did you have a medical cause Y or N:")
attendance = int(input("enter your attendance: "))
if medical_cause == 'Y':
    print("your are allowed")
else:
     if attendance >=75:
         print("allowed")          
     else:
         print("not allowed")   