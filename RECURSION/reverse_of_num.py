import math

def reverse_of_num(num):
    if(num%10==num):
        return num
    return num%10*(math.pow(10,math.floor(math.log10(num))))+reverse_of_num(num//10)

# using global variable00
sum_of_digits=0
def reverse_of_num2(num):
    global sum_of_digits
    if(num==0):
        return 
    sum_of_digits=(sum_of_digits*10)+(num%10)
    reverse_of_num2(num//10)
    return sum_of_digits

# USING STRING
def reverse_of_num3(num):
    if(num%10==num):
        return str(num)
    return str(num%10)+str(reverse_of_num3(num//10))

# using helper function 
def reverse_of_num4(num):
    return reverse_helper(num,math.ceil(math.log10(num)))

def reverse_helper(num,digits):
    if(num%10==num):
        return num
    return num%10*math.pow(10,digits-1)+reverse_helper(num//10,digits-1)

print(reverse_of_num4(1929))