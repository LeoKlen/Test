#https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/
class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        data = {'(':')'}
        max_len = 0

        for ch in s:
            if ch in data:
                stack.append(ch)
                if len(stack) > max_len:
                    max_len = len(stack)

            else:
                if ch == ')':
                    stack.pop()
                    continue

        return max_len
