import sys
def findnextpermutation(arr):
    pointer=len(arr)-1
    while(pointer>0):
        if(arr[pointer]>arr[pointer-1]):
            break
        pointer-=1
    if(pointer==0):
        return arr[::-1]

    else:
        breakelement=arr[pointer-1]
        min=sys.maxsize
        minIndex=-1
        for i in range(pointer,len(arr)):
            if(arr[i]<min and arr[i]>breakelement):
                minIndex=i    
        temp=arr[minIndex]
        arr[minIndex]=arr[pointer-1]
        arr[pointer-1]=temp

    arr[pointer:]=arr[len(arr)-1:pointer-1:-1]
    return arr

print(findnextpermutation([2,3,1]))


            