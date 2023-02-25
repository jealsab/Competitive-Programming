class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i]+=nums[i-1]
        return nums
        # prf_sum=[]
        # added=0
        # for i in range(len(nums)):
        #     added+=nums[i]
        #     prf_sum.append(added)
        # return prf_sum
            
            