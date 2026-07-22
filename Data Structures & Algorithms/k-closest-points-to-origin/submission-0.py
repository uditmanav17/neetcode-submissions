import numpy as np
from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = np.linalg.norm(point)
            heappush(heap, (-dist, point))
            if len(heap) > k:
                heappop(heap)
        return [point for _, point in heap]

        