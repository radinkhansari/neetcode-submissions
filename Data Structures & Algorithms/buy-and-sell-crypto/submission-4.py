class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        maxProf = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                diff = price - min_price
                maxProf = max(diff, maxProf)
        return maxProf