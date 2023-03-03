class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
                
        def eatFinish(mid):
            hours = 0
            for pile in piles:
                  hours+= ceil(pile/mid) 
            return hours   


        low = 1
        high = max(piles)

        while low < high:
            mid = (low + high)//2

            if eatFinish(mid)<= h :
                high = mid 

            else:
                low = mid+1

        return high
  