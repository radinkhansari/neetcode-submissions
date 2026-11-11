class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numset = set(nums)
        for num in nums:
            if num - 1 in numset:
                continue
            length = 1
            while num + length in numset:
                length += 1
            longest = max(longest, length)
        return longest