class Solution:         
    def partition(self, head: ListNode, k: int) -> ListNode:
        if head == None: 
            return None  
        
        low = ListNode()
        high = ListNode()
        l = low 
        h = high
        while head != None:                                                 
            if head.val < k :
                l.next = head
                l = l.next
            else:
                h.next = head
                h = h.next
            head=head.next

        l.next = high.next
        h.next = None   

        return low.next                            
    
    