def removeduplicates(nums):
    i=0
    while i<= len(nums)-2 :
        if(nums[i]==nums[i+1]):
            nums.pop(i)
        else:
            i+=1
    return nums

def removeDuplicates( nums) -> int:
        write = 1
        prev = nums[0]
        read = 1
        while read < len(nums):
            while read < len(nums) and nums[read] <= prev:
                if read == len(nums) - 1:
                    return write
                read += 1
            prev = nums[read]
            nums[read], nums[write] = nums[write], nums[read]
            write += 1
            read += 1
        return write


def removeDuplicates( nums: list[int]) -> int:
        n=len(nums)
        if(n==1):
            return 1
        base=0
        comparer=1
        while(comparer<n):
            if(nums[base]==nums[comparer]):
                comparer+=1
            else:
                nums[base+1]=nums[comparer]
                base+=1
        
        return base+1


print(removeDuplicates([1,2,3,3,4,4,5]))
        