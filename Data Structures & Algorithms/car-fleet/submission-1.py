class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = prev_time = 0
        for pos, spd in sorted(zip(position, speed), reverse=True):
            time2target = (target - pos) / spd
            # print(time2target)
            if time2target > prev_time:
                ans += 1
                prev_time = time2target
        return ans