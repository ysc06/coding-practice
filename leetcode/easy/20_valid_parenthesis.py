class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        open = {')': '(', ']':'[', '}': '{'}
        for i in s:
            if i in open.values():
                stack.append(i)
            elif i in open:
                if not stack or stack[-1] != open[i]:
                    return False
                stack.pop()
            else:
                return False
        return not stack
