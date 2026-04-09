# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Edge Case
        if not head or not head.next:
            return 

        slow = head 
        fast = head
        # Find the mid 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid  = slow

        
        current = mid.next
        prev = None
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        mid.next = None
        
        #merge 
        tempA = head
        tempB = prev        
        while tempA and tempB:
            A_nxt = tempA.next
            B_nxt = tempB.next

            tempA.next = tempB
            tempB.next = A_nxt

            tempA = A_nxt
            tempB = B_nxt
           
            
    

        



