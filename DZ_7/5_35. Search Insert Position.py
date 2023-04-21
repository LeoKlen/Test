#https://leetcode.com/problems/search-insert-position/description/
def in_list(listik, targ, i, j):
    if i > j:
        return i
    
    middle = (i + j) // 2
    
    if listik[middle] == targ:
        return middle
    
    if targ > listik[middle]:
        return in_list(listik, targ, middle + 1, j)
    if targ < listik[middle]:
        return in_list(listik, targ, i, middle - 1)


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return in_list(nums, target, 0, len(nums)-1)
