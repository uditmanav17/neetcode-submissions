class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # ans = [0, 0, 0]
        t0, t1, t2 = target
        x = y = z = False
        for a, b, c in triplets:
            x |= (a == t0 and b <= t1 and c <= t2)
            y |= (a <= t0 and b == t1 and c <= t2)
            z |= (a <= t0 and b <= t1 and c == t2)
            if x and y and z:
                return True
        return False


        