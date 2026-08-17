class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        N = len(s)

        def helper(start_idx, curr_ans, ans):
            if start_idx >= N:
                ans.append(curr_ans[:])
                return
            for idx in range(start_idx, N):
                sub_str = s[start_idx: idx + 1]
                if sub_str == sub_str[::-1]:
                    helper(idx + 1, curr_ans + [sub_str], ans)
            
        ans = []
        helper(0, [], ans)
        return ans

