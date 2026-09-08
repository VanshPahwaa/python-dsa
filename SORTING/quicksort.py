def quicksort(arr,start,end):
    if(start>=end):
        return 
    p=partition(arr,start,end)
    quicksort(arr,start,p)
    quicksort(arr,p+1,end)

def partition(arr,start,end):
    pivotIndex=start
    l,r=start,end
    while(l<r):
        while(l<=end and arr[l]<=arr[pivotIndex]):
            l+=1
        while(r>=start and arr[r]>arr[pivotIndex]):
            r-=1
        if(l<r):
            arr[l],arr[r]=swap(l,r,arr)
    arr[pivotIndex],arr[r]=swap(pivotIndex,r,arr)
    return r

def swap(l,r,my_list):
    # my_list[l]=my_list[l]^my_list[r]
    # my_list[r]=my_list[l]^my_list[r]
    # my_list[l]=my_list[l]^my_list[r]
    # temp=my_list[l]
    # my_list[l]=my_list[r]
    # my_list[r]=temp
    return my_list[r],my_list[l]

my_list=[9,8,7,6,5,4,3,2,1]
quicksort(my_list,0,len(my_list)-1)
print(my_list)

