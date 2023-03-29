class Solution:
    def countBits(self, n: int) -> List[int]:
        lst = []
        for i in range(n+1):
            count = 0
            s = bin(i)
            for i in range(2, len(s)):
                if s[i] == '1':
                    count += 1     
            lst.append(count)
        return lst
    
         
            