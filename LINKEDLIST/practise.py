class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def insertatbeg(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            temp=self.head
            self.head=newnode
            self.head.next=temp
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


    def deletebyIndex(self,index):
        itr=self.head
        if(index<0 and index>self.getlength()-1):
            print("index out of range")
        count=0
        while count+1!=index:
            count+=1
            itr=itr.next 

        itr.next=itr.next.next
        itr.next.prev=itr

    def insertatspecific(self,index,data):
        if(index<0 ):
            print("invalid index")
        elif(index==0):
            return self.insertatbeg(data)
        else:
            itr=self.head
            count=0
            while(itr!=None and count+1!=index):
                count+=1
                itr=itr.next
            if(itr!=None):
                temp=Node(data)
                temp.next=itr.next
                itr.next=temp
            else:
                print('index is not available')
        return 
    
    def insert_at_end(self,data):
        itr=self.head
        newnode=Node(data)
        if(itr is None):
            itr=newnode
        while(itr.next!=None):
            itr=itr.next

        itr.next=newnode

    def update_at_index(self,data,index):
        if(index<0):
            print("invalid index")
        else:
            count=0
            itr=self.head
            while itr!=None and count!=index:
                count+=1
                itr=itr.next
            if(itr!=None):
                itr.data=data
            else:
                print("index not found")

ll=LinkedList()
ll.insertatbeg(2)
ll.insertatbeg(4)
ll.print()
        
