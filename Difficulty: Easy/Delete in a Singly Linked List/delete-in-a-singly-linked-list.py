'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def deleteNode(self, head, x):
        
        if x == 1:
            return head.next
            
        curr = head
        prev = None
        
        for i in range(0, x-1):
            prev = curr
            curr = curr.next
        prev.next = curr.next
            
        return head
        
