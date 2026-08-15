"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, arr: List[Interval]) -> bool:
        arr.sort(key = lambda x: x.start)
        N = len(arr)

        for i in range(N - 1):
            if arr[i].end > arr[i + 1].start:
                return False
        
        return True
