#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        
        a.sort()  
        b.sort()
    
        i = j = 0  
    
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                i += 1
            elif a[i] == b[j]:
                i += 1
                j += 1
            else: 
                return False
    
        return j == len(b)