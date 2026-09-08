# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        slow=head
        fast=head
        # Step 2: Traverse the linked list
        # with the slow and fast pointers
        while fast is not None and fast.next is not None:
            # Move slow one step
            slow = slow.next
            # Move fast two steps
            fast = fast.next.next

            # Check if slow and fast pointers meet
            if slow == fast:
                return True  # Loop detected

            # If fast reaches the end of the
            # list, there is no loop
        return False
