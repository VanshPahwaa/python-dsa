class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        windowsize=len(part)
        i=0
        while(part in s):
            while(i+windowsize<=len(s)):
                if(s[i:i+windowsize]==part):
                    s=s[:i]+s[i+windowsize:]
                    i=0
                else:
                    i+=1        
        return s

obj = Solution()
print(obj.removeOccurrences(
    "tyqjskoqvgpujduoxvqaagtttyqjskoqvgpujduoxvqaagtyqjstyqjskoqvgpujduoxvqaagtkoqvgpujduotyqjskoqvgpujduoxvqaagtxvqaagtjgdjx",
    "tyqjskoqvgpujduoxvqaagt",
))

# tyqjskoqvgpujduoxvqaagtttyqjskoqvgpujduoxvqaagtyqjskoqvgpujduoxvqaagtjgdjx