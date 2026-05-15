class Solution:
    def AllPossibleStrings(self, s: str):
        res = []
        
        def backtrack(index, current_str):
            if index == len(s):
                if current_str != "": 
                    res.append(current_str)
                return
            
            backtrack(index + 1, current_str + s[index])
            
            backtrack(index + 1, current_str)
            
        backtrack(0, "")
        
        res.sort()
        return res