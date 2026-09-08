def findnumofsubarray(nums,k):
    prefixsum={0:1}
    sum=0
    cnt=0
    for i in range(0,len(nums)):
        sum+=nums[i]
        requiredprefix=sum-k
        if(requiredprefix in prefixsum):
            cnt+=prefixsum[requiredprefix]
        if(sum in prefixsum):
            prefixsum[sum]+=1
        else:
            prefixsum[sum]=1
    return cnt
    

# Optimised with using default dictionary
# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         res,curr_sum = 0,0
#         data = defaultdict(int)
#         data[0] = 1
#         for i,num in enumerate(nums):
#             curr_sum += num
#             res += data[curr_sum-k]
#             data[curr_sum] += 1
#         return res

print(findnumofsubarray([1,1,1],2))