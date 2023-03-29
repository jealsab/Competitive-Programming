class Solution:
    def countBits(self, n: int) -> List[int]:
        lst = []
        for i in range(n+1):
            count = 0
            s = list(bin(i))
            s = s[2:]
            arr = list(map(int, s))
            lst.append(sum(arr))
        return lst
    
         
            