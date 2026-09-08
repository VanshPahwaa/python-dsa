def ispali(num):
    reversed=0
    dup=num
    while(num>0):
        reversed=reversed*10+num%10
        num=num//10
    return reversed==dup

print(ispali(1211))