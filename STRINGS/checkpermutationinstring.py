class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1=[0]*26
        for i in s1:
            count1[ord(i)-97]+=1

        count2=[0]*26
        i=0
        while(i<len(s2) and i<len(s1)):
            count2[ord(s2[i])-97]+=1
            i+=1
        

        if(count1==count2):
            return True
        lastupdatedInd=0
        for i in range(len(s1),len(s2)):
            count2[ord(s2[i])-97]+=1
            count2[ord(s2[lastupdatedInd])-97]-=1
            lastupdatedInd+=1
            if(count1==count2):
                return True
        return False        
            
obj=Solution()
print(obj.checkInclusion("ab","abc"))