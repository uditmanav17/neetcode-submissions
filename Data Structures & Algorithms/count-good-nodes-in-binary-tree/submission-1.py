# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from math import inf

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0
        q = deque([(root, -inf)])
        while q:
            node, path_max = q.popleft()
            if node.val >= path_max:
                # print(node.val, path_max)
                good_nodes += 1
            for child in (node.left, node.right):
                if child:
                    q.append((child, max(path_max, node.val)))
        return good_nodes
        