class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        left = 0
        res = 0
        for right in range(len(s)):
            while left < right and s[right] in sett:
                sett.remove(s[left])
                left += 1
            sett.add(s[right])
            res = max(res, right - left + 1)
        return res