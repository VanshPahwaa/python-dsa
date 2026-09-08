class Solution:
    def singleNonDuplicate(self, nums) -> int:
        left=0
        right=len(nums)-1
        while(left<=right):
            mid=left+(right-left)//2
            if(len(nums)==1):
                return mid

            if(left==right or (nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1])):
                return nums[mid]
            else:
                r=right-mid
                l=mid-left
                if(nums[mid]==nums[mid-1]):
                    l=l-1
                else:
                    r=r-1
                if(r==0 or r%2==0):
                    right=left+(l-1)
                else:
                    left=right-r+1
                

obj=Solution()       
print(obj.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
