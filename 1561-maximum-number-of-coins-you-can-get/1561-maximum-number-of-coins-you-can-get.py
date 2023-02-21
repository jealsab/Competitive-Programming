class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res=0
        i=0
        j=len(piles)-2
        while j>=0 and i<len(piles)/3:
            res+=piles[j]
            j-=2
            i+=1
        return res
