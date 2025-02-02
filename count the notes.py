#take total amount as input from user
amount = int(input("please enter amount for withdraw"))
#calculate the number of notes of different denominations
note_1 = amount // 100 # 760//100=7
note_2 = (amount%100) //50
note_3 = ((amount%100)%50)//10
print("notes of 100",note_1)
print("notes of 50",note_2)
print("notes of 10",note_3) 
