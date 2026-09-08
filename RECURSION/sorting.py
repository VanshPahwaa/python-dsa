def quick_sort(my_arr,piteration,citeration):
    if(piteration<0):
        return my_arr
    if(citeration<piteration):
        if(my_arr[citeration]>my_arr[citeration+1]):
            swap(my_arr,citeration)
        return quick_sort(my_arr,piteration,citeration+1)
    else:
        return quick_sort(my_arr,piteration-1,0)
    




def swap(my_arr,index):
    my_arr[index]=my_arr[index+1]-my_arr[index]
    my_arr[index+1]=my_arr[index+1]-my_arr[index]
    my_arr[index]=my_arr[index+1]+my_arr[index]




print(quick_sort([5,6,7,4,9,8,5,3],7,0))