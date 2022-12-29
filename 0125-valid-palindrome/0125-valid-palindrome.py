class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p=[]
        for character in string.punctuation:
            s= s.lower()
            s = s.replace(character, '')
        s= s.replace(" ","")
        i=len(s)
        while i >0:
            p.append(s[i-1])
            i-=1
        d= "".join(p)
        if d==s:
            return True
        else: 
            return False