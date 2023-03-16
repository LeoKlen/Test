#https://leetcode.com/problems/valid-palindrome/description/
class Solution:
    def isPalindrome(self, string: str) -> bool:
        
        l = 0
        r = len(string)-1

        while l<r:

            while string[l] == ' ' and l < r:
                l+=1

            while string[r] == ' '  and l < r:
                r-=1
            
            if string[l] != string[r]:
                return False

            l+=1
            r-=1

        return True
