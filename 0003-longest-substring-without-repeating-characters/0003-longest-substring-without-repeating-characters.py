class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        maxLength = 0
        dict = []
        while j < len(s):
            if s[j] not in dict:
                dict.append(s[j])
                j += 1
                maxLength = max(maxLength, j-i)
            else:
                dict.remove(s[i])
                i += 1
        return maxLength