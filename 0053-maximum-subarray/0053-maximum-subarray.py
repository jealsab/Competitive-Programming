class Solution:
    def maxSubArray(self, nums: List[int]) -> int:           
        max_sum = nums[0]
        pre_sum = 0
        for i in range(len(nums)):  
            if pre_sum < 0:
                pre_sum = 0
            pre_sum += nums[i]
            if pre_sum > max_sum:
                max_sum = pre_sum
        return max_sum
    
    
#         max_sum=float("-inf")
#         pre_sum=nums[0]
#         for i in range(len(nums)):            
#             if  (pre_sum > nums[i]):
#                 pre_sum+=nums[i]
#             else:
#                 pre_sum=nums[i]
#             max_sum=max(max_sum,pre_sum)

#         return max_sum