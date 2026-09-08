# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         windowsize=len(s)
#         while(windowsize>=2):
#             i=0
#             while(i+windowsize<=len(s)):
#                 if(s[i:i+windowsize]==s[i:i+windowsize][::-1]):
#                     return s[i:i+windowsize]
#                 i+=1    
#             windowsize-=1
#         return s[0]

# optimised approach
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res="" 
        resLen=1
        for i in range(len(s)):
            l,r=i,i
            #checking for odd substring
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if(resLen<r-l+1):
                    res=s[l:r+1]
                    resLen=r-l+1
                l-=1
                r+=1
            l,r=i,i+1
            #checking for even string
            while(l>0 and r<len(s) and s[l]==s[r]):
                if(resLen<r-l+1):
                    res=s[l:r+1]
                    resLen=r-l+1
                l-=1
                r+=1
        return res
    
obj=Solution()
print(obj.longestPalindrome("babad"))
