#https://leetcode.com/problems/first-bad-version/description/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
def in_list( i, j):
    if i >= j:
        return i
    
    middle = (i + j) // 2
    
    #if middle == targ:
    #    return middle
    
    if isBadVersion(middle):
        return in_list(i, middle)
    else:
        return in_list(middle + 1, j)
class Solution:
    def firstBadVersion(self, n: int) -> int:
        return in_list(0, n)
