#https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        data = {'{':'}','[':']','(':')'}

        for ch in s:
            if ch in data:
                stack.append(ch)
            else:
                if len(stack) == 0 or data[stack.pop()] != ch:
                    return False
        if len(stack) > 0:
            return False
        return True
