class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] 
        min_val = nums[0]
        
        for n in nums:
            while stack and stack[-1][0] <= n:
                min_val = min(min_val, stack.pop()[0])
                
            if stack and n > stack[-1][1]:
                return True
                
            stack.append([n, min_val])

        return False