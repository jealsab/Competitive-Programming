class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         # i = 0
        total = 0
        j = 0
        res = float("inf")
        
#         if sum(nums)<target:
#             return 0
        
        for i in range(0, len(nums)):
            total+=nums[i]
            while total >= target  and j < len(nums):
#                 j += 1
                total -= nums[j]
                res=min(res,i-j+1)
                j+=1
        if res ==  float("inf"):
            return 0
        return res
#             # print(i,j)
#             res = min(res, j - i + 1)
#             total -= nums[i]
#             print(total)

#         # i += 1
        
#         return res
    
        
        