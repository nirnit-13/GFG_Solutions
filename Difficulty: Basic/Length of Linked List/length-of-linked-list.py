'''
Definition for Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def getCount(self, head):
        count = 0
        current = head

        while current:
            current = current.next
            count += 1
        return count