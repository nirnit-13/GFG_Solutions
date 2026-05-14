class Solution:
    def maxWater(self, arr):
        max = 0
        left = 0
        right = len(arr)-1
        
        while left < right:
            water = (right - left) * min(arr[right], arr[left])

            if water > max:
                max = water

            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
        
        return max
        