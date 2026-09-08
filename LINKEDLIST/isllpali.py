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
    
    def reverseList(self,head):
        itr=head
        temp=None
        last=None
        while(itr):
            temp=itr.next
            itr.next=last
            last=itr
            itr=temp

        return last



    def isPalindrome( self) -> bool:
        slow,fast=self.head,self.head.next
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next

        secondhead=self.reverseList(slow.next)
        firsthead=self.head
        while(secondhead is not None):
            if(firsthead.data!=secondhead.data):
                return False
            secondhead=secondhead.next
            firsthead=firsthead.next
        return True 







def isPalindrome(head) -> bool:
        slow,fast=head,head.next
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next

        secondhead=reverse(slow.next)
        printing(secondhead)
        firsthead=head
        while(secondhead is not None):
            if(firsthead.data!=secondhead.data):
                return False
            secondhead=secondhead.next
            firsthead=firsthead.next
        return True 

def reverse(head):
        if(head==None or head.next==None):
            return head
        itr=head
        last=None
        rlst=""
        while(itr):
            # rlst+=itr.data
            temp=itr.next            
            itr.next=last
            last=itr
            itr=temp
        return last

def printing(head):
        if head is None:
            print("Linked list is empty")
            return
        itr = head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)
        # print(head.data)
        


ll=LinkedList()
ll.insert_values([1,1,2,1])
ll.print()
print(ll.isPalindrome())
# ll.reverseList()
# head=reverse(ll.head)
# printing(reverse(ll.head))
# printing(ll.head)
# print(isPalindrome(ll.head))
