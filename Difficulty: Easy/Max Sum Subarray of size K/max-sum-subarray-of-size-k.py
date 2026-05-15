class Solution:
    def maxSubarraySum(self, arr, k):
        
        curr_sum = sum(arr[:k])
        max_sum = curr_sum
        
        if k == 0 or k > len(arr):
            return 0
            
        for i in range(k,len(arr)):
            curr_sum = curr_sum + arr[i] - arr[i-k]
            
            if curr_sum > max_sum:
                max_sum = curr_sum
                        
        return max_sum
                
        