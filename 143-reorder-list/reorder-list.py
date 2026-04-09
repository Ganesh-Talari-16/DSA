# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
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
        
        temp1 = head
        temp2 = prev        
        while temp2:
            nxt = temp1.next
            temp1.next = temp2
            temp1 = temp2
            temp2 = nxt
            

        



