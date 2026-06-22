# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #  A -> B -> C
        #  p    c    n
        if not head:
            return None

        cur = head
        prev = None

        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        
        return prev
