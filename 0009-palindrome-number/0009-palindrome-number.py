class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp=x
        rev=0
        while x>0:
            n=x%10
            rev=(rev*10)+n
            x/=10
        if rev==temp:
            return True
        else:
            return False
            
            
            
        