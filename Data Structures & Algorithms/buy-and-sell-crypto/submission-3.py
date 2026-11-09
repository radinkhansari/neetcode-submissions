class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_profit= 0
        minn = float('inf')
        for right in range(len(prices)):
            if prices[right] < minn:
                minn = prices[right]
            max_profit = max(prices[right] - minn, max_profit)
        return max_profit