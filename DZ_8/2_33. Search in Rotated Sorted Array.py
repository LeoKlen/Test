#https://leetcode.com/problems/search-in-rotated-sorted-array/description/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        i = 0
        j = len(nums) - 1

        while i <= j:
            middle = (i + j) // 2

            if nums[middle] == target:  
                return middle

            if nums[j] < nums[middle]:   
                if nums[i] <= target < nums[middle]:                  
                    j = middle - 1 
                else:            
                    i = middle + 1
            else:
                if nums[middle] < target <= nums[j]:              
                    i = middle + 1
                else:              
                    j = middle - 1
        
        return -1
