# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hare = turtle = head
        ind =0
        while (hare and hare.next):
            if ind!=0 and hare.val == turtle.val:
                return True
            hare = hare.next.next
            turtle = turtle.next
            ind+=1
        return False