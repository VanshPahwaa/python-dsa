def combinationsumI(ind,target,arr,com,ans):
    if(target==0):
        ans.append(com[:])
        return
    elif(ind==len(arr)):
        return
    if(arr[ind]<=target):
        com.append(arr[ind])
        combinationsumI(ind,(target-arr[ind]),arr,com,ans)
        com.pop()
    combinationsumI(ind+1,target,arr,com,ans)

my_list=[2,3,6,7]
ans=[]
combinationsumI(0,7,my_list,[],ans)
print(ans)
