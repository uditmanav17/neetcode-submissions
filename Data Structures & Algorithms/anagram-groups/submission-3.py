from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def compute_hash(word):
            encode = [0] * 26
            for char in word:
                encode[ord(char) - ord('a')] += 1
            return tuple(encode)

        hashes = defaultdict(list)
        for word in strs:
            curr_hash = compute_hash(word)
            hashes[curr_hash].append(word)
        return [i for i in hashes.values()]
        