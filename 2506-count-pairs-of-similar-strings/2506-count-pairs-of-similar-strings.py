class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count=0
        w=[set(word) for word in words]
        
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if w[i]==w[j]:
                    count+=1
        return count
       