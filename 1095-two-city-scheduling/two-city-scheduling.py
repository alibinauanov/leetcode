class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs.sort(key = lambda x: x[0] - x[1])

        n = len(costs) // 2
        total = 0
        for i in range(n):
            total += costs[i][0] + costs[i + n][1]
        return total

        # -10, -170, 350, 10 -> -170, -10, 10, 350 -> [30, 200], [10, 20], [30, 20], [400, 50]
        # 30 + 20 = 50
        # 10 + 50 = 60
        # 50 + 60 = 110