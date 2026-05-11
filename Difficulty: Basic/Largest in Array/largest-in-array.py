class Solution:
    def largest(self, arr):
        largest = 0
        for i in range(0, len(arr)):
            if arr[i] > largest:
                largest = arr[i]
        return largest
        
