"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, root: Optional['Node']) -> Optional['Node']:
        nodes_map = {}

        def clone(node):
            if node in nodes_map:
                return nodes_map[node]
            new_node = Node(node.val)
            nodes_map[node] = new_node
            for nbrs in node.neighbors:
                new_node.neighbors.append(clone(nbrs))
            return new_node
        
        return clone(root) if root else None

        