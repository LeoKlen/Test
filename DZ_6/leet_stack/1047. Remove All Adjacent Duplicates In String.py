#https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
        #print(stack)
        return ''.join(stack)
