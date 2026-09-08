# 796
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if(goal==s):
            return True
        else:
            for i in range(0,len(goal)):
                goal=goal[-1]+goal[0:-1]
                if(s==goal):
                    return True
        return False