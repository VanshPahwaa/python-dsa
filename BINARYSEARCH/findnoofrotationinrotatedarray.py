import sys


def findrotation(nums):
    left = 0
    right = len(nums) - 1
    ans = sys.maxsize 
    rotation=0
    while left <= right:
        mid = left + (right - left) // 2
        if nums[left] <= nums[right]:
            if(ans > nums[left]):
                ans=nums[left]
                rotation=left
                break
        elif nums[mid] >= nums[left]:
            if ans>nums[left]:
                ans=nums[left]
                rotation=left
            left=mid+1
        else:
            if ans>nums[mid]:
                ans=nums[mid]
                rotation=mid
            right=mid-1
    return rotation


print(findrotation([7, 8, 9, 0, 1, 2, 3, 4, 5, 6]))
