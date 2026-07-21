from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-ele for ele in stones]
        heapify(heap)
        while len(heap) >= 2:
            n1 = heappop(heap)
            n2 = heappop(heap)
            if n1 == n2:
                continue
            else:
                diff = -abs(n1 - n2)
                heappush(heap, diff)
        return -heappop(heap) if heap else 0
