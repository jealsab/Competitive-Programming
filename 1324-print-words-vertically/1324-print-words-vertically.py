class Solution:
    def printVertically(self, s: str) -> List[str]:

        s = s.split()
        m = len(s)
        output = []
        n=0
        for word in s:
            n=max(n,len(word))
        for j in range(n):
            res = []
            for i in range(m):
                word = s[i]
                if j < len(word):
                    res.append(word[j])  
                else :
                    res.append(' ')
            output.append(''.join(res).rstrip())
        return output