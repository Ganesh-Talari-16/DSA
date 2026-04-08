# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        Lprev = dummy
        for _ in range(left - 1):
            Lprev = Lprev.next

        start = Lprev.next
        end = start

        for _ in range(right - left):
            end = end.next

        # Reverse logic 
        after = end.next
        prev = after
        current = start 
        while current != after :
            nxt = current.next 

            current.next = prev 
            prev = current
            current = nxt
        
        Lprev.next = prev
    
        return dummy.next