# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(
        self, 
        root: Optional[TreeNode],
        mini = -math.inf,
        maxi = math.inf
    ) -> bool:
        if not root:
            return True
        condn = mini < root.val < maxi
        return (
            condn
            and self.isValidBST(root.left, mini, root.val)
            and self.isValidBST(root.right, root.val, maxi)
        )
        