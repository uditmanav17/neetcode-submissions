# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def helper(node):
            if not node:
                return 0, 0
            
            l_depth, l_dia = helper(node.left)
            r_depth, r_dia = helper(node.right)
            
            curr_dia = l_depth + r_depth
            return max(l_depth, r_depth) + 1, max(l_dia, r_dia, curr_dia)

        depth, dia = helper(root)
        # print(depth, dia)

        return dia
        