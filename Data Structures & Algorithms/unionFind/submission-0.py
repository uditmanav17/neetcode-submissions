class UnionFind:
    
    def __init__(self, n: int):
        self.n = n
        self.parents = {i:i for i in range(n)}
        self.num_components = n
        

    def find(self, node: int) -> int: 
        parents = self.parents
        if parents[node] != node:
            parents[node] = self.find(parents[node])
        return parents[node]
        

    def isSameComponent(self, x: int, y: int) -> bool: 
        p1 = self.find(x)
        p2 = self.find(y)
        return p1 == p2


    def union(self, x: int, y: int) -> bool:
        p1 = self.find(x)
        p2 = self.find(y)
        if p1 == p2:
            return False
        elif p1 < p2:
            self.parents[p2] = p1
        else:
            self.parents[p1] = p2
        self.num_components -= 1
        return True

    def getNumComponents(self) -> int:
        return self.num_components