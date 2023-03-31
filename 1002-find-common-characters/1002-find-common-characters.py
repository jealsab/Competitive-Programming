class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])
      
        res = []
        for i in range(1, len(words)):
            s = Counter(words[i])
            
            for c in count:
                if s[c] > 0:
                    count[c] = min(count[c], s[c])
                else:
                    count[c] = 0
                    
        for i in count:
            for j in range(count[i]):
                res.append(i)
            
        return res