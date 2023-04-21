#https://leetcode.com/problems/binary-search/description/
def bin_search(listik, targ, i, j):
    if i > j:
        return -1
    
    middle = (i + j) // 2
    if targ > listik[-1] or targ < listik[0]:
        return -1
    if targ == listik[middle]:
        return middle
    
    if targ > listik[middle]:
        return bin_search(listik, targ, middle + 1, j)
    if targ < listik[middle]:
        return bin_search(listik, targ, i, middle - 1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return bin_search(nums, target, 0, len(nums))
