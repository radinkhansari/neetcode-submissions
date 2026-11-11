class Solution:
    def climbStairs(self, n: int) -> int:
        zero, one = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + zero
            zero = temp
        return one