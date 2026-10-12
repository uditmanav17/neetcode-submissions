class Solution:
    def makesquare(self, arr: List[int]) -> bool:
        total = sum(arr)
        side, rem = divmod(total, 4)
        arr.sort(reverse=True)
        if rem != 0 or arr[0] > side:
            return False

        ans = [0] * 4
        N = len(arr)

        def backtrack(idx):
            if idx == N:
                return True
            ele = arr[idx]
            for i in range(4):
                if ans[i] + ele <= side:
                    ans[i] += ele
                    if backtrack(idx + 1):
                        return True
                    ans[i] -= ele
                if ans[i] == 0:
                    break
            return False

        return backtrack(0)        


