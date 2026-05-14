class Solution:
	def pushZerosToEnd(self, arr):
    	x = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[x] = arr[i]
                x += 1

        for i in range(x, len(arr)):
            arr[i] = 0

        return arr