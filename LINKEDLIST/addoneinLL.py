class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)
    
    def addone(self,temp):
        if(temp==None):
            return 1
        carry=self.addone(temp.next)
        sum=temp.data+carry
        if(sum>9):
            temp.data=0
            return 1
        else:
            temp.data=sum
            return 0
    #through backtracking
    def addoneLL(self):
        if(self.head!=None):
            carry=self.addone(self.head)
            if(carry):
                newnode=Node(1)
                newnode.next=self.head
                self.head=newnode
            


ll=LinkedList()
ll.insert_values([9,9,9])
ll.print()
ll.addoneLL()
ll.print()
