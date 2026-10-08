"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        maps = {}
        h1 = head

        while h1:
            maps[h1] = Node(h1.val)
            h1 = h1.next

        h2 = head
        while h2:
            h2_cpy = maps.get(h2)
            h2_cpy.next = maps.get(h2.next, None)
            h2_cpy.random = maps.get(h2.random, None)
            h2 = h2.next
        return maps[head]
