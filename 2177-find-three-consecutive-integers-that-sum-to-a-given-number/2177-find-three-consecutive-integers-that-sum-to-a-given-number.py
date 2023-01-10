class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        z=num%3
        if z==0:
            return[int(num/3-1),int(num/3),int(num/3+1)]
        else:
            return []
        
        
        
