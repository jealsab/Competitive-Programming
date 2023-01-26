class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = {}
        res = 0
        for x in nums:
            if k - x in count and count[k - x] > 0:
                # print(count[k-x],k,x)
                res += 1
                count[k - x] -= 1 
                
            elif x not in count:
                count[x] = 1
            else:
                count[x] += 1
        
        return res