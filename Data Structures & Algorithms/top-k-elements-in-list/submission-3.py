from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        ans = []
        for num, cnt in counts.items():
            heappush(ans, (cnt, num))
            if len(ans) > k:
                heappop(ans)
        return [i for _, i in ans]
        