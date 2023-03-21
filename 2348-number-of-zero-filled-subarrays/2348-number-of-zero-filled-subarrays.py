class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        n = 0
        
        for i in nums:
            if i == 0: 
                n += 1
            else: 
                n = 0
            res += n
            
        return res