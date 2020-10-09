#To check whether a number is a Perfect square of 4
def is_power(num):
    if(num == 0):
        return print(False)
    while(num!= 1):
        if(num%4 !=0):
            return print(False)
        num = num//4
    return print(True)
is_power(4)