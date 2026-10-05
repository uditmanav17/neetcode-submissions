import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        visited = set()
        minH = [(0, 0)]  # (cost, node index)

        while len(visited) < n:
            cost, i = heapq.heappop(minH)
            if i in visited:
                continue
            res += cost
            visited.add(i)
            xi, yi = points[i]
            for j in range(n):
                if j not in visited:
                    xj, yj = points[j]
                    d = abs(xi - xj) + abs(yi - yj)
                    heapq.heappush(minH, (d, j))
        return res