def rotated_binarysearch(my_array,target,s,e):
    if(s>e):
        return -1
    mid=s+((e-s)//2)
    if(target==my_array[mid]):
        return mid
    if(my_array[s]<my_array[mid]):
        if(target<my_array[mid] and target>=my_array[s]):
            return rotated_binarysearch(my_array,target,s,mid-1)
        else:
            return rotated_binarysearch(my_array,target,mid+1,e)
    
    if(target>my_array[mid] and target<=my_array[e]):
        return rotated_binarysearch(my_array,target,mid+1,e)
    
    return rotated_binarysearch(my_array,target,s,mid-1)

print(rotated_binarysearch([6,7,8,9,1,2,3,4,5],2,0,8))

