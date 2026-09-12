class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        r = 0
        minn = prices[0]
        while r < len(prices):
            if prices[r] < minn:
                minn = prices[r]
            if prices[r] - minn > profit:
                profit = prices[r] - minn
            r += 1

        return profit