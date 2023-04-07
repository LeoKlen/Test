#https://leetcode.com/problems/remove-outermost-parentheses/description/
class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        stack = []
        data = {'(':')'}
        ans = ''
        for ch in s:
            if ch in data:
                if stack:
                    ans += ch
                stack.append(ch)
            elif ch == ')':
                stack.pop()
                if stack:
                    ans += ch
        return ans
