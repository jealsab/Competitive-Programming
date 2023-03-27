# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:  
        res= []
        st = []
        i = 0
        while head:
            res.append(0)
            val = head.val
            while len(st) > 0 and st[-1][1] < val:
                res[st.pop()[0]] = val
            st.append((len(res)-1, val))  
            head = head.next
            i += 1
        return res
    