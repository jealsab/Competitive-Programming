# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
            
        
        dummy = ListNode(0)
        result = dummy 
        curr = 0
        while l1 or l2 or curr:
            if l1:
                curr += l1.val
                l1 = l1.next
            if l2:
                curr += l2.val
                l2 = l2.next
            
            result.next = ListNode(curr%10)
            result = result.next
            curr = curr//10
            
        return dummy.next