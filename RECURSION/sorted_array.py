def sorted_array(my_array,index):
    if(index==len(my_array)-1):
        return True
    
    return my_array[index]<=my_array[index+1] and sorted_array(my_array,index+1)

print(sorted_array([1,2,3,4,5,5],0))