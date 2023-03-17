#https://leetcode.com/problems/valid-palindrome/description/
class Solution:
    def isPalindrome(self, string: str) -> bool:
        l = 0
        r = len(string) - 1

        while l < r:
            print(string[l])
            print(string[r])
            while not(string[l].isalpha() or string[l].isdigit())and l < r :
                l += 1

            while not(string[r].isalpha() or string[r].isdigit()) and l < r :
                r -= 1

            if string[l].lower() != string[r].lower():
                return False

            l += 1
            r -= 1

        return True
