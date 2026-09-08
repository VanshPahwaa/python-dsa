import sys
def findnext(newarr,arr,length,ans):
    if(length==len(newarr)):
        ans.append(newarr.copy())
        print(newarr)
        return
    minimum=-sys.maxsize-1
    i=0
    while(i<=len(arr)-1):
        newarr.append(arr[i])
        arr.pop(i)
        findnext(newarr,arr,length,ans)
        arr.insert(i,newarr[-1])
        newarr.pop()
        i+=1
    return ans
def findnexpermutation(arr):
    ans=findnext([],sorted(arr),len(arr),[])
    print(ans,arr)
    index=next(x for x in range(0,len(ans))if ans[x]==arr)
    return ans[index+1]


print(findnexpermutation([1,2,3]))
        