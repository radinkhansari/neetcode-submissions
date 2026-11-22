class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numset = set(nums)
        for num in nums:
            if num - 1 in numset:
                continue
            count = 1
            while num + count in numset:
                count += 1
            longest = max(longest, count)
        return longest