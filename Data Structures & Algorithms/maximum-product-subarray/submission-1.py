class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cureMin, cureMax = 1, 1
        res = max(nums)
        for num in nums:
            if num == 0:
                cureMin, cureMax = 1, 1
                continue
            temp = cureMax * num
            cureMax = max(cureMin * num, cureMax * num, num)
            cureMin = min(cureMin * num, temp, num)
            res = max(res, cureMax)
        return res