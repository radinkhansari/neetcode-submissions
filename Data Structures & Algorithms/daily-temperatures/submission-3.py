class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for indx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stackIndx, stackTemp = stack.pop()
                res[stackIndx] = indx - stackIndx
            stack.append([indx, temp])
        return res