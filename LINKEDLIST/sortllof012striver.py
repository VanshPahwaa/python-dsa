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

    def sortllof012(self):
        if(self.head is None ):
            return 
        
        temp=self.head
        firstone,firstzero,firsttwo=Node(-1),Node(-1),Node(-1)
        lastone,lastzero,lasttwo=firstone,firstzero,firsttwo
        
        while(temp):
            if(temp.data==0):
                lastzero.next=Node(0)
                lastzero=lastzero.next  
            elif(temp.data==1):
                lastone.next=Node(1)
                lastone=lastone.next
            else:
                lasttwo.next=Node(2)
                lasttwo=lasttwo.next
            temp=temp.next
        lastzero.next=firstone.next if firstone.next else firsttwo.next
        lastone.next=firsttwo.next
        lasttwo.next=None
        self.head=firstzero.next
        

ll=LinkedList()
ll.insert_values([1,1,1])
ll.print()
ll.sortllof012()
ll.print()

