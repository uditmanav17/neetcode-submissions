class Solution:
    def trap(self, arr: List[int]) -> int:
        N = len(arr)
        left_max, right_max = [0] * N, [0] * N
        prev_l_max = prev_r_max = 0
        
        for i in range(N):
            l_ele = arr[i]
            left_max[i] = prev_l_max
            prev_l_max = max(l_ele, prev_l_max)

            r_ele = arr[N - i - 1]
            right_max[N - i - 1] = prev_r_max
            prev_r_max = max(r_ele, prev_r_max)

        water = 0
        for idx in range(N):
            max_height = min(left_max[idx], right_max[idx])
            curr_water = max(max_height - arr[idx], 0)
            water += curr_water

        return water



        