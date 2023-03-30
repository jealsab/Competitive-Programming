class Solution:
    def findComplement(self, num: int) -> int:
        bit_mask_amount = 2**(num.bit_length()) - 1 
        
        return (num ^ bit_mask_amount)

    