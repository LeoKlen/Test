#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        
        if nums[j] > nums[i]:
            return nums[0]
        
        while i < j:
            middle = (i + j) // 2     
            if nums[j] < nums[middle]:
                i = middle + 1
            else:
                j = middle 
                
        return nums[i]
