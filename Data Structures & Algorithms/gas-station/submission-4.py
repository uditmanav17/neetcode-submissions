class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        min_idx = min_gas = curr = 0
        for idx, (g, c) in enumerate(zip(gas, cost)):
            if curr < min_gas:
                min_gas = curr
                min_idx = idx
            curr += (g - c)

        return min_idx
            

        