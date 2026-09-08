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

    def oddEvenList(self):
        if(self.head==None or self.head.next==None or self.head.next.next==None):
            return self.head
        else:
            oldodd=self.head
            oldeven=self.head.next
            firsteven=self.head.next
            while(oldodd and oldodd.next and oldodd.next.next):
                oldodd.next=oldodd.next.next
                oldodd=oldodd.next
                if(oldeven.next.next!=None):
                    oldeven.next=oldeven.next.next
                    oldeven=oldeven.next
                self.print()

            oldodd.next=firsteven
            oldeven.next=None
            self.print()

    def oddEvenList(self, head):
        if(head==None or head.next==None):
            return head
        else:
            oldodd=head
            oldeven=head.next
            firsteven=head.next
            while(oldeven!=None and oldeven.next!=None):
                oldodd.next=oldodd.next.next
                oldodd=oldodd.next
                oldeven.next=oldeven.next.next
                oldeven=oldeven.next
            oldodd.next=firsteven
            return head
    
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
            


ll=LinkedList()
ll.insert_values([1,2,3,4,5])
ll.print()
ll.oddEvenList()
ll.print()
