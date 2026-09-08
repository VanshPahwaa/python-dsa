def findkthsequence(seq,k,ans,totalnum,n,arr):
    if(n==0 or len(arr)==0):
        ans.append(seq)
        return 
    b=k//fact(n-1)
    k=k%fact(n-1)
    seq=seq+f"{arr[b]}"
    arr.pop(b)
    findkthsequence(seq,k,ans,totalnum,n-1,arr)

def fact(n):
    if(n<=1):
        return 1
    return n*fact(n-1)

k=17
ans=[]
arr=[1,2,3,4]
findkthsequence("",k-1,ans,len(arr),len(arr),arr)
print(ans)