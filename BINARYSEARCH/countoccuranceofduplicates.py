class Solution:
    def searchRange(self, nums, target: int) ->int:
        first=self.firstoccurance(nums,target)
        if(first==-1):
            return 0
        second=self.lastoccurance(nums,target)
        return ((second+1)-first)
        # return [first,second].
    def firstoccurance(self,nums,target):
        left=0
        right=len(nums)-1
        ans=-1
        while(left<=right):
            mid=left+(right-left)//2
            if(target==nums[mid]):
                ans=mid
                right=mid-1
            elif(target>nums[mid]):
                left=mid+1
            else:
                right=mid-1
        return ans

    def lastoccurance(self,nums,target):
        left=0
        right=len(nums)-1
        ans=-1
        while(left<=right):
            mid=left+(right-left)//2
            if(target==nums[mid]):
                ans=mid
                left=mid+1
            elif(target>nums[mid]):
                left=mid+1
            else:
                right=mid-1
        return ans
obj=Solution()
print(obj.searchRange([5,8,8,10],7))