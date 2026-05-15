from collections import deque

class Solution:
    def firstNegInt(self, arr, k):
        n = len(arr)
        q = deque()  
        ans = []
        
        for i in range(n):
            if q and q[0] < i - k + 1:
                q.popleft()
                
            if arr[i] < 0:
                q.append(i)
                
            if i >= k - 1:
                if q:
                    ans.append(arr[q[0]])
                else:
                    ans.append(0)
                    
        return ans