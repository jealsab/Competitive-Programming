class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1],c = (digits[-1]+1)%10 , (digits[-1]+1)//10
        for i in range(len(digits)-2,-1,-1):
            digits[i],c = (digits[i]+c)%10 , (digits[i]+c)//10
        if c:
            return [1] + digits
        return digits