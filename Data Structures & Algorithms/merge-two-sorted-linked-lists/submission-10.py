# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        i,j=0,0
        prev=ListNode()
        cnt=0
        if list1 is None: return list2
        if list2 is None: return list1
        while list1 and list2:
            temp = None
            if (list1.val) <= (list2.val):
                prev.next = list1
                temp = list1.next
                prev= list1
                list1.next = list2
                list1 = temp
                if cnt==0: head = prev

            else:
                prev.next = list2
                temp = list2.next
                prev= list2
                list2.next = list1
                list2 = temp
                if cnt==0: head = prev
            cnt+=1
        if list1:
             prev.next = list1
        else:
             print(list2.val)
             
             prev.next = list2
        return head
