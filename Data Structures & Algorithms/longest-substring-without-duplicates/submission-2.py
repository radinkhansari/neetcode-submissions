class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, longest = 0, 0
        sett = set()
        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(s[left])
                left += 1
            sett.add(s[right])
            longest = max(longest, right - left + 1)
        return longest

        '''l = 0
        longest = 0
        sett = set()
        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1

            w = r - l + 1
            longest = max(longest, w)
            sett.add(s[r])
        return longest'''

        '''
        left, longest= 0, 0
        sett = set()
        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(s[left])
                left += 1
            sett.add(s[right])
            longest = max(right - left + 1, longest)
        return longest'''


        left, longest = 0, 0
        sett = set()
        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(r[left])
                left += 1
            sett.add(s[right])
            longest = max(longest, right - left + 1)

                


