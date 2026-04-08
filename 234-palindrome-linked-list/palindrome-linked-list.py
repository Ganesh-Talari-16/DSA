# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head 
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # This is for Reversing 
        def rev(node):
            current = node
            prev = None
            while current:
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt
            return prev
       


        half = rev(slow)
        first , second = head , half
        while second:
            if first.val != second.val :
                return False
            first = first.next
            second = second.next
        return True

        