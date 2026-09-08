def infixtoprefix(string1):
    i=0
    n=len(string1)
    ans=""
    stack=[]
    while(i<n):
        if(string1[i]>="A" and string1[i]<="Z" or string1[i]>="a" and string1[i]<="z" or string1[i]>="0" and string1[i]<="9"):
            ans+=string1[i]
        elif(string1[i]=="("):
            stack.append(string1[i])
        elif(string1[i]==")"):
            while(len(stack)!=0 and stack[-1]!="("):
                ans+=stack[-1]
                stack.pop()
            stack.pop()
        else:
            while(len(stack)!=0 and priority(string1[i])<=priority(stack[-1] )):
                  ans+=stack[-1]
                  stack.pop()
            stack.append(string1[i])
        i+=1    
    while(len(stack)!=0):
        ans+=stack[-1]
        stack.pop()
    return ans


def priority(x):
    if(x=="^"):
        return 3
    elif(x=="*" or x=="/"):
        return 2
    elif(x=="+" or x=='-'):
        return 1
    else:
        return -1
    
print(infixtoprefix("a+b*(c^d-e)"))