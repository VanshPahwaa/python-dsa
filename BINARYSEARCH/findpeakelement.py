def  findpeak(nums):
    left=1
    n=len(nums)
    right=n-2
    if(1==n):
        return 0
    if(nums[0]>nums[1]):
        return 0
    if(nums[n-2]<nums[n-1]):
        return n-1
    while(left<=right):
        mid=left+(right-left)//2
        if(nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]):
            return mid
        elif(nums[mid]>nums[mid-1]):
            left=mid+1
        elif(nums[mid]>nums[mid+1]):
            right=mid-1
        else:
            right=mid-1
    return -1 

print(findpeak([1,2,3,1]))