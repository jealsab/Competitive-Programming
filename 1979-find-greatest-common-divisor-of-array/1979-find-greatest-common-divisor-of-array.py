class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort() 
        def gcd(a, b):
             if b == 0:
                return (a)
             return gcd(b, a % b)
        return gcd(nums[0],nums[-1])
       