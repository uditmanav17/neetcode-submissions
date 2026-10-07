class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for idx, (n_start, n_end) in enumerate(intervals):
            if not ans:
                ans.append(intervals[idx])
                continue
            p_start, p_end = ans[-1]
            if n_start <= p_end:
                merged_int = [
                    min(p_start, n_start),
                    max(p_end, n_end)
                ]
                ans[-1] = merged_int
            else:
                ans.append(intervals[idx])
        return ans