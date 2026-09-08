# def secondlargest(nums):
#     ind=0
#     largest=0
#     dupp=nums
#     while(ind<=len(nums)-1):
#         if nums[ind]>nums[largest]:
#             largest=ind
#         ind+=1
#     ind=0   
#     dupp.pop(largest)
#     secondlargest=0
#     while(ind<=len(dupp)-1):
#         if nums[ind]>nums[secondlargest]:
#                 secondlargest=ind
#         ind+=1
#     return nums[secondlargest]


# print(secondlargest([5,4,3,2,1]))

# APPROACH TWO 
def secondLargestElement(nums):
    if len(nums) < 2:
            return -1

    large = float('-inf')
    second_large = float('-inf')

    # Loop through the numsay to find the second largest element
    for i in range(len(nums)):
        # Update the largest and second largest values
        if nums[i] > large:
            second_large = large
            large = nums[i]
        elif nums[i] > second_large and nums[i] != large:
            second_large = nums[i]
    if(second_large==float("-inf")):
        return -1

    return second_large  

print(secondLargestElement(nums=[1,2,3,4,5,6,7,8,9,10]));
        




# O(n)
# sc O(N)

