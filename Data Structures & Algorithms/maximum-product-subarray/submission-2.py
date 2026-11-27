class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cureMin, cureMax = 1, 1
        res = max(nums)
        for num in nums:
            if num == 0:
                cureMin, cureMax = 1, 1
                continue
            else:
                temp = cureMin
                cureMin = min(cureMin * num, cureMax * num, num)
                cureMax = max(temp * num, cureMax * num, num)
            res = max(res, cureMax)
        return res