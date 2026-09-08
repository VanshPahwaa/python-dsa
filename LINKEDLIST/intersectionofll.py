def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        itr1=headA
        itr2=headB
        while(itr1!=itr2):
            itr1=itr1.next
            itr2=itr2.next
            if(itr1==itr2):
                return itr1
            if(itr1==None):
                itr1=headB
            if(itr2==None):
                itr2=headA
        return itr1