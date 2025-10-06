# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not (head.next):
            return False
        p1 = head
        p2 = head.next
        while p1 != p2:
            if p1 == None or p2 == None or p1.next == None or p2.next == None:
                return False
            p2 = p2.next.next
            p1 = p1.next
            
        return True