class Solution:
    def trap(self, height) -> int:
        l,total=0,0
        r=len(height)-1
        rmax,lmax=0,0
        while(l<r):
            if(height[l]<=height[r]):
                if(lmax>height[l]):
                    total+=lmax-height[l]
                else:
                    lmax=height[l]
                l+=1
            else:
                if(rmax>height[r]):
                    total+=rmax-height[r]
                else:
                    rmax=height[r]
                r-=1
        return total
    
obj=Solution()
print(obj.trap([0,1,0,2,1,0,1,3,2,1,2,1]))

        