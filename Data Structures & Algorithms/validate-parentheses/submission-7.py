class Solution:
    def isValid(self, s: str) -> bool:
        dictt = {
            ']' : '[',
            ')' : '(',
            '}' : '{'
        }
        stack = []
        for c in s:
            if c not in dictt:
                stack.append(c)
            else:
                if not stack or stack[-1] != dictt[c]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0