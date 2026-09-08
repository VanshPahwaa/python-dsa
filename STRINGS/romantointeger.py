class Solution:
    def romanToInt(self, s: str) -> int:
        if(s=='I'):
            return 1
        elif(s=='V'):
            return 5
        elif(s=='X'):
            return 10
        elif(s=='L'):
            return 50
        elif(s=='C'):
            return 100
        elif(s=='D'):
            return 500
        elif(s=='M'):
            return 1000
        else:
            r=self.romanToInt(s[-1])
            l=self.romanToInt(s[:-1])
            if(r>l):
                return r-l
            else:
                return r+l
            
obj=Solution()
print(obj.romanToInt("IXXV"))