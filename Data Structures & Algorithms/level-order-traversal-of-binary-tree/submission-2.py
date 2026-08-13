# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans

        q = deque([root])
        while q:
            N = len(q)
            curr_lvl = []
            for _ in range(N):
                node = q.popleft()
                curr_lvl.append(node.val)
                for child in (node.left, node.right):
                    if child:
                        q.append(child)
            ans.append(curr_lvl[:])
        return ans


        