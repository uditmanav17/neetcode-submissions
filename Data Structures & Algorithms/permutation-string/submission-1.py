from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = Counter(s1)
        s2_counts = Counter()
        l = 0
        for r, char in enumerate(s2):
            s2_counts[char] = s2_counts.get(char, 0) + 1
            while l <= r and s2_counts[char] > s1_counts.get(char, 0):
                s2_counts[s2[l]] -= 1
                l += 1
            if s2_counts == s1_counts:
                return True
        return False


        