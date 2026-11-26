class Solution:
    def climbStairs(self, n: int) -> int:
        zero, one = 1, 1
        for i in range(n - 1):
            temp = zero
            zero = one
            one = one + temp
        return one