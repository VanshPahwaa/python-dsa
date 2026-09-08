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


    def sortList(self):
        if(self.head is None or self.head.next is None):
            return 
        
        self.head=self.mergeSort(self.head)
        return 

    def mergeSort(self,head):
        if(head==None or head.next==None):
            return head
        middle=self.findmiddle(head)
        right=middle.next
        middle.next=None
        lefthead=self.mergeSort(self.head)
        righthead=self.mergeSort(right)
        return self.merge(lefthead,righthead)

    def findmiddle(self,temp):
        if temp is None or temp.next is None:
            return 
        slow,fast=temp,temp
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        return slow

    def merge(self,lefthead,righthead):
        itr1=lefthead
        itr2=righthead
        dummynode=Node(-1)
        temp=dummynode
        while(itr1!=None and itr2!=None):
            if(itr1.data<itr2.data):
                temp.next=Node(itr1.data)
                itr1=itr1.next
            else:
                temp.next=Node(itr2.data)
                itr2=itr2.next
            temp=temp.next

        if(itr1):
            temp.next=itr1
        if(itr2):
            temp.next=itr2
        return dummynode.next
            

        

                
ll=LinkedList()
ll.insert_values([5,3,7,2])
ll.print()
ll.sortList()
ll.print()