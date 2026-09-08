# def issorted(nums):
#     for i in range(0,len(nums)-1):
#         if(nums[i]>nums[i+1]):
#             return False
        
#     return True

#issorted and rotated
# def check( nums):
#     ind=0
#     while(ind<=len(nums)-2):
#         if(nums[ind]<=nums[ind+1]):
#             ind+=1
#         else:
#             break

#     if(ind==len(nums)-1):
#         return True
#     ind+=1
#     for i in range(0,len(nums)-1):
#         if(nums[ind%len(nums)]>nums[(ind+1)%len(nums)]):
#             return False
#         ind+=1
#     return True

# print(check([6,10,6]))
# print([5,4,3,2,1][::-1])

# class Solution:
#     def check(self, nums) -> bool:
#         n = len(nums)
#         for r in range(n):
#              cs = []

#              for i in range(r,n):
#                 cs.append(nums[i])
#              for i in range(r):
#                 cs.append(nums[i])
            
#              is_sorted = True
#              for i in range(n-1):
#                 if cs[i] > cs[i+1]:
#                     is_sorted = False
#                     break

#              if is_sorted:
#                 return True

#         return False 

# obj=Solution()
# print(obj.check([2,3,4,5,1]))

#optimised
class Solution:
    def check(self, nums) -> bool:
        count, n = 0, len(nums)
        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                count += 1
                if count > 1: return False
        return True
          
        

