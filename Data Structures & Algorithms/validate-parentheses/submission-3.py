class Solution:
    def isValid(self, s: str) -> bool:
        dictt = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        stack = []
        for c in s:
            if c in dictt:
                if stack and stack[-1] == dictt[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0