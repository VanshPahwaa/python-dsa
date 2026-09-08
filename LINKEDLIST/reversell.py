# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        itr=head
        stackarr=[]
        while(itr):
            stackarr.append(itr.val)
            itr=itr.next
        itr2=head
        while(itr2):
            itr2.val=stackarr.pop()
            itr2=itr2.next

        return head