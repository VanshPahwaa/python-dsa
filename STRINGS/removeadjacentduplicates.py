# 1047
class Solution:
    def removeDuplicates(self, s: str) -> str:
        ind = 0
        while ind <= len(s) - 1:
            if ind < len(s) - 1 and s[ind] == s[ind + 1]:
                s = s[0:ind] + s[ind + 2 : len(s)]
            elif ind > 0 and s[ind] == s[ind - 1]:
                s = s[0 : ind - 1] + s[ind + 1 : len(s)]
                ind-=1
            else:
                ind += 1

        return s


obj = Solution()
print(
    obj.removeDuplicates(
        "ehflcjmgljhbjecdbbikajfdmabbdcfdiahkaglkeibbfdcljcghhmfgfmfjjfaamlijgihiejmccfiigekaljkmfklldfikjgkb"
    )
)

# optimised
class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = []
        for c in s:
            # if the current character is same as the last one in `ans`
            # then we cannot push it to `ans`
            # we remove the one in `ans`
            if ans and ans[-1] == c: ans.pop()
            # otherwise, add the current character to `ans`
            else: ans.append(c)
        return ''.join(ans)

# class Solution:
#     def removeDuplicates(self, s: str) -> str:
#         ind=0
#         temp=list(s)

#         while(ind<=len(temp)-2):
#             if(temp[ind]==temp[ind+1]):
#                 del temp[ind:ind+2]
#             elif(ind>0 and temp[ind]==temp[ind-1]):
#                 del temp[ind-1:ind+1]
#             else:
#                 ind+=1

#         return "".join(temp)
