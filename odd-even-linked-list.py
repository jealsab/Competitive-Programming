# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
       
        if not head or not head.next:
            return head
        head_even, odd, even = head.next, head, head.next
        while odd and even and even.next:
            odd.next = even.next
            odd = odd.next
            if odd:
                even.next = odd.next
                even = even.next

        odd.next = head_even
        return head