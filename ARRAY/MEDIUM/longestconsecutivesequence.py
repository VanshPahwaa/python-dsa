# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         maxseq=0
#         for i in range(0,len(nums)):
#             target=nums[i]+1
#             j=0
#             cnt=1
#             while(j<=len(nums)-1):
#                 if nums[j]==target:
#                     target+=1
#                     j=0
#                     cnt+=1
#                 else:
#                     j+=1
#             maxseq=max(maxseq,cnt)
#         return maxseq
    
# class Solution:
#     def longestConsecutive(self, nums) -> int:
#         nums.sort()
#         maxseq=1
#         pointer=0
#         cnt=1
#         if(len(nums)==0):
#             return 0
#         while(pointer<=len(nums)-2):
#             if(nums[pointer]+1==nums[pointer+1]):
#                 cnt+=1
#             elif(nums[pointer]==nums[pointer+1]):
#                 pass
#             else:
#                 cnt=1
#             maxseq=max(maxseq,cnt)
#             pointer+=1
#         return maxseq

            

# optimised
def longestconsecutive(nums):
    st=set()
    for i in nums:
        st.add(i)

    if(len(nums)==0):
        return 0
    maxseq=1
    for i in range(0,len(nums)):
        cnt=0
        if nums[i]-1 not in st:
            x=nums[i]
            while(x in nums):
                x+=1
                cnt+=1
        maxseq=max(cnt,maxseq)
        
    return maxseq


print(longestconsecutive([1,1,2,3,4]))

        

