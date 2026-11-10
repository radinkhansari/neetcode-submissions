class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        minPrice = prices[left]
        maxProf = 0
        for right in range(len(prices)):
            if prices[right] < minPrice:
                minPrice = prices[right]
            maxProf = max(prices[right] - minPrice, maxProf)
        return maxProf