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
# brute force
def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dictofnode={}
        itr=head
        while itr!=None:
            if(itr not in dictofnode):
                dictofnode[itr]=1
            else:
                return itr
            itr=itr.next
        return None
#optimized
 def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast=head,head
        while(fast!= None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                slow=head
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                return slow


ll=LinkedList()
ll.insert_values([])
ll.print()
