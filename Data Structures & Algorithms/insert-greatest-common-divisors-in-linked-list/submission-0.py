# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from math import gcd

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ptr = sentinal = head
        
        while ptr:
            next_node = ptr.next
            if next_node:
                mid_node = ListNode(gcd(ptr.val, next_node.val))
                mid_node.next = next_node
                ptr.next = mid_node
            ptr = next_node

        return head
