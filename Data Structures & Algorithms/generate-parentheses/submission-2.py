class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def helper(left, right, curr, ans):
            if len(curr) == 2 * n:
                ans.append("".join(curr))
                return
            if left < n:
                helper(left + 1, right, curr + ["("], ans)
            if right < left:
                helper(left, right + 1, curr + [")"], ans)
        
        ans = []
        helper(0, 0, [], ans)
        return ans
