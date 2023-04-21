#https://leetcode.com/problems/find-peak-element/description/
def in_list(arr, i, j):
    if i >= j:
        return i
    
    middle = (i + j) // 2
    
    #if middle == targ:
    
    if arr[middle] > arr[middle + 1]:
        return in_list(arr, i, middle)
    else:
        return in_list(arr, middle + 1, j)


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return in_list(nums, 0, len(nums)-1)
