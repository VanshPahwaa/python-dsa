# # 205 problem
# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         ind=0
#         visited={char:False for char in s}
#         if(s==t):
#             return True
#         else:
#             while(ind<=len(s)-1):
#                 if(s[ind]==t[ind]):
#                     ind+=1
#                 else:
#                     if(visited[s[ind]]!=True):
#                         table=str.maketrans(f"{s[ind]}{t[ind]}", f"{t[ind]}{s[ind]}")
#                         s=s.translate(table)
#                         visited[s[ind]]=True
#                         if(s==t):
#                             return True
#                         ind+=1
#                     else:
#                         return s==t
#             return False


def isIsomorphic(s: str, t: str) -> bool:
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))

print(isIsomorphic("egg","add"))