class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = {}
        res = 0
        for i in nums:
            if k - i in count and count[k - i] > 0:
                res += 1
                count[k - i] -= 1 
                
            elif i not in count:
                count[i] = 1
            else:
                count[i] += 1
        
        return res