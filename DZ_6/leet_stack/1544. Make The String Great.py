#https://leetcode.com/problems/make-the-string-great/description/
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
    
        for ch in s:
            if stack and ch.upper() == stack[-1].upper() and ((stack[-1].islower() and ch.isupper()) or (stack[-1].isupper() and ch.islower())) :
                stack.pop()
            else:
                stack.append(ch)
        #print(stack)
        return ''.join(stack)
