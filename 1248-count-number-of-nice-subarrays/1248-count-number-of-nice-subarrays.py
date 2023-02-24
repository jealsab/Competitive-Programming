class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        size=len(nums)
        for i in range(0,size):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        count=0
        freq={}
        prfxsum=0
        size=len(nums)
        for i in range(size):
            prfxsum+=nums[i]
            if prfxsum==k: 
                count+=1
            if prfxsum-k in freq:
                count+=freq[prfxsum-k]   
            if prfxsum in freq:
                freq[prfxsum]+=1
            else:
                freq[prfxsum]=1
            
        return count
        