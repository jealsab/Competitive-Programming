class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count_p=Counter(p)
        k = len(p)
        res=[]
        count_s=Counter(s[:k-1])
        for i in range(len(s)-k+1):
            count_s[s[i+k-1]]+=1
            if count_p==count_s:
                res.append(i)
            count_s[s[i]]-=1
            # if count_s[s[i]]==0:
            #     del count_s[s[i]]
        return res
#         count_curr=Counter(s[:k])

#         ans = []
#         if count_curr == count_p:
#             ans.append(0)

#         for i in range(k, len(s)):
#             count_curr[s[i]] += 1
#             count_curr[s[i-k]] -= 1

#             if count_curr == count_p:
#                 ans.append(i-k+1)

#         return ans
                
                
                
                
                
                
                