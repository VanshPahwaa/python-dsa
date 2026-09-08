class Solution:

    def toLowerCase(self,ch):
    # if((ch>='a' and ch<='z') or (ch>=0 or ch<9)):
    #     return ch
        if(ch>='A' and ch<="Z"):
            return chr(ord(ch)-ord('A')+ord('a'))
        else:
            return ch
    
    def isvalid(self,ch):
        if((ch>='0' and ch<='9') or (ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
            return True
        else:
            return False
    def isPalindrome(self, str: str) -> bool:
        start=0
        end=len(str)-1
        while(start<end):
            if(self.isvalid(str[start])):
                if(self.isvalid(str[end])):
                    first=self.toLowerCase(str[start])
                    second=self.toLowerCase(str[end])
                    if(first == second ):
                        start+=1
                        end-=1
                    else:
                        return False
                else:
                    end-=1
            else:
                start+=1

        return True
    
obj=Solution()
print(obj.isPalindrome("A man, a plan, a canal: Panama"))