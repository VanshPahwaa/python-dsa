targetsum=3

def findsubsequences(arr):
    # listsubsequences(arr,0,[])
   return  listsubsequenceswithsumK(arr,0,[],0)


# list all subsequences
def listsubsequences(arr,index,subsqs):
    if(index==len(arr)):
        print(subsqs)
        return
    subsqs.append(arr[index])
    listsubsequences(arr,index+1,subsqs)
    subsqs.pop()
    listsubsequences(arr,index+1,subsqs)

# list all subsequences have sum equal to k

def listsubsequenceswithsumK(arr,index,subsqs,sum):
    if(index==len(arr)):
        global targetsum
        if(sum==targetsum):
            print(subsqs)
            return 1
        return 0
    subsqs.append(arr[index])
    sum=sum+arr[index]
    l=listsubsequenceswithsumK(arr,index+1,subsqs,sum)
    subsqs.pop()
    sum=sum-arr[index]
    r=listsubsequenceswithsumK(arr,index+1,subsqs,sum)

    return l+r
arr=[1,2,3]
print("the number of subsequences  are",findsubsequences(arr))