# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ls = []
        p = head
        while p != None:
            ls.append(p.val)
            p = p.next
        
        l = 0
        r = len(ls) - 1
        while l <= r:
            if ls[l] != ls[r]:
                return False
            l += 1
            r -= 1
        return True
        