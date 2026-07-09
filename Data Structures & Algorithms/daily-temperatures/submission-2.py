class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stk = []
        for idx, ele in enumerate(temperatures):
            while stk and temperatures[stk[-1]] < ele:
                s_idx = stk.pop()
                ans[s_idx] = idx - s_idx
            stk.append(idx)
        return ans
