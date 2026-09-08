class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node


    def reverseList(self):
        last=None
        itr=self.head
        self.head=self.findreverseLL(itr,last)

    def findreverseLL(self,itr,last):
        if(itr==None):
            return last
        front=itr.next
        itr.next=last
        last=itr
        itr=front
        return self.findreverseLL(itr,last)

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


LL=LinkedList()
LL.insert_at_begining(2)
LL.insert_at_begining(4)
LL.insert_at_begining(7)
LL.insert_at_begining(9)

LL.reverseList()
LL.print()
