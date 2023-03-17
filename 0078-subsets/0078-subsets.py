class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        occurence = set()

        def backtrack(start , curr):
            if tuple(curr) not in occurence:
                ans.append(curr.copy())
                occurence.add(tuple(curr))
            
            if start == len(nums):
                return
            for i in range(start, len(nums)):
                curr.append(nums[i])
                
                backtrack(i+1,curr)
                curr.pop()
                
        
        n = len(nums)  
        backtrack(0 , [])
        return ans
       