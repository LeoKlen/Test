#https://leetcode.com/problems/valid-palindrome-ii/description/
class Solution:

    def validPalindrome(self, data: str) -> bool:
        def ispal_2(data,l, r):

            while l<r:
                
                if data[l] != data[r]:
                    return False

                l+=1
                r-=1

            return True
        l = 0
        r = len(data)-1

        while l<r:
            if data[l] != data[r]:
                return ispal_2(data,l+1, r) or ispal_2(data,l, r-1)
            l+=1
            r-=1

        return True
