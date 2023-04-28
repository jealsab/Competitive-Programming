# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """ 
        if not head.next: 
            return None 
        temp = head
        while n:
                temp = temp.next
                n -= 1
        if not temp: 
                return head.next 

        node = head
        while temp.next:
                node = node.next
                temp = temp.next

        if node: 
                node.next = node.next.next
        return head