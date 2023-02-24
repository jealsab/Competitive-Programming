class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        res_s=[]
        res_t=[]
        for i in range(len(s)):
            if s[i]!="#":
                res_s.append(s[i])
                print(res_s)
            else:
                if res_s:
                    res_s.pop()
        for j in range(len(t)):
            if t[j]!="#":
                res_t.append(t[j])
                print(res_t)
            else:
                if res_t:
                    res_t.pop()
        return res_s==res_t