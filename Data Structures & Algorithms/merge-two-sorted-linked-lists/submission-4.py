# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from math import inf

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sentinal = ptr = ListNode(0)

        l1 = p1 = list1
        l2 = p2 = list2

        while l1 or l2:
            if not l1:
                ptr.next = l2
                break
            if not l2:
                ptr.next = l1
                break
            
            n1 = l1.val if l1 else inf
            n2 = l2.val if l2 else inf
            if n1 < n2:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next
        
        return sentinal.next