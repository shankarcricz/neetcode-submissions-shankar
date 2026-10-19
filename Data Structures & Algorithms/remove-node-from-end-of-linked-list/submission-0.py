# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head
        size = 0
        while dummy:
            dummy = dummy.next
            size+=1
        removeInd = size-n
        ind = 0
        dummy = curr = head
        prev = ListNode()
        while curr:
            if ind == removeInd:
                print("removing ", curr.val )

                prev.next = curr.next
                if ind==0: return head.next
                return head
            prev = curr
            curr = curr.next
            ind+=1
        


        