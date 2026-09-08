def mergesort(arr,start,end):
    if(start>=end):
        return 

    mid=start+(end-start)//2
    mergesort(arr,start,mid)
    mergesort(arr,mid+1,end)
    sort(arr,start,mid,end)

def sort(arr,start,mid,end):
    l,r=start,mid+1
    sortedarr=[]
    while(l<=mid and r<=end):
        if(arr[l]<arr[r]):
            sortedarr.append(arr[l])
            l+=1
        else:
            sortedarr.append(arr[r])
            r+=1
    while(l<=mid):
        sortedarr.append(arr[l])
        l+=1
    while(r<=end):
        sortedarr.append(arr[r])
        r+=1
    
    for i in range(0,len(sortedarr)):
        arr[start+i]=sortedarr[i]

my_list=[8,7,6,5,4,3,2,1]
mergesort(my_list,0,len(my_list)-1)
print(my_list)
    
            
