class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first=l1
        second=l2
        carry=0
        newLL=ListNode(-1)
        temp=newLL
        while first or second:
            sum=carry
            if(first):
                sum+=first.val
            if(second):
                sum+=second.val

            temp.next=ListNode(sum%10)
            temp=temp.next
            carry=sum//10
            
            if(first):
                first=first.next
            if(second):
                second=second.next

        if(carry==1):
            temp.next=ListNode(1,None)
        
        return newLL.next
