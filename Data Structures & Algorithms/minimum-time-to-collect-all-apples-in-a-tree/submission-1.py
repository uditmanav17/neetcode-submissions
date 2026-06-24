from collections import defaultdict, deque


class Solution:
    def build_graph(self, edges):
        graph = defaultdict(list)
        indeg = defaultdict(int)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indeg[u] += 1
            indeg[v] += 1
        return graph, indeg


    def minTime(
        self, n: int, 
        edges: List[List[int]], 
        hasApple: List[bool]
    ) -> int:
        graph, indeg = self.build_graph(edges)
        q = deque([
            node 
            for node, deg in indeg.items() 
            if hasApple[node] == False and deg == 1 and node != 0
            # only leaf nodes without apples
        ])
        while q:
            curr_node = q.popleft()
            indeg[curr_node] -= 1
            for nbr in graph.get(curr_node, []):
                if indeg[nbr] > 0:
                    indeg[nbr] -= 1
                if not hasApple[nbr] and indeg[nbr] == 1 and nbr != 0:
                    q.append(nbr)
        # print(indeg)
        return sum(indeg.values())




