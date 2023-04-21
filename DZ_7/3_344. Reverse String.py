#https://leetcode.com/problems/reverse-string/description/


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def rev(s, i, j):
            
            if i >= j:
                return
            s[i], s[j] = s[j], s[i]
            
            return rev(s, i+1, j-1)
        return rev(s, 0, len(s)-1)
