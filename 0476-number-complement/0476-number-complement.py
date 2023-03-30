class Solution:
    def findComplement(self, num: int) -> int:
        # s = ~num
        lst= []
        s = bin(num)
        for i in range(2, len(s)):
            if s[i] == '1':
                lst.append('0')
            else:
                lst.append('1')
        a = "".join(lst)
        q = '0b'+ a
        return int(q,2)
    