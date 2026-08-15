"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import heappop, heappush

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        heap = []
        for inte in intervals:
            start, end = inte.start, inte.end
            if heap and heap[0] <= start:
                heappop(heap)
            heappush(heap, end)

        return len(heap)
