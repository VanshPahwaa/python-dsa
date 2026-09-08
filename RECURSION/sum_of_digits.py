def sum_of_digits(num):
    # if(num%10==num):
    #     return num
#  or below or above 
    if(num<10):
        return num
    return num%10+sum_of_digits(num//10)

print(sum_of_digits(2100))