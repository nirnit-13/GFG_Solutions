class Solution:
    def getSecondLargest(self, arr):
        lar = -1
        lar2 = -1
        
        for i in range(0, len(arr)):
            if arr[i] > lar:
                lar2 = lar
                lar = arr[i]
            elif arr[i] > lar2 and arr[i] != lar:
                lar2 = arr[i]
        return lar2