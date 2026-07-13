# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(node):
            if not node:
                # balanced, depth
                return True, 0
            
            l_balanced, l_depth = helper(node.left)
            r_balanced, r_depth = helper(node.right)

            curr_balanced = l_balanced and r_balanced and abs(l_depth - r_depth) <= 1

            return curr_balanced, max(l_depth, r_depth) + 1

        ans, _ = helper(root)
        return ans

        