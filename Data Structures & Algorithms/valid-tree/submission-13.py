class DSU:
    def __init__(self, n):
        self.parents = {i: i for i in range(n)}

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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        dsu = DSU(n)
        for u, v in edges:
            temp = dsu.union(u, v)
            if not temp:
                return False
        return True
        