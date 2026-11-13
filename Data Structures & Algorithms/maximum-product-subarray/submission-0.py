class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cureMax, cureMin = 1, 1
        res = max(nums)
        for n in nums:
            if n == 0:
                cureMin, cureMax = 1, 1
                continue
            temp = cureMax * n
            cureMax = max(n * cureMax, n * cureMin, n)
            cureMin = min(temp, n * cureMin, n)
            res = max(res, cureMax)
        return res