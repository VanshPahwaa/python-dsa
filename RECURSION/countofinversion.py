def merge(arr,start,end):
    if(start>=end):
        return 0
    mid=start+(end-start)//2
    l=merge(arr,start,mid)
    r=merge(arr,mid+1,end)
    return sort(arr,start,mid,end)+l+r
    

def sort(arr,start,mid,end):
    first=start
    second=mid+1
    sortedarr=[]
    count=0
    while(first<=mid and second<=end):
        if(arr[first]<arr[second]):
            sortedarr.append(arr[first])
            first+=1
        else:
            count+=mid-first+1
            sortedarr.append(arr[second])
            second+=1
    
    if first<=mid:
        while(first<=mid):
            sortedarr.append(arr[first])
            first+=1
    if second<=end:
        while(second<=end):
            sortedarr.append(arr[second])
            second+=1
   
    for i in range(start,end+1):
        arr[i]=sortedarr[i-start]
    return count

# sampledata=[5,3,74,9,6,7,1,3]
sampledata=[2,5,1,9,0,7,3]
print(merge(sampledata,0,len(sampledata)-1))
print(sampledata)