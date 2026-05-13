"""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
"""

class Solution:
    def insertAtFront(self, head, x):
        a = Node(x)
        a.next = head
        head = a
        
        return head
        
