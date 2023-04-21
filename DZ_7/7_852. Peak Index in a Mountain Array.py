# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
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
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return in_list(arr, 0, len(arr)-1)
