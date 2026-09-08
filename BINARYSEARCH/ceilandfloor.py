# def searchfloor(nums, target: int) -> int:
#         left=0
#         right=len(nums)-1
#         while(left<=right):
#             mid=left+(right-left)//2
#             if(nums[mid]==target):
#                 return nums[mid]
#             elif(nums[mid]>target):
#                 right=mid-1
#             else:
#                 left=mid+1
#         return nums[right]

def searchfloor(nums, target: int) -> int:
        left=0
        right=len(nums)-1
        floor=-1
        ceil=-1
        while(left<=right):
            mid=left+(right-left)//2
            if(nums[mid]==target):
                return [nums[mid],nums[mid]]
            elif(nums[mid]<target):
                floor=nums[mid]
                left=mid+1

            else:
                ceil=nums[mid]
                right=mid-1
        return [floor,ceil]


def searchceil( nums, target: int) -> int:
        left=0
        right=len(nums)-1
        while(left<=right):
            mid=left+(right-left)//2
            if(nums[mid]==target):
                return nums[mid]
            elif(nums[mid]>target):
                right=mid-1
            else:
                left=mid+1
        return nums[left]

print(searchfloor([3, 4, 4, 7, 8, 10],8))
print(searchceil([3, 4, 4, 7, 8, 10],8))