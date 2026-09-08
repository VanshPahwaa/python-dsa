def linear_search(arr,target,index):
    if(index==len(arr)):
        return -1
    if(target==arr[index]):
        return index
    return linear_search(arr,target,index+1)

def findalloccurence(arr,target,index):
    return helper(arr,target,index,[])


def helper(arr,target,index,my_list):
    if(index==len(arr)):
        return my_list
    if(target==arr[index]):
        my_list.append(index)
    return helper(arr,target,index+1,my_list)



def findalloccurence2(arr,target,index):
    my_list=[]
    if(index==len(arr)):
        return my_list
    if(target==arr[index]):
        my_list.append(index)
    return my_list + findalloccurence2(arr,target,index+1)


# print(linear_search([2,6,7,8,9,1,55,4],55,0))
print(findalloccurence2([4,6,4,9,78,56,6,7,78],78,0))