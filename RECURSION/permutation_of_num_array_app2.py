def findpermutation(ind,comb,ans):
    if(ind>=len(comb)-1):
        ans.append(comb.copy())
        return
    
    for i in range(ind,len(comb)):
        swap(comb,ind,i)
        ind+=1
        findpermutation(ind,comb,ans)
        ind-=1
        swap(comb,i,ind)
        


def swap(comb,ind,i):
    temp=comb[ind]
    comb[ind]=comb[i]
    comb[i]=temp


nums=[1,2,3]
ans=[]
findpermutation(0,nums,ans)
print(ans)
