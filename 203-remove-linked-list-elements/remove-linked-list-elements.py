# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        
        while start.next:
            if start.next.val == val :
                start.next = start.next.next
            else:
                start = start.next
        return dummy.next