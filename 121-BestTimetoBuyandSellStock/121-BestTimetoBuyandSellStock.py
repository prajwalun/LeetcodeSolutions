# Last updated: 29/04/2025, 20:03:48
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                cur_profit = prices[r] - prices[l]
                maxP = max(maxP, cur_profit)
            else:
                l = r
            r += 1
        return maxP