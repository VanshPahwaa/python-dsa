def findpermutation(map,comb,ans,nums):
    if(len(comb)==len(nums)):
        ans.append(comb.copy())
        print(comb)
        return 
    
    i=0
    for i in range(0,len(nums)):
        if(map[i]==0):
            comb.append(nums[i])
            map[i]=1
            findpermutation(map,comb,ans,nums)
            comb.pop()
            map[i]=0
    
        
nums=[1,2,3]
ans=[]
map={i:0 for i in range(0,len(nums))}
findpermutation(map,[],ans,nums)
print(ans)
