def reverseofnum(num):
    reversed=0
    while(num>0):
        reversed=reversed*10+num%10
        num=num//10
    return reversed

print(reverseofnum(56789))