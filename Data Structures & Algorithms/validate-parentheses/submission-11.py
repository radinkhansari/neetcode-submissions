class Solution:
    def isValid(self, s: str) -> bool:
        dictt = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []
        for c in s:
            if c not in dictt:
                stack.append(c)
            else:
                if stack and stack[-1] == dictt[c]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0