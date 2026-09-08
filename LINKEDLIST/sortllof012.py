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
        firstone,firstzero,firsttwo=None,None,None
        lastone,lastzero,lasttwo=None,None,None
        
        while(temp):
            if(temp.data==0):
                if(firstzero is None):
                    firstzero=temp
                    lastzero=temp
                else:
                    lastzero.next=temp
                    lastzero=temp   
            elif(temp.data==1):
                if(firstone is None):
                    firstone=temp
                    lastone=temp
                else:
                    lastone.next=temp
                    lastone=temp
            else:
                if(firsttwo is None):
                    firsttwo=temp
                    lasttwo=temp
                else:
                    lasttwo.next=temp
                    lasttwo=temp
            temp=temp.next

        if(firstzero):
            lastzero.next=firstone if firstone else firsttwo
            if(firstone):
                lastone.next=firsttwo if firsttwo else None
            elif(firsttwo):
                lasttwo.next=None
            else:
                lastzero.next=None
            self.head=firstzero
        else:
            if(firstone):
                lastone.next=firsttwo if firsttwo else None
                if(firsttwo):
                    lasttwo.next=None
                self.head=firstone

            else:
                lasttwo.next=None
                self.head=firsttwo



ll=LinkedList()
ll.insert_values([0,0,0,0,0,2,27])
ll.print()
ll.sortllof012()
ll.print()

