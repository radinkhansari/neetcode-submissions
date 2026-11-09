class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        res = 0
        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            if heights[left] < heights[right]:
                left += 1
                res = max(res, area)
            else:
                right -= 1
                res = max(res, area)
        return res
            