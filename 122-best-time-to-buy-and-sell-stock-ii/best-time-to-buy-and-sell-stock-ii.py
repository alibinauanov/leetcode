class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] > prices[l]:
                day_profit = prices[r] - prices[l]
                profit += day_profit
            l = r
            r += 1
        return profit