#define a funcation to calculate cube

def cub(number):
    return number*number*number

#define a fucation which execute cub funcation if the user enterednuber is didisible by 3

def by_three(number):
    if number%3==0:
        return cub(number)
    else:
        return False
    

print(by_three(9))
print(by_three(4))