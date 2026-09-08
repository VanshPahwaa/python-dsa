class Solution:
    def beautySum(self, s: str) -> int:

        if len(s) < 3:
            return 0
        sob=0
        for i in range(0,len(s)-2):
            for j in range(i,len(s)):
                max=0 
                freq={}
                for x in s[i:j+1]:
                    if x not in freq:
                        freq[x]=0
                    freq[x]+=1
                    if(max<freq[x]):
                        max=freq[x]
                sob+=(max-min(freq.values()))
        return sob
    
obj=Solution()
print(obj.beautySum("aabcb"))

