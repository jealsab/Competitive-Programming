class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = list(s)
        print(s)
        i, j = 0, 0
        output = ''
        while i < len(res) and j < len(spaces):
            if i == spaces[j]:
                output += " "
                j += 1
            else:
                output += res[i]
                i += 1
        return output + ''.join(res[i:])