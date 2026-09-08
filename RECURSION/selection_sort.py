def selection_sort(my_arr,index):
    if(index>len(my_arr)-1):
        return my_arr
    else:
        minIndex=findmin(my_arr,index)
        swap(my_arr,index,minIndex)
        return selection_sort(my_arr,index+1);

# def findmin(my_arr,index):
#     if(index==len(my_arr)-1):
#         return my_arr[index]
#     return min(my_arr[index],findmin(my_arr,index+1));

def findmin(my_arr,index):
    if(index==len(my_arr)-1):
        return index
    min=findmin(my_arr,index+1)
    return index if my_arr[index]<my_arr[min] else min


def swap(my_arr,findex,sindex):
    # my_arr[findex]=my_arr[sindex]-my_arr[findex]
    # my_arr[sindex]=my_arr[sindex]-my_arr[findex]
    # my_arr[findex]=my_arr[sindex]+my_arr[findex]
    temp=my_arr[sindex]
    my_arr[sindex]=my_arr[findex]
    my_arr[findex]=temp



# print(findmin([56,9,4,3,7,6,5],0))
print(selection_sort([56,9,4,3,7,6,5],0))
# print(findmin([56,9,4,3,7,6,5],0))