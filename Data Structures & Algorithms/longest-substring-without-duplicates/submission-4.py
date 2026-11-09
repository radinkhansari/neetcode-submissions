class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, longest = 0, 0
        sett = set()
        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(s[left])
                left += 1
            diff = right - left + 1
            sett.add(s[right])
            longest = max(longest, diff)
        return longest