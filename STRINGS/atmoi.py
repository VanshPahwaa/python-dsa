class Solution:
    def myAtoi(self, s: str) -> int:
        start=0
        newval="0"
        sign=1
        isstarted=False
        while(start<=len(s)-1):
            if(isstarted):
                if(s[start]>='0' and s[start]<='9'):
                    newval+=s[start]
                else:
                    break
            else:
                if(s[start]=="-"):
                    sign=-1
                elif(s[start]>='0' and s[start]<='9'):
                    newval+=s[start]
                    isstarted=True
                elif(s[start]>='a' and s[start]<='z' or s[start]>="A" and s[start]<="Z"):
                    break
                else:
                    pass
            start+=1
        newval=sign*int(newval)
        range=2**31
        # print(range)
        if(newval>=range-1):
            return range-1
        elif(newval<=-1*range):
            return sign*range
        return newval
        
obj=Solution()                  
print(obj.myAtoi("+   ____ 78"))
            

            
