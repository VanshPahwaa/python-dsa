class Node:
    def __init__(self, data, next_node=None, back_node=None):
        self.data = data
        self.next = next_node
        self.back = back_node

class LinkedList:
    def convert_arr_to_dll(arr):
        # Create the head node with the first element of the array
        head = Node(arr[0])
        # Initialize 'prev' to the head node
        prev = head

        for i in range(1, len(arr)):
            # Create a new node with data from the array and set its 'back' pointer to the previous node
            temp = Node(arr[i], None, prev)
            # Update the 'next' pointer of the previous node to point to the new node
            prev.next = temp
            # Move 'prev' to the newly created node for the next iteration
            prev = temp

        # Return the head of the doubly linked list
        return head
    
    def print_dll(head):
        while head is not None:
            # Print the data in the current node
            print(head.data, end=" ")
            # Move to the next node
            head = head.next

    def delete_tail(head):
        if head is None or head.next is None:
            return None  # If the list is empty or has only one node, return None

        tail = head
        while tail.next is not None:
            # Traverse to the last node (tail)
            tail = tail.next

        new_tail = tail.back
        new_tail.next = None
        tail.back = None

        # Free memory of the deleted node
        del tail

        return head