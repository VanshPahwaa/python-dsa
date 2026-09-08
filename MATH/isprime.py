# brute force tc o(num)
def isprime(num):
    for i in range(2,num):
        if(num%i==0):
            return False
        
    return True
# better tc o(sqrt(num))
def isprime_optimized(num):
    if num<=1:
        return False
    c=2
    while(c*c<=num):
        if num%c==0:
            return False
        c+=1
    return True

# 




print(isprime_optimized(5))