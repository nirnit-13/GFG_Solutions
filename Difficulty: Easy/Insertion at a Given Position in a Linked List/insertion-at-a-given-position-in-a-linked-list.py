'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    def insertPos(self, head, pos, val):
        a = Node(val)
        current = head
        
        if head == None:
            return a
            
        elif pos == 1:
            a.next = head
            head = a
            return head
            
        else:
            for i in range(1, pos -1):
                current = current.next
            a.next = current.next
            current.next = a
            
        return head
                
      
      