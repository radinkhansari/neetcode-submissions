class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        priceMin = float('inf')
        profMax = 0
        for price in prices:
            priceMin = min(priceMin, price)
            profMax = max(profMax, price - priceMin)
        return profMax