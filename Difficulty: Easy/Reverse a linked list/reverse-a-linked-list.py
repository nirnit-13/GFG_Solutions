'''
# Node Class
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
'''

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr is not None:
            next_node = curr.next  # Store the next node
            curr.next = prev       # Reverse the link
            
            # Move pointers forward
            prev = curr
            curr = next_node
            
        return prev  # prev is the new head