class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.countPali(s, i, i)
            res += self.countPali(s, i, i + 1)
        return res
    def countPali(self, s, start, end):
        res = 0
        while start >= 0 and end <= len(s) - 1 and s[start] == s[end]:
            res += 1
            start -= 1
            end += 1
        return res