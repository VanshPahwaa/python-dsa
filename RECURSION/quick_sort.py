# def quick_sort(arr,start,end):
#     if(start<=end):
#         return 
#     pi=sort(arr,start,end)
#     quick_sort(arr,start,pi-1)
#     quick_sort(arr,pi+1,end)

# def sort(arr,start,end):
    
#     pi=start+int((end-start)/2)
#     i=start+1
#     j=end
#     while(i<=j):
#         while(i<=end and arr[i]<=arr[pi] ):
#             i=i+1

#         while(j>=start and arr[j]>arr[pi] ):
#             j=j-1
        
#         if(i<j):
#             swap(arr,i,j)

#     swap(arr,pi,i)
#     return j


def swap(my_arr,findex,sindex):
    # my_arr[findex]=my_arr[sindex]-my_arr[findex]
    # my_arr[sindex]=my_arr[sindex]-my_arr[findex]
    # my_arr[findex]=my_arr[sindex]+my_arr[findex]
    temp=my_arr[sindex]
    my_arr[sindex]=my_arr[findex]
    my_arr[findex]=temp

# arr=[3,7,5,2,1,9,4]
# quick_sort(arr,0,7)
# print(arr)

def quicksort(alist, start, end):
    '''Sorts the list from indexes start to end - 1 inclusive.'''
    if start<end:
        p = partition(alist, start, end)
        quicksort(alist, start, p-1)
        quicksort(alist, p + 1, end)
 
 
def partition(alist, start, end): 
    pi=start+int((end-start)/2)
    pivot = alist[pi]
    i = start
    j = end
 
    while i<j:
        while (alist[i] <= pivot and i <= end-1 ):
            i = i + 1
        while (alist[j] > pivot and j >= start+1 ):
            j = j - 1
 
        if i < j:
            swap(alist,i,j)
    swap(alist,pi,j)
    return j
 
# alist = input('Enter the list of numbers: ').split()
# alist = [int(x) for x in alist]
alist=[5,4,6,9,7,23,2,5,6,5]
quicksort(alist, 0, len(alist)-1)
print(alist)