class Solution:
    def findMin(self, nums) -> int:
        left=0
        right=len(nums)-1
        if(right==0):
            return nums[left]
        while(left<=right):
            mid=left+(right-left)//2
            if(nums[mid-1]>nums[mid]):
                return nums[mid]
            elif(nums[mid]<nums[left]):
                # if left is unsorted
                right=mid-1
            elif(nums[mid]>nums[right]):
                # if right is unsorted
                left=mid+1
            else:
                return nums[left]


            

        