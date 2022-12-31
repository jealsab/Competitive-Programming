class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """   
        pair = 0
        n= len(nums)
        for i in range(n):
            for j in range(n):
                if(nums[i]==nums[j] and i < j):
                    pair +=1
        return pair 

    
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         count = 0
#         n= len(nums)
#         for i in range(n):
#             for j in range(n):
#                 if(nums[i]==nums[j] and i < j):
#                     count +=1
#         return count 
