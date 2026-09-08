def detectCycle(self, head):
        slow,fast=head,head
        while(fast!= None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                count=1
                slow=slow.next
                while(slow!=fast):
                   slow=slow.next
                   count+=1
                return count