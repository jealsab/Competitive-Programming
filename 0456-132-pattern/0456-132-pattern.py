class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        j = float('-inf')
        stack = []
        nums= nums[::-1]
        
        for n in nums:
            if n < j:
                return True
            
            while stack and stack[-1] < n:
                j = stack.pop()
            stack.append(n)
            
        return False
