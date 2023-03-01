class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        count=0

        freq=defaultdict(int)
        
        prfxsum=0
        
        for i in range(len(nums)):
            
            prfxsum+=nums[i]
            
            if prfxsum %k==0: 
                count+=1
                
            if prfxsum%k in freq:
                count+=freq[prfxsum%k]   
                
           
            
            freq[prfxsum%k]+=1
            
        return count
