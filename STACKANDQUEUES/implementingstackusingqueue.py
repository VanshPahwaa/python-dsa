class MyStack:
    def __init__(self):
        self.stack1=[]
       
    def enque(self,val):
        self.stack1.append(val)

    def deque(self):
        if(len(self.stack1)<=0):
            return 
        value=self.stack1.pop(0)
        return value 

    def topqueue(self):
        if(len(self.stack1)<=0):
            return None
        return self.stack1[0]

    def push(self, x: int) -> None:
        size=len(self.stack1)
        self.enque(x)
        for i in range(0,size):
            self.enque(self.topqueue())
            self.deque()

        
    def pop(self) -> int:
        if(len(self.stack1)<=0):
            return 
        return self.deque()
        
    def top(self) -> int:
        if(len(self.stack1)<=0):
            return 
        val=self.topqueue()
        return val
        

    def empty(self) -> bool:
        return len(self.stack1)<=0
    
obj=MyStack()
obj.push(2)
obj.push(5)
print(obj.pop())
print(obj.top())



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()