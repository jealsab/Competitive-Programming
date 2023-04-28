class Solution(object):
    def largestMerge(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        i = 0
        j = 0
        res = ""

        while i < len(word1) and j <  len(word2):
            if word1[i] > word2[j]:
                res+=word1[i]
                i+= 1

            elif word1[i] < word2[j]:
                res+=word2[j]
                j+= 1

            else:
                if word1[i:] > word2[j:]:
                    res+=word1[i]
                    i+= 1
                else:
                    res+=word2[j]
                    j += 1
        return res+word1[i:]+word2[j:]