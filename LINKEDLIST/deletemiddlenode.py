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

    def deletemiddleNode(self):    
        slow=self.head
        if(slow.next is None):
           return None
        fast=self.head.next.next
        
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        temp=slow.next
        slow.next=slow.next.next
        temp.next=None



ll=LinkedList()
ll.insert_values([1,2,3,4,5])
ll.print()
ll.deletemiddleNode()
ll.print()
        