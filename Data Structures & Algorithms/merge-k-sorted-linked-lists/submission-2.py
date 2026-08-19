# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappush, heappop

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for idx, l in enumerate(lists):
            if l:
                heappush(heap, (l.val, idx, l))
        
        sentinal = ptr = ListNode(0)
        while heap:
            val, idx, node = heappop(heap)
            ptr.next = node
            if node.next:
                node = node.next
                heappush(heap, (node.val, idx, node))
            ptr = ptr.next
        
        return sentinal.next

        