class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       
        i = 0 
        while i < len(nums):
            idx = nums[i] 
            if nums[i] < len(nums) and nums[i] != i:
                nums[i], nums[idx] = nums[idx], nums[i] 
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i]!= i:
                return i
        return i+1