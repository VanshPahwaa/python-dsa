 def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head is None or head.next is None):
            return head
        
        parentitr=head
        while(parentitr):
            itr=head.next
            previtr=head
            ppitr=None
            while(itr):
                if(previtr.val>itr.val):
                    if(ppitr==None):
                        previtr.next=itr.next
                        itr.next=previtr
                        head=itr
                    else:
                        previtr.next=itr.next
                        itr.next=previtr
                        ppitr.next=itr
                ppitr=previtr
                previtr=itr
                itr=itr.next
            parentitr=parentitr.next
        return head