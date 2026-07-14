# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def encode_tree(self, node):
        if not node:
            return "#"
        return f"{node.val} {self.encode_tree(node.left)} {self.encode_tree(node.right)}"

    def isSubtree(
        self, 
        root: Optional[TreeNode], 
        subRoot: Optional[TreeNode]
    ) -> bool:
        encode_tree = self.encode_tree(root)
        encode_subtree = self.encode_tree(subRoot)
        return encode_subtree in encode_tree

        