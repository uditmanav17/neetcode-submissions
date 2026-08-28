

class DSU:
    def __init__(self, n):
        self.parents = {i: i for i in range(1, n + 1)}
        print(self.parents)

    def find(self, node):
        parents = self.parents
        if parents[node] != node:
            parents[node] = self.find(parents[node])
        return parents[node]
    
    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 == p2: 
            return False
        if p1 < p2:
            self.parents[p2] = p1
        else:
            self.parents[p1] = p2
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        dsu = DSU(N)
        for u, v in edges:
            if not dsu.union(u, v):
                return [u, v]
        
        