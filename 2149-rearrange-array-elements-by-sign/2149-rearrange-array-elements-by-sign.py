class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_idx=0
        negative_idx=1
        result=[0]*len(nums)
        for i in range (len(nums)):
            if nums[i]>0:
                result[positive_idx]=nums[i]
                positive_idx+=2
            else:
                result[negative_idx]=nums[i]
                negative_idx+=2
        return result
                