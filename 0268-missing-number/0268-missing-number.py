class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        count=Counter(nums)
        n=len(nums) #2
        for i in range(n+1):
            if i not in count:
                return i