class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_idx = 0
        for s_idx, s_char in enumerate(s):
            if t_idx < len(t) and s_char == t[t_idx]:
                t_idx += 1
        return len(t) - t_idx