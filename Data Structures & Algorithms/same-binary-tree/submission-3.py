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

    def isSameTree(
        self, 
        p: Optional[TreeNode], 
        q: Optional[TreeNode]
    ) -> bool:
        encoded_t1 = self.encode_tree(p)
        encoded_t2 = self.encode_tree(q)
        return encoded_t1 == encoded_t2
        