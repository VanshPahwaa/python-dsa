def printalldivisor(num):
    divisors=[]
    if num<1:
        divisors.append(0)
    i=1
    while(i*i<=num):
        if(num%i==0):
            if(num//i != i):
                divisors.extend([i,num//i])
            else:
                divisors.append(i)
        i+=1
    return sorted(divisors)

print(printalldivisor(4))
             
