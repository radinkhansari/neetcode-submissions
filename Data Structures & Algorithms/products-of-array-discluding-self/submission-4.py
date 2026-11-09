class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before, after = 1, 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] *= before
            before *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= after
            after *= nums[i]
        return res