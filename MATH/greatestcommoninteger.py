def greatestofcommoninteger(num1,num2):
    minimum=min(num1,num2)
    maximum=max(num1,num2)
    c=1
    goc=1
    while(c*c<=minimum):
        if(minimum%c==0):
            if(maximum%c==0):
                goc=max(goc,c)
            if(maximum%(minimum//c)==0):  
                goc=max(goc,minimum//c)
        
        c+=1

    return goc

print(greatestofcommoninteger())
