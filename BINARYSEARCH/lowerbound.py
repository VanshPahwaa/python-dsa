def findlowerbound(nums,target):
    left=0
    right=len(nums)-1
    while(left<=right):
        mid=left+(right-left)//2
        if(nums[mid]>=target):
            if(mid-1 >=0 and nums[mid-1] >=target):
                right=mid-1
            else:
                return mid
        else:
            left=mid+1
    return left

print(findlowerbound([1,2,3,3,7,8,9,9,9,11],10))