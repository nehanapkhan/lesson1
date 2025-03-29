L =[4,5,1,2,9,7,10,8]
print("original list"
,L)

#create a veriable to store sum of the list
count = 0

#find the sum
for i in L:
    count = count+1
avg = count/len(L)
print("sum =",count)
print("average =",avg)
L.sort()

print( "smallest element is:",L[0])  
print("lagest element is:",L[-1])