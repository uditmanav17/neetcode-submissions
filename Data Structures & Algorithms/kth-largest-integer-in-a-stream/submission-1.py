from heapq import heappush, heappop, heapify

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapify(self.min_heap)
        # Keep only the k largest elements
        while len(self.min_heap) > k:
            heappop(self.min_heap)
    
    def add(self, val: int) -> int:
        heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heappop(self.min_heap)
        return self.min_heap[0]