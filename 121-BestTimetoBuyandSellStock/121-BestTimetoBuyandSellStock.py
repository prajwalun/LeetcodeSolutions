# Last updated: 26/03/2025, 17:38:01
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Two Pointer Approach
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            # Check the profit scenario
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                # Update pointers
                l = r
            r += 1
        return maxP