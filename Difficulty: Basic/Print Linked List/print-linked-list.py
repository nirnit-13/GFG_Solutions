'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    def printList(self, head):

        ans = []
        current = head

        while current:
            ans.append(current.data)
            current = current.next

        return ans