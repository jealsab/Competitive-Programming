class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count_p=Counter(p)
        k = len(p)
        res=[]
        count_curr=Counter(s[:k])

        ans = []
        if count_curr == count_p:
            ans.append(0)

        for i in range(k, len(s)):
            count_curr[s[i]] += 1
            count_curr[s[i-k]] -= 1

            if count_curr == count_p:
                ans.append(i-k+1)

        return ans
                
                
                
                
                
                
                