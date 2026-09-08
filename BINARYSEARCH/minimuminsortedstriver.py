import sys


def findinsorted(nums):
    left = 0
    right = len(nums) - 1
    ans = sys.maxsize 
    while left <= right:
        mid = left + (right - left) // 2
        if nums[left] <= nums[right]:
            ans = min(ans, nums[left])
            break
        elif nums[mid] >= nums[left]:
            ans = min(ans, nums[left])
            left=mid+1
        else:
            ans = min(ans, nums[mid])
            right=mid-1
    return ans


print(findinsorted([7, 8, 9, 0, 1, 2, 3, 4, 5, 6]))
