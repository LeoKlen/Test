#https://leetcode.com/problems/reverse-string/description/
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        for i in range(len(s)):
            s.insert(len(s)-i, s[0])
            s.pop(0)
        print(s)
        return s
