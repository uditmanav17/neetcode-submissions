from math import inf
from heapq import heappush, heappop

class Solution:
    def build_graph(self, edges):
        graph = {}
        for u, v, wt in edges:
            graph.setdefault(u, set())
            graph[u].add((v, wt))
        return graph

    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        dists = {i: inf for i in range(1, n + 1)}
        graph = self.build_graph(times)
        
        heap = [(0, k)]
        dists[k] = 0
        # print(dists)

        while heap:
            node_dist, node = heappop(heap)
            node_dist = abs(node_dist)
            for nbr, nbr_dist in graph.get(node, []):
                # print(node, node_dist, nbr, nbr_dist)
                if dists[nbr] > nbr_dist + node_dist:
                    dists[nbr] = nbr_dist + node_dist
                    heappush(heap, (-dists[nbr], nbr))
                    # print("-", dists)
        # print(dists)
        ans = max([v for _, v in dists.items()])
        return ans if ans != inf else -1
