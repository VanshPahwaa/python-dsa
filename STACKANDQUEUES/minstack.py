

class MinStack:

    def __init__(self):
        self.stack=[]            
        self.min=0
    def push(self, val: int) -> None:
        if(len(self.stack)==0):
            self.min=val
            self.stack.append(val)
        else:
            if(val<self.min):
                self.stack.append(2*val-self.min)
                self.min=val
            else:
                self.stack.append(val)
    
    def pop(self) -> None:
        if(len(self.stack)==0):
            return 
        elif(len(self.stack)==1):
            self.stack.pop()
            self.min=None
        else:
            if(self.min>self.stack[-1]):
                self.min=(2*self.min-self.stack[-1])
                self.stack.pop()
            else:
                self.stack.pop()
        
    def top(self) -> int:
        if(len(self.stack)==0):
            return 
        if(self.min<self.stack[-1]):
            return self.stack[-1]
        return self.min
    
    def getMin(self) -> int:
        return self.min    


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

obj=MinStack()
obj.push(2)
obj.push(0)
obj.push(3)
obj.push(0)
print(obj.getMin())
print(obj.top())
obj.pop()
print(obj.top())
print(obj.getMin())
obj.pop()
print(obj.top())

print(obj.getMin())
obj.pop()
print(obj.getMin())
print(obj.top())

print(obj.top())



