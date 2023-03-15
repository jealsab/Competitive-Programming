class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1:
            return 0
        if k %2 ==0:
            return 1 - self.kthGrammar(n-1, ceil(k/2))
        return self.kthGrammar(n-1, ceil(k/2))


















#     if n == 1:
#             return 0
#         if n > 1:
#             s=self.kthGrammar(n-1,k)
#             if s ==0:
#                 return int('01')
#             elif s==1:
#                 return 10
#         return s[k]
        