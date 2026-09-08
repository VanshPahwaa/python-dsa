class Solution:
    def twoSum(self, nums, target: int):
        freq={}
        
        pointer=0
        while(pointer<=len(nums)-1):
            rem=target-nums[pointer]
            if(rem in freq):
                return [pointer,freq[rem]]
            else:
                freq[nums[pointer]]=pointer    
            pointer+=1


# incase only need to return true or false on the basis of presence

class Solution:
    def twoSum(self, nums, target: int) :
        nums.sort()
        right,left=len(nums)-1,0
        while(left<right):
            if(nums[left]+nums[right]==target):
                return True
            elif(nums[left]+nums[right]>target):
                right-=1
            else:
                left+=1
        return False           
            
        
        
        
        