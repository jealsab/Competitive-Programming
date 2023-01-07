class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        nums1=num1.split("+")
        nums2=num2.split("+")
      

        num1R=int(nums1[0])
        num1I=int(nums1[1][:-1])
        num2R=int(nums2[0])
        num2I=int(nums2[1][:-1])
        
        return str((num1R*num2R-num1I*num2I))+ "+"+str((num1R*num2I+num1I*num2R))+"i"