def findsingleelement(nums):
        n=len(nums)
        if(n==1):
            return nums[0]
        
        #these two condition are put to avoid to loop go out of range option for index  n+1 and -1
        if(nums[0]!=nums[1]):
            return nums[0]
        
        if(nums[n-1]!=nums[n-2]):
            return nums[n-1]
        left=1
        right=n-2
        while(left<=right):
            mid=left+(right-left)//2
            if(nums[mid]!=nums[mid+1] and nums[mid]!=nums[mid-1]):
                return nums[mid]
            elif(mid%2==0 and nums[mid]==nums[mid+1] or mid%2!=0 and nums[mid]==nums[mid-1]):
                left=mid+1
            else:
                right=mid-1

        return -1         
                    



