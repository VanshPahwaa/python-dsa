# class Solution:
#     def maxSubArray(self, arr) -> int:
#         pointer=1
#         sum=arr[0]
#         maxsum=sum
        
#         while(pointer<=len(arr)-1):
#             if(sum<=0 ):
#                 maxsum=max(maxsum,arr[pointer])
#                 sum=arr[pointer]
            
#             else:
#                 sum+=arr[pointer]
#                 maxsum=max(maxsum,sum)
#             pointer+=1
#         return maxsum


# optimised
class Solution:
    def maxSubArray(self, arr) -> int:
        pointer,sum=0,0
        
        maxsum=arr[0]
        start=0
        substart,subend=0,0
        for pointer in range(0,len(arr)):
            if(sum<=0):
                sum=0
                start=pointer
            sum+=arr[pointer]

            if(maxsum<sum):
                substart=start
                subend=pointer                
            maxsum=max(maxsum,sum)
            
        return arr[substart:subend+1]
        # return maxsum

obj=Solution()
print(obj.maxSubArray([-2,-3,4,-1,-2,1,5,-3]))