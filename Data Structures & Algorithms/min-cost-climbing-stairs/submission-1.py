class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cumsum = [-1] * len(cost)

        def cost_fun(i):
            if i >= len(cost):
                return 0
            if cumsum[i] >= 0:
                return cumsum[i]
            cumsum[i] = cost[i] + min(cost_fun(i + 1), cost_fun(i + 2))
            return cumsum[i]

        return min(cost_fun(0), cost_fun(1))
