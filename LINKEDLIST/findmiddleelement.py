# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        itr=head
        count=0
        while(itr):
            itr=itr.next
            count+=1
        mid=count//2+1
        midNode=head
        while(midNode):
            mid-=1
            if(mid==0):
                return midNode
            midNode=midNode.next
             
            
        return midNode
        