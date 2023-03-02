class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # [1,0,1,0,1], goal = 2
#          1 1 2 2 3 
        count=0
        freq={}
        prfxsum=0
        size=len(nums)
        for i in range(size):
            prfxsum+=nums[i]
            if prfxsum==goal: 
                count+=1
            if prfxsum-goal in freq:
                count+=freq[prfxsum-goal]   
            if prfxsum in freq:
                freq[prfxsum]+=1
            else:
                freq[prfxsum]=1
            
        return count
