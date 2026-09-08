class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class LinkedList:
    def __init__(self):
        self.head=None
    
    def insertatbeg(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode

    def print(self):
        if(self.head is None):
            print("Linked list is empty")
        else:
            itr=self.head
            llstr=""
            while(itr):
                llstr+=str(itr.data)+"--->" if itr.next else str(itr.data)
                itr=itr.next
            print(llstr)

    def deleteatbeg(self):
        if self.head.next is None:
            self.head=None
        else:
            self.head=self.head.next
            self.head.prev=None

    def insert_at_index(self,data,index):
        newnode=Node(data)
        if(index<0):
            print("not at relvant index")
        elif(index==0):
            self.insertatbeg(data)
        else:
            count=0
            itr=self.head
            while(itr!=None and count!=index):
                itr=itr.next
                count+=1

            if(itr!=None):        
                newnode.prev=itr.prev
                newnode.prev.next=newnode
                newnode.next=itr
                itr.prev=newnode
            else:
                print("index out of range")
                

   

if __name__ == '__main__':    
    ll=LinkedList()
    ll.insertatbeg(2)
    ll.insertatbeg(4)
    ll.insertatbeg(8)
    # ll.update_at_index(6,2)
    ll.insert_at_index(3,1)

    # ll.deleteatbeg()
    ll.print()
            
