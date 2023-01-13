class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        l = len(nums)
        j = 0
        
        for i in range(l-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        
        for i in range(l):
            if nums[i]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
        return nums