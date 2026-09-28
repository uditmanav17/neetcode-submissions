# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from math import gcd

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        while ptr and ptr.next:
            mid = ListNode(gcd(ptr.val, ptr.next.val))
            mid.next = ptr.next
            ptr.next = mid
            ptr = mid.next  # == the original next node
        return head
