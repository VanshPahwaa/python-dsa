class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        result = [-1] * n
        stack = []

        for i in range(2 * n):
            num = nums[i % n]  # Circular array logic
            while stack and nums[stack[-1]] < num:
                result[stack.pop()] = num
            if i < n:
                stack.append(i)

        return result

obj=Solution()
print(obj.nextGreaterElements([1,2,1]))