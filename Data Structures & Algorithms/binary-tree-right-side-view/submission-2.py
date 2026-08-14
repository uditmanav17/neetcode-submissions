# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = {}
        max_depth = 0
        q = deque([(root, 1)])
        while q:
            node, depth = q.popleft()
            max_depth = max(max_depth, depth)
            ans[depth] = node.val
            for child in (node.left, node.right):
                if child:
                    q.append((child, depth + 1))
        return [ans[k] for k in range(1, max_depth + 1)]

        