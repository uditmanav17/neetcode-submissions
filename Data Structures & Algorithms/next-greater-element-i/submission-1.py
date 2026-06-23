class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        N = len(nums2)
        ans = {}
        stk = []
        for idx, ele in enumerate(nums2):
            while stk and ele > stk[-1]:
                s_ele = stk.pop()
                ans[s_ele] = ele
            stk.append(ele)
        
        result = []
        for ele in nums1:
            result.append(ans.get(ele, -1))
        return result

