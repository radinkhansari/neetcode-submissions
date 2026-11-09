class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for indx, val in enumerate(nums):
            if indx > 0 and nums[indx] == nums[indx - 1]:
                continue
            left, right = indx + 1, len(nums) - 1
            while left < right:
                currSum = val + nums[left] + nums[right]
                if currSum < 0:
                    left += 1
                elif currSum > 0:
                    right -= 1
                else:
                    res.append([val, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1 
        return res
            

